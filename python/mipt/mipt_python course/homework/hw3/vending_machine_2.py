"""
It's good if you haven't forgotten about the data structures design from your first homework assignment. In this task
you're supposed to write several functions for interaction with the structure. The use of new materials is a thing to
be welcomed.

Var1 (a vending machine):
1. Put items into a vending machine (think of the limits on the size of the machine)
2. Purchase products
3. Pick up/add cash to the vending machine.
Show a shopping bag composition / Change item prices / Calculate change...

Requirements:
1. At least three of the listed functions are assumed to be necessarily implemented but you can add any you want,
especially if they illustrate recently studied methods and correspond to the practical part of the task.
2. At least one of the functions should include type annotations.
3. Solution should be presented as an opened Pull Request in your GitHub repository from the branch with task solution
to the branch without task solution. You can create new empty repository / fork course repo / use existing repo if you
have one.
"""

vending_machine = {
    'items': {
        'cola': [100, 10],
        'pepsi': [150, 15],
        'fants': [200, 20]
    },
    'cash': 1000,
    'purchase_history': []
}


def add_cash(money: int) -> None:
    if money <= 0:
        raise ValueError()
    vending_machine['cash'] += money


def buy(item_name: str, money: int) -> None:
    vending_machine['items'][item_name][0] -= 1
    vending_machine['cash'] += vending_machine['items'][item_name][1]
    vending_machine['purchase_history'].append([item_name, 1])
    if money > vending_machine['items'][item_name][1]:
        return money - vending_machine['items'][item_name][1]


def finish(money: int) -> None:
    if money <= 0:
        raise ValueError()
    vending_machine['cash'] -= money


def add_items(item_name: str, number: int, price: int = 10):
    if number <= 0 or price <= 0:
        raise ValueError()
    if item_name in vending_machine['items'].keys():
        vending_machine['items'][item_name][0] += number
    else:
        vending_machine['items'][item_name] = [number, price]


def purchase(item_name: str, number: int):
    if number <= 0 \
            or item_name not in vending_machine['items'].keys() \
            or vending_machine['items'][item_name][0] < number:
        raise ValueError()
    vending_machine['items'][item_name][0] -= number
    vending_machine['cash'] += number * vending_machine['items'][item_name][1]
    vending_machine['purchase_history'].append([item_name, 1])
