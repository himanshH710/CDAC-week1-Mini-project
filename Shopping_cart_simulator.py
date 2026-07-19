print("=" * 55)
print("             SHOPPING CART SIMULATOR")
print("=" * 55)

# Lists to store products and prices
products = []
prices = []

while (choice := int(input("""
Choose an Option

1. Add Product
2. Remove Product
3. View Cart
4. Search Product
5. Total Items
6. Generate Bill
7. Clear Cart
8. Exit

Enter Your Choice: """))) != 8:

    # -----------------------------
    # 1. Add Product
    # -----------------------------
    if choice == 1:

        product = input("\nEnter Product Name: ")
        price = float(input("Enter Product Price: ₹"))

        products.append(product)
        prices.append(price)

        print(f"\n'{product}' added successfully!")

    # -----------------------------
    # 2. Remove Product
    # -----------------------------
    elif choice == 2:

        if len(products) == 0:
            print("\nCart is Empty!")
        else:
            product = input("\nEnter Product Name to Remove: ")

            if product in products:

                index = products.index(product)

                products.pop(index)
                prices.pop(index)

                print(f"\n'{product}' removed successfully!")

            else:
                print("\nProduct not found!")

    # -----------------------------
    # 3. View Cart
    # -----------------------------
    elif choice == 3:

        if len(products) == 0:
            print("\nYour cart is empty.")
        else:

            print("\n" + "=" * 40)
            print("YOUR SHOPPING CART")
            print("=" * 40)

            for i in range(len(products)):
                print(f"{i+1}. {products[i]:20} ₹{prices[i]}")

            print("=" * 40)

    # -----------------------------
    # 4. Search Product
    # -----------------------------
    elif choice == 4:

        if len(products) == 0:
            print("\nCart is Empty!")

        else:

            product = input("\nEnter Product Name to Search: ")

            if product in products:

                index = products.index(product)

                print("\nProduct Found!")
                print(f"Product : {products[index]}")
                print(f"Price   : ₹{prices[index]}")

            else:
                print("\nProduct not found!")

        # -----------------------------
    # 5. Total Items
    # -----------------------------
    elif choice == 5:

        print(f"\nTotal Products in Cart: {len(products)}")

    # -----------------------------
    # 6. Generate Bill
    # -----------------------------
    elif choice == 6:

        if len(products) == 0:
            print("\nCart is Empty!")

        else:

            subtotal = 0

            print("\n" + "=" * 50)
            print("               FINAL BILL")
            print("=" * 50)

            for i in range(len(products)):
                print(f"{i+1}. {products[i]:20} ₹{prices[i]}")
                subtotal += prices[i]

            print("-" * 50)

            discount = subtotal * 10 / 100
            gst = (subtotal - discount) * 18 / 100

            # Operator Precedence
            final_bill = (subtotal - discount) + gst

            print(f"Subtotal      : ₹{subtotal:.2f}")
            print(f"Discount (10%): ₹{discount:.2f}")
            print(f"GST (18%)     : ₹{gst:.2f}")
            print("-" * 50)
            print(f"Final Bill    : ₹{final_bill:.2f}")
            print("=" * 50)

    # -----------------------------
    # 7. Clear Cart
    # -----------------------------
    elif choice == 7:

        if len(products) == 0:
            print("\nCart is already empty!")

        else:
            products.clear()
            prices.clear()

            print("\nCart Cleared Successfully!")

    # -----------------------------
    # Invalid Choice
    # -----------------------------
    else:
        print("\nInvalid Choice! Please select between 1 and 8.")

print("\nThank you for using Shopping Cart Simulator!")
print("Visit Again!")