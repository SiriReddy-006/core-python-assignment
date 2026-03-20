menu = ["Pizza", "Burger", "Pasta", "Salad"]

def add_item():
    x = input("Add item: ")
    menu.append(x)
    print("Item added.")

def remove_item():
    y = input("Remove item: ")
    if y in menu:
        menu.remove(y)
        print("Item removed.")
    else:
        print("Item not found.")

def check_item():
    z = input("Check item: ")
    if z in menu:
        print(z, "is available")
    else:
        print("Not available")


def main():
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Check item")
    print("4. Show menu")

    choice = int(input("Choose option (1-4): "))
    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        check_item()
    elif choice == 4:
        print("Menu:", menu)
    else:
        print("Invalid choice")

    print("Updated menu:", menu)


main()
