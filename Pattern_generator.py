print("=" * 50)
print("           PATTERN GENERATOR")
print("=" * 50)

while (choice := int(input("""
Choose a Pattern

1. Square Pattern
2. Right Triangle
3. Inverted Triangle
4. Pyramid
5. Inverted Pyramid
6. Diamond
7. Number Triangle
8. Floyd's Triangle
9. Alphabet Triangle
10. Hollow Square
11. Exit

Enter Your Choice: """))) != 11:

    # -----------------------------
    # 1. Square Pattern
    # -----------------------------
    if choice == 1:
        rows = int(input("\nEnter Number of Rows: "))
        symbol = input("Enter Symbol: ")

        print()

        for i in range(rows):
            for j in range(rows):
                print(symbol, end=" ")
            print()

    # -----------------------------
    # 2. Right Triangle
    # -----------------------------
    elif choice == 2:
        rows = int(input("\nEnter Number of Rows: "))
        symbol = input("Enter Symbol: ")

        print()

        for i in range(1, rows + 1):
            for j in range(i):
                print(symbol, end=" ")
            print()

    # -----------------------------
    # 3. Inverted Triangle
    # -----------------------------
    elif choice == 3:
        rows = int(input("\nEnter Number of Rows: "))
        symbol = input("Enter Symbol: ")

        print()

        for i in range(rows, 0, -1):
            for j in range(i):
                print(symbol, end=" ")
            print()

    # -----------------------------
    # 4. Pyramid
    # -----------------------------
    elif choice == 4:
        rows = int(input("\nEnter Number of Rows: "))
        symbol = input("Enter Symbol: ")

        print()

        for i in range(rows):

            # Spaces
            for j in range(rows - i - 1):
                print(" ", end="")

            # Symbols
            print(symbol * (2 * i + 1))  # Print the symbols in the pyramid shape

            print()

    # -----------------------------
    # 5. Inverted Pyramid
    # -----------------------------
    elif choice == 5:
        rows = int(input("\nEnter Number of Rows: "))
        symbol = input("Enter Symbol: ")

        print()

        for i in range(rows):

            # Spaces
            for j in range(i):
                print(" ", end="")

            # Symbols
            print(symbol * (2 * (rows - i) - 1))  # Print the symbols in the inverted pyramid shape

            print()

        # -----------------------------
    # 6. Diamond
    # -----------------------------
    elif choice == 6:
        rows = int(input("\nEnter Number of Rows: "))
        symbol = input("Enter Symbol: ")

        print()

        # Upper Half
        for i in range(rows):
            for j in range(rows - i - 1):
                print(" ", end="")

            for j in range(2 * i + 1):
                print(symbol, end="")

            print()

        # Lower Half
        for i in range(rows - 2, -1, -1):
            for j in range(rows - i - 1):
                print(" ", end="")

            for j in range(2 * i + 1):
                print(symbol, end="")

            print()

    # -----------------------------
    # 7. Number Triangle
    # -----------------------------
    elif choice == 7:
        rows = int(input("\nEnter Number of Rows: "))

        print()

        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    # -----------------------------
    # 8. Floyd's Triangle
    # -----------------------------
    elif choice == 8:
        rows = int(input("\nEnter Number of Rows: "))

        print()

        number = 1

        for i in range(1, rows + 1):
            for j in range(i):
                print(number, end=" ")
                number += 1
            print()

    # -----------------------------
    # 9. Alphabet Triangle
    # -----------------------------
    elif choice == 9:
        rows = int(input("\nEnter Number of Rows: "))

        print()

        for i in range(1, rows + 1):
            alphabet = 65

            for j in range(i):
                print(chr(alphabet), end=" ")
                alphabet += 1

            print()

    # -----------------------------
    # 10. Hollow Square
    # -----------------------------
    elif choice == 10:
        rows = int(input("\nEnter Size of Square: "))
        symbol = input("Enter Symbol: ")

        print()

        for i in range(rows):
            for j in range(rows):

                if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                    print(symbol, end=" ")
                else:
                    print(" ", end=" ")

            print()

    # -----------------------------
    # Invalid Choice
    # -----------------------------
    else:
        print("\nInvalid Choice! Please enter a number between 1 and 11.")

print("\nThank you for using the Pattern Generator!")