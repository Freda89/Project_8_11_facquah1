
import json


class FileManager:
    """Handles JSON for shopping list data."""

    def __init__(self, filename):
        """Save the file name."""
        self.filename = filename

    def load_items(self):
        """Load the shopping list from the JSON file."""
        try:
            with open(self.filename, "r") as file:
                items = json.load(file)

        except FileNotFoundError:
            return []
        
        except json.JSONDecodeError:
            print("The items file is not valid JSON. Starting with an empty list.")
            return []

        except OSError as error:
            print(f"Could not load items: {error}")
            return []
        
        if not isinstance(items, list):
            print("The items file must contain a JSON list. Starting with an empty list.")
            return []
        return items

    def save_items(self, items):
        """Save item dictionaries as formatted JSON."""
        try:
            with open(self.filename, "w") as file:
                json.dump(items, file, indent=4)
   
        except OSError as error:
            print(f"Could not save items: {error}")
            return False
        
        return True
