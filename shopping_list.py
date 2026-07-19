from shopping_item import ShoppingItem

class ShoppingList:
    """Manage an ordered collection of ShoppingItem objects."""

    def __init__(self):
        """Create an empty shopping list."""
        self.items = []

    def add_item(self, name):
        """Add and return a new shopping item with name."""
        item = ShoppingItem(name)
        self.items.append(item)
        return item

    def display_items(self):
        """Print all items with their number and purchase status."""
        if not self.items:
            print("No items in the shopping list.")
            return

        print("\nShopping Items:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item}")

    def _get_item(self, index):
        """Return an item selection or if invalid."""
        if index < 1 or index > len(self.items):
            raise IndexError("Item index out of range.")
        return self.items[index - 1]

    def mark_item_purchased(self, index):
        """Mark the numbered item as purchased and return its name."""
        item = self._get_item(index)
        item.mark_purchased()
        return item.name

    def delete_item(self, index):
        """Remove the item and return its name."""
        removed_item = self._get_item(index)
        self.items.pop(index - 1)
        return removed_item.name

    def to_dict_list(self):
        """Return a JSON dictionary for every item."""
        return [item.to_dict() for item in self.items]

    def load_items(self, item_dicts):
        """Replace items with JSON format."""
        self.items = []
        for item_data in item_dicts:
            if not isinstance(item_data, dict):
                continue
            name = item_data.get("name")
            if isinstance(name, str) and name.strip():
                self.items.append(ShoppingItem(name, item_data.get("purchased", False)))
