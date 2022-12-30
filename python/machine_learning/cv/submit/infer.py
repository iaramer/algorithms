import os
import onnxruntime as rt
import numpy as np
import cv2
import yaml
from torchvision import transforms
from tqdm import tqdm


LABEL_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


sess = rt.InferenceSession("densenet.onnx")


input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()[0].name

means = np.array((0.4914, 0.4822, 0.4465))
stds = np.array((0.2023, 0.1994, 0.2010))        
base_transform = transforms.Compose([
    transforms.ToTensor(), 
    transforms.Normalize(means, stds)
])

with open('predictions.yaml', 'w') as f:
    for filename in tqdm(os.listdir('imgs')):
        try:
            img = cv2.imread(os.path.join('imgs', filename), cv2.IMREAD_COLOR)
            img = cv2.resize(img, (32, 32))
            img_tensor = base_transform(img).numpy()
            img_tensor = np.expand_dims(img_tensor, axis=0)

            output_tensor = sess.run([output_name], {input_name: img_tensor})[0]
            predicted_class = np.argmax(output_tensor)

            f.write(f'{filename} {LABEL_NAMES[predicted_class]}\n')
        except:
            f.write(f'{filename} (error, please check if the file is a valid image)\n')
