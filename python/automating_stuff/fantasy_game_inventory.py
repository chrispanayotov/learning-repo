from collections import Counter
current_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for key, value in inventory.items():
        total += value
        print(f"{value} {key}")
    print(f"Total number of items: {total}")


def add_to_inventory(inventory, loot):
    loot = {item: loot.count(item) for item in loot}
    inventory = Counter(inventory)
    loot = Counter(loot)
    return inventory + loot


current_inventory = add_to_inventory(current_inventory, dragon_loot)
display_inventory(current_inventory)