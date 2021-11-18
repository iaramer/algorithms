"""
Imagine, you are developing a vending machine. You need to keep your vending machine state: which items are presented
on which shelves, how much money inside machine to give change, how much money user inserted in current time, which
purchases users made etc. You need to create a data structure for that using known data types.
"""
from typing import Dict, List


class VMachine:
    """Vending machine class."""

    def __init__(self, money_inside=0, item_prices=None, shelve_items=None):
        """
        Instantiate a vending machine.

        :param money_inside: how much money inside.
        :param item_prices: prices of items.
        :param shelve_items: what items are there on the shelves.
        """
        if shelve_items is None:
            shelve_items = dict()
        if item_prices is None:
            item_prices = dict()
        self.item_prices = item_prices  # dict of str keys (item name) and values (cost)
        self.shelve_items = shelve_items  # dict of str keys (shelve id/name) and list values (item name)
        self.money_inside = money_inside

        self.user_balance = 0  # assume that our currency is counted in integer numbers
        self.purchases = dict()  # dict of str keys (item name) and values (number)
        self.purchases_total_cost = dict()  # dict of str keys (item name) and values (number)

    def add_money(self, amount: int) -> None:
        """
        User method to add more money.

        :param amount: amount of money to add.
        """
        if amount < 0:
            raise Exception('Validation error.')
        self.money_inside += amount
        print(f'Balance: {self.money_inside}')

    def purchase(self, item: str) -> None:
        """
        User method to perform a purchase.

        :param item: name of an item.
        """
        if item not in self.item_prices.keys():
            raise Exception(f'There is no item {item} in the price list.')
        if self.money_inside < self.item_prices[item]:
            raise Exception('Not enough money.')
        for shelve, shelve_items in self.shelve_items.items():
            if item in shelve_items:
                shelve_items.remove(item)
                self.user_balance -= self.item_prices[item]
                print(f'Enjoy your {item}!')
                return
        raise Exception(f'No {item} left in the machine!')

    def get_money_back(self) -> int:
        """
        User method. Returns current deposit.

        :return: deposit.
        """
        change = self.user_balance
        self.user_balance = 0
        return change

    def set_item_prices(self, new_item_prices: Dict[str, int]) -> None:
        """
        Admin method. Set new item prices.

        :param new_item_prices: guess what! new item prices!
        """
        self.item_prices = new_item_prices

    def add_shelve_items(self, new_shelve_items: Dict[str, List[str]]) -> None:
        """
        Admin method. Add new shelve items.

        :param new_shelve_items: it's pretty obvious, come on.
        """
        for shelve, items in new_shelve_items.items():
            if shelve not in self.shelve_items.keys():
                raise Exception(f'There is no shelve {shelve} in the machine.')
            else:
                for item in items:
                    if item not in self.item_prices.keys():
                        raise Exception(f'There is no item {item} in the price list.')
                self.shelve_items[shelve] += items

    def add_money_inside(self, amount: int) -> None:
        """
        Admin method. Add more money to the machine.

        :param amount: amount of money.
        """
        if amount < 0:
            raise Exception('Validation error.')
        self.money_inside += amount

    def get_money(self, amount: int) -> int:
        """
        Admin method. Returns money.

        :param amount: amount of money.
        """
        if amount < 0:
            raise Exception('Validation error.')
        if self.money_inside < amount:
            raise Exception(f'Not enough money. Current amount: {self.money_inside}.')
        else:
            self.money_inside -= amount
            return amount
