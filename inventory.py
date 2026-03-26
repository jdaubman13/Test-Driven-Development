def add_item(inventory, item):
    if item == "":
        raise ValueError("Please add a valid item to inventory")
    elif len(inventory["items"]) >= inventory["capacity"]:
        raise ValueError("Inventory is at max capacity")
    elif inventory["locked"] is True:
        return inventory
    else:
        inventory["items"].append(item)
        return inventory


def remove_item(inventory, item):
    if item not in inventory["items"]:
        raise ValueError("Inventory item not in inventory")
    elif inventory["locked"] is True:
        return inventory
    else:
        inventory["items"].remove(item)
        return inventory


def get_item_count(inventory):
    return len(inventory["items"])
