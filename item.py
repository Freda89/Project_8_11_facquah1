
class Item:
    """A shopping list item."""
    def __init__(self, name):
        """Initialize an item with a name."""
        self.name = name
    def __str__(self):
        """Return the item name."""
        return self.name
