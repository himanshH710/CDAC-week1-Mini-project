print("=" * 50)
print("              NUMBER ANALYZER")
print("=" * 50)

while (choice := int(input("""
Choose an Option

1. Even or Odd
2. Prime Number
3. Armstrong Number
4. Palindrome Number
5. Factorial
6. Fibonacci Series
7. Multiplication Table
8. Sum of Digits
9. Reverse Number
10. Exit

Enter Your Choice: """))) != 10:

    # Even or Odd
    if choice == 1:
        num = int(input("\nEnter a Number: "))

        if num % 2 == 0:
            print(f"{num} is an Even Number.")
        else:
            print(f"{num} is an Odd Number.")

    # Prime Number
    elif choice == 2:
        num = int(input("\nEnter a Number: "))

        if num <= 1:
            print(f"{num} is not a Prime Number.")
        else:
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(f"{num} is a Prime Number.")
            else:
                print(f"{num} is not a Prime Number.")

    # Armstrong Number
    elif choice == 3:
        num = int(input("\nEnter a Number: "))

        original = num
        digits = len(str(num))
        total = 0

        while num > 0:
            digit = num % 10
            total += digit ** digits
            num //= 10

        if total == original:
            print(f"{original} is an Armstrong Number.")
        else:
            print(f"{original} is not an Armstrong Number.")

    # Palindrome Number
    elif choice == 4:
        num = int(input("\nEnter a Number: "))

        original = num
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num //= 10

        if reverse == original:
            print(f"{original} is a Palindrome Number.")
        else:
            print(f"{original} is not a Palindrome Number.")

    # Factorial
    elif choice == 5:
        num = int(input("\nEnter a Number: "))

        if num < 0:
            print("Factorial does not exist for negative numbers.")
        else:
            factorial = 1

            for i in range(1, num + 1):
                factorial *= i

            print(f"Factorial of {num} = {factorial}")

    # Fibonacci Series
    elif choice == 6:
        terms = int(input("\nEnter Number of Terms: "))

        first = 0
        second = 1

        print("\nFibonacci Series:")

        for i in range(terms):
            print(first, end=" ")
            next_term = first + second
            first = second
            second = next_term

        print()

    # Multiplication Table
    elif choice == 7:
        num = int(input("\nEnter a Number: "))

        print(f"\nMultiplication Table of {num}\n")

        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    # Sum of Digits
    elif choice == 8:
        num = int(input("\nEnter a Number: "))

        original = num
        total = 0

        while num > 0:
            digit = num % 10
            total += digit
            num //= 10

        print(f"Sum of Digits of {original} = {total}")

    # Reverse Number
    elif choice == 9:
        num = int(input("\nEnter a Number: "))

        original = num
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num //= 10

        print(f"Reverse of {original} = {reverse}")

    # Invalid Choice
    else:
        print("\nInvalid Choice! Please select a number between 1 and 10.")

print("\nThank you for using the Number Analyzer!")