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

        if stock_level == 0:
            return False, item_id

        success = await self.inventory.decrement_stock(item_id)
        # This may not be successful because in the time we waited
        # to get the stock and item the stock level may have decreased.
        if not success:
            return False, item_id

        self.items_by_category[item["category"]].append(item)

        return True, item_id

    def find_combos(self):
        number_of_combos = None

