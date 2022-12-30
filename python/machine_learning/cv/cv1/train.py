import os
from typing import Dict

import numpy as np
from sklearn.metrics import accuracy_score
import torch
from torch.utils.data import DataLoader
from torch import nn
from torchvision import datasets, transforms
from torch.nn import functional as F

from catalyst import dl
from catalyst.utils import set_global_seed, prepare_cudnn
from catalyst.loggers.console import ConsoleLogger
from contextlib import contextmanager


BATCH_SIZE = 256


class DenseBlock(nn.Module):
    def __init__(self, in_channels, growth_rate, num_layers, kernel_size=3):
        super(DenseBlock, self).__init__()
        self.layers = nn.ModuleList()
        for i in range(num_layers):
            self.layers.append(
                nn.Sequential(
                    nn.Conv2d(
                        in_channels + i * growth_rate,
                        growth_rate,
                        kernel_size,
                        padding=1,
                        bias=False,
                    ),
                    nn.BatchNorm2d(growth_rate),
                    nn.ReLU(inplace=True),
                )
            )

    def forward(self, in_tensor):
        out = in_tensor
        for layer in self.layers:
            out = torch.cat((out, layer(out)), dim=1)
        return out


class DenseNet(nn.Module):
    def __init__(self, num_classes, growth_rate=32, num_dense_blocks=6, num_layers_per_block=6):
        super(DenseNet, self).__init__()
        self.num_classes = num_classes

        self.in_preproc = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
        )

        self.features = nn.ModuleList()
        in_channels = 64
        for i in range(num_dense_blocks):
            self.features.append(
                DenseBlock(in_channels, growth_rate, num_layers_per_block)
            )
            in_channels += growth_rate * num_layers_per_block
            if i < num_dense_blocks - 1:
                self.features.append(
                    nn.Sequential(
                        nn.Conv2d(in_channels, in_channels // 2, kernel_size=1, bias=False),
                        nn.BatchNorm2d(in_channels // 2),
                        nn.ReLU(inplace=True),
                        nn.AvgPool2d(kernel_size=2, stride=2),
                    )
                )
                in_channels = in_channels // 2
        self.features.append(nn.AdaptiveAvgPool2d(1))

        self.classifier = nn.Sequential(
            nn.Dropout(p=0.25),
            nn.Linear(in_channels, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, self.num_classes),
        )

    def forward(self, in_tensor):
        x = self.in_preproc(in_tensor)
        for block in self.features:
            x = block(x)
        feat = torch.flatten(x, 1)
        logits = self.classifier(feat)
        return logits


def _format_metrics(dct):
    return " | ".join([f"{k}: {float(dct[k]):.03}" for k in sorted(dct.keys())])


class CustomLogger(ConsoleLogger):
    """Custom console logger for parameters and metrics.
    Output the metric into the console during experiment.

    Note:
        We inherit ConsoleLogger to overwrite default Catalyst logging behaviour
    """

    def log_metrics(
        self,
        metrics: Dict[str, float],
        scope: str = None,
        # experiment info
        run_key: str = None,
        global_epoch_step: int = 0,
        global_batch_step: int = 0,
        global_sample_step: int = 0,
        # stage info
        stage_key: str = None,
        stage_epoch_len: int = 0,
        stage_epoch_step: int = 0,
        stage_batch_step: int = 0,
        stage_sample_step: int = 0,
        # loader info
        loader_key: str = None,
        loader_batch_len: int = 0,
        loader_sample_len: int = 0,
        loader_batch_step: int = 0,
        loader_sample_step: int = 0,
    ) -> None:
        """Logs loader and epoch metrics to stdout."""
        if scope == "loader":
            prefix = f"{loader_key} ({stage_epoch_step}/{stage_epoch_len}) "
            print(prefix + _format_metrics(metrics))

        elif scope == "epoch":
            prefix = f"* Epoch ({stage_epoch_step}/{stage_epoch_len}) "
            print(prefix + _format_metrics(metrics["_epoch_"]))


def get_transforms():
    # ImageNet mean and std values for image pixel values
    means = np.array((0.4914, 0.4822, 0.4465))
    stds = np.array((0.2023, 0.1994, 0.2010))        
    base_transforms = [transforms.ToTensor(), transforms.Normalize(means, stds)]
    augmented_transforms = [
        transforms.RandomCrop(32, padding=4, padding_mode="reflect"),
        transforms.RandomHorizontalFlip(),
        transforms.ColorJitter(hue=0.01, brightness=0.3, contrast=0.3, saturation=0.3),
    ]
    augmented_transforms += base_transforms

    transform_basic = transforms.Compose(base_transforms)
    transform_augment = transforms.Compose(augmented_transforms)
    return transform_basic, transform_augment


@contextmanager
def infer(model):
    """Fully turns model state to inference (and restores it in the end)"""
    status = model.training
    model.train(False)
    with torch.no_grad():
        try:
            yield None
        finally:
            model.train(status)


def load_ckpt(path, model, device=torch.device("cpu")):
    """
    Load saved checkpoint weights to model
    :param path: full path to checkpoint
    :param model: initialized model class nested from nn.Module()
    :param device: base torch device for validation
    :return: model with loaded 'state_dict'
    """
    assert os.path.isfile(path), FileNotFoundError(f"no file: {path}")

    ckpt = torch.load(path, map_location=device)
    ckpt_dict = ckpt["model_state_dict"]
    model_dict = model.state_dict()
    ckpt_dict = {k: v for k, v in ckpt_dict.items() if k in model_dict}
    model_dict.update(ckpt_dict)
    model.load_state_dict(model_dict)
    return model


@torch.no_grad()
def validate_model(model, loader, device):
    """
    Evaluate implemented model
    :param model: initialized model class nested from nn.Module() with loaded state dict
    :param loader batch data loader for evaluation set
    :param device: base torch device for validation
    :return: dict performance metrics
    """
    label_list = []
    pred_list = []
    model.train(False)
    model = model.to(device)

    for data_tensor, lbl_tensor in loader:
        lbl_values = lbl_tensor.cpu().view(-1).tolist()
        label_list.extend(lbl_values)
        logits = model(data_tensor.to(device))
        scores = F.softmax(logits.detach().cpu(), 1).numpy()
        pred_labels = np.argmax(scores, 1)
        pred_list.extend(pred_labels.ravel().tolist())

    labels = np.array(label_list)
    predicted = np.array(pred_list)
    acc = accuracy_score(labels, predicted)
    print(f"model accuracy: {acc:.4f}")
    metric_dict = {"accuracy": acc}
    return metric_dict


def test(num_classes, val_data_loader, device):
    ckpt_fp = os.path.join("logs", "checkpoints", "best.pth")
    mod = DenseNet(num_classes=num_classes)
    mod = load_ckpt(ckpt_fp, mod).eval()
    new_runner = validate_model(mod, val_data_loader, device)


def main(run_test=True):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    set_global_seed(42)
    prepare_cudnn(True)

    transform_basic, transform_augment = get_transforms()
    train_dataset = datasets.CIFAR10("./cifar10", train=True, download=True, transform=transform_augment)
    valid_dataset = datasets.CIFAR10("./cifar10", train=False, download=True, transform=transform_basic)

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    valid_loader = DataLoader(valid_dataset, batch_size=BATCH_SIZE, shuffle=False)
    loaders = {
        "train": train_loader,
        "valid": valid_loader,
    }

    runner = dl.SupervisedRunner(
        input_key="img", output_key="logits", target_key="targets", loss_key="loss"
    )

    num_classes = len(train_dataset.classes)
    model = DenseNet(num_classes)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = torch.nn.CrossEntropyLoss()

    runner.train(
        model=model,
        criterion=criterion,
        optimizer=optimizer,
        loaders=loaders,
        loggers={"console": CustomLogger()},
        num_epochs=6,
        callbacks=[
            dl.AccuracyCallback(input_key="logits", target_key="targets", topk_args=(1, 3, 5)),
        ],
        logdir="./logs",
        valid_loader="valid",
        valid_metric="loss",
        minimize_valid_metric=True,
        verbose=True,
        load_best_on_end=True,
    )

    if run_test:
        test(num_classes, loaders["valid"], device)


if __name__ == "__main__":
    main()
