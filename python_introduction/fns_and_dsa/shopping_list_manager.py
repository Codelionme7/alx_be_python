"""
shopping_list_manager.py

A simple Shopping List Manager using a Python list.

Features:
- Start with an empty shopping_list
- Add items
- Remove items (case-insensitive match)
- View current list
- Menu-driven loop until exit
"""

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = input("Enter your choice: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if choice == '1':
            item = input("Enter item to add: ").strip()
            if not item:
                print("No item entered. Nothing was added.")
            else:
                shopping_list.append(item)
                print(f"Added '{item}' to the shopping list.")

        elif choice == '2':
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter item to remove: ").strip()
            if not item_to_remove:
                print("No item entered. Nothing was removed.")
                continue

            # Case-insensitive removal: remove the first matching item
            for idx, existing_item in enumerate(shopping_list):
                if existing_item.lower() == item_to_remove.lower():
                    removed = shopping_list.pop(idx)
                    print(f"Removed '{removed}' from the shopping list.")
                    break
            else:
                print(f"'{item_to_remove}' not found in the shopping list.")

        elif choice == '3':
            if not shopping_list:
                print("The shopping list is currently empty.")
            else:
                print("\nCurrent shopping list:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()