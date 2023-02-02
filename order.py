import asyncio
from combo import Combo


class Order:
    def __init__(self, inventory):
        self.inventory = inventory
        self.items_by_category = {"Burgers": [], "Sides": [], "Drinks": []}
        self.combos = []