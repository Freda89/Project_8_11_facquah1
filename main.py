from shopping_list import ShoppingList
from file_manager import FileManager

def display_menu():
    """Display the menu options to the user."""
    print("\nShopping List Manager")
    print("1. Add a shopping item")
    print("2. View all shopping items")
    print("3. Mark an item as purchased")
    print("4. Delete an item")
    print("5. Exit")


def get_user_choice():
    """Return the user's menu choice as an integer."""
    try:
        choice = int(input("Enter a choice (1-5): "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return None

def main():
    """Run the main shopping list manager program."""
    file_manager = FileManager("items.json")
    shopping_list = ShoppingList()
    shopping_list.load_items(file_manager.load_items())

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            name = input("Enter the item name: ").strip()
            if name:
                try:
                    shopping_list.add_item(name)
                except ValueError as error:
                    print(error)
                    continue
                file_manager.save_items(shopping_list.to_dict_list())
                print(f"Added '{name}'.")
            else:
                print("Item name cannot be empty.")

        elif choice == 2:
            shopping_list.display_items()

        elif choice == 3:
            try:
                index = int(input("Enter the item number to mark as purchased: "))
                shopping_list.mark_item_purchased(index)
                file_manager.save_items(shopping_list.to_dict_list())
            except ValueError:
                print("Please enter a valid item number.")
            except IndexError:
                print("Item number is out of range.")

        elif choice == 4:
            try:
                index = int(input("Enter the item number to delete: "))
                removed_name = shopping_list.delete_item(index)
                file_manager.save_items(shopping_list.to_dict_list())
                print(f"Deleted '{removed_name}'.")
            except ValueError:
                print("Please enter a valid item number.")
            except IndexError:
                print("Item number is out of range.")

        elif choice == 5:
            print("Exiting the shopping list manager. Goodbye!")
            break

        else:
            print("Please choose a valid option from 1 to 5.")

if __name__ == "__main__":
    main()
