
from item import Item

class ShoppingItem(Item):
    """Represent one named shopping item and its purchase status."""

    def __init__(self, name, purchased=False):
        """Create a shopping item with its optional purchase status."""
        super().__init__(name)
        self.purchased = bool(purchased)

    def mark_purchased(self):
        """Mark the item as purchased."""
        self.purchased = True

    def to_dict(self):
        """Return JSON data format for an item."""
        return {"name": self.name, "purchased": self.purchased}

    def __str__(self):
        """Return item and it's status"""
        status = "Purchased" if self.purchased else "Not purchased"
        return f"{self.name} - {status}"
