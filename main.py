import asyncio
from inventory import Inventory
from order import Order

def display_catalogue(catalogue):
    burgers = catalogue["Burgers"]
    sides = catalogue["Sides"]
    drinks = catalogue["Drinks"]

    print("--------- Burgers -----------\n")
    for burger in burgers:
        item_id = burger["id"]
        name = burger["name"]
        price = burger["price"]
        print(f"{item_id}. {name} ${price}")

    print("\n---------- Sides ------------")
    for side in sides:
        sizes = sides[side]

        print(f"\n{side}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n---------- Drinks ------------")
    for beverage in drinks:
        sizes = drinks[beverage]

        print(f"\n{beverage}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n------------------------------\n")


async def get_order(inventory, num_items):
    order = Order(inventory)
    tasks = []

    print("Please enter the number of items that you would like to add to your order. Enter q to complete your order.")
    while True:
        item_id = input("Enter an item number: ")
        if item_id == "q":
            break

        if not item_id.isdigit():
            print("Please enter a valid number.")
            continue

        item_id = int(item_id)
        if item_id > num_items:
            print(f"Please enter a number below {num_items + 1}.")
            continue

        add_to_order_task = asyncio.create_task(order.add_item(item_id))
        tasks.append(add_to_order_task)

    print("Placing order...")

    for task in tasks:
        # if the task returns False we could not add the item
        # to the order because the item is out of stock
        in_stock, item_id = await task

        if not in_stock:
            print(
                f"Unfortunately item number {item_id} is out of stock and has been removed from your order. Sorry!")

    return order


def display_order(order, sub_total, tax, total):
    print("\nHere is a summary of your order: \n")
    print(order)
    print(f"\nSubtotal: ${round(sub_total, 2)}")
    print(f"Tax: ${round(tax, 2)}")
    print(f"Total: ${round(sub_total + tax, 2)}")


