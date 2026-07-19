"""Tests for the ShoppingItem model in Shopping List Manager."""

from shopping_item import ShoppingItem

def test_mark_purchased_sets_flag():
    """A purchased item should update its purchased status."""
    item = ShoppingItem("Milk")  # create an item named Milk
    assert item.purchased is False  # the item starts as not purchased
    item.mark_purchased()  # mark the item as purchased
    assert item.purchased is True  # the item should now be purchased


def test_to_dict_returns_expected_data():
    """ShoppingItem.to_dict returns the correct JSON format."""
    item = ShoppingItem("Bread")  # create an item named Bread
    assert item.to_dict() == {"name": "Bread", "purchased": False}  # verify dict output matches the model state
