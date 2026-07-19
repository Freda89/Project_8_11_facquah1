"""Tests for the ShoppingList behavior in Shopping List Manager."""

import pytest  # pytest is used for fixtures and expressive assertions

from shopping_list import ShoppingList  # import the class under test


@pytest.fixture
def shopping_list():
    """Provide a fresh ShoppingList instance for each test."""
    return ShoppingList()  # a clean list for every test


def test_add_item_increases_list(shopping_list):
    """Adding an item should increase the list length."""
    shopping_list.add_item("Eggs")  # add an item named Eggs
    assert len(shopping_list.items) == 1  # one item should now exist
    assert shopping_list.items[0].name == "Eggs"  # the item name should match


def test_mark_item_purchased_changes_status(shopping_list):
    """Marking an item purchased should update its status."""
    shopping_list.add_item("Juice")  # insert a new item
    shopping_list.mark_item_purchased(1)  # mark the first item as purchased
    assert shopping_list.items[0].purchased is True  # status should now be True


def test_delete_item_removes_item(shopping_list):
    """Deleting an item should remove it and return the name."""
    shopping_list.add_item("Cheese")  # add an item to delete
    removed_name = shopping_list.delete_item(1)  # delete the first item
    assert removed_name == "Cheese"  # confirm the returned name
    assert len(shopping_list.items) == 0  # the list should be empty afterward


def test_to_dict_list_returns_correct_structure(shopping_list):
    """to_dict_list should serialize shopping items to dictionaries."""
    shopping_list.add_item("Butter")  # add a test item
    assert shopping_list.to_dict_list() == [{"name": "Butter", "purchased": False}]  # verify the result


def test_load_items_restores_item_data(shopping_list):
    """Loading item dictionaries should recreate ShoppingItem instances."""
    shopping_list.load_items([{"name": "Apples", "purchased": True}])  # load data from JSON-like dicts
    assert len(shopping_list.items) == 1  # one item should be present
    assert shopping_list.items[0].name == "Apples"  # item name should restore
    assert shopping_list.items[0].purchased is True  # purchase state should restore
