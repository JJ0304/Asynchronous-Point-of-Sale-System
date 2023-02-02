import asyncio
from combo import Combo


class Order:
    def __init__(self, inventory):
        self.inventory = inventory
        self.items_by_category = {"Burgers": [], "Sides": [], "Drinks": []}
        self.combos = []

    async def add_item(self, item_id):
        stock_level, item = await asyncio.gather(
            self.inventory.get_stock(item_id), self.inventory.get_item(item_id)
        )