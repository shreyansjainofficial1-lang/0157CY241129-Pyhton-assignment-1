library = {"Python Basics": 5, "Clean Code": 3, "Computer Networks": 2}

while True:
    print("\\n1. View books  2. Add/update book  3. Borrow book  4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        for book, quantity in library.items():
            print(f"{book}: {quantity}")
    elif choice == "2":
        book = input("Book name: ")
        quantity = int(input("Quantity to add: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
        else:
            library[book] = library.get(book, 0) + quantity
            print("Book quantity updated.")
    elif choice == "3":
        book = input("Book name to borrow: ")
        if library.get(book, 0) > 0:
            library[book] -= 1
            print("Book issued.")
        else:
            print("Book unavailable.")
    elif choice == "4":
        print("Exiting library system.")
        break
    else:
        print("Invalid option.")
