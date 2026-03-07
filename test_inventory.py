import pytest
from inventory import add_item, remove_item, get_item_count

def test_add_item_works_on_empty(empty_inventory):
    result = add_item(empty_inventory, "Sword")
    assert "Sword" in result["items"]

def test_add_item_rejects_empty_string_on_empty(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory, "")

def test_add_item_rejects_on_full(full_inventory):
    with pytest.raises(ValueError):
        add_item(full_inventory, "67")

def test_add_item_rejects_on_locked(locked_inventory):
    result = add_item(locked_inventory, "Shield")
    assert result["items"] == ["sword"]

def test_remove_item_works(empty_inventory):
    empty_inventory["items"] = ["b","a","b"]
    result = remove_item(empty_inventory, "b")
    assert result["items"] == ["a","b"]

def test_remove_item_rejects_unkown_item(full_inventory):
    with pytest.raises(ValueError):
        remove_item(full_inventory, "b")

def test_locked_inventory_cannot_be_removed(locked_inventory):
    result = remove_item(locked_inventory, "sword")
    assert "sword" in result["items"]

def test_get_item_count_works(full_inventory):
    result = get_item_count(full_inventory)
    assert result == 10

def test_get_item_count_returns_zero(empty_inventory):
    result = get_item_count(empty_inventory)
    assert result == 0

def test_get_item_count_works_on_locked(locked_inventory):
    result = get_item_count(locked_inventory)
    assert result == 1
