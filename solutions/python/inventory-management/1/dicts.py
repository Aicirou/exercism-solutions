"""Functions to keep track and alter inventory."""


def create_inventory(items: list[str]) -> dict[str]:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    return add_items({}, items)


def add_items(inventory: dict[str], items: list[str]) -> dict[str]:
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    for item in items:
        inventory[item] = inventory.setdefault(item, 0) + 1
    return inventory


def decrement_items(inventory: dict[str], items: list[str]) -> dict[str]:
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    for item in items:
        # Only decrement if the item exists and the count is above 0
        if inventory.get(item, 0) > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory: dict[str], item: str) -> dict[str]:
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    # .pop(key, None) removes the key safely if it exists, otherwise does nothing
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory: list[str]) -> list[tuple]:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    # Filter items with count > 0 using a list comprehension
    return [(item, count) for item, count in inventory.items() if count > 0]
