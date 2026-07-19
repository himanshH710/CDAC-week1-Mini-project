# 🐍 Python Fundamentals Mini Projects

## 📌 Overview

This repository contains a collection of beginner-friendly Python mini projects created to strengthen core programming fundamentals. Each project focuses on solving a real-world problem while reinforcing essential Python concepts through hands-on practice.

---

## 🎯 Learning Objectives

These projects are designed to help practice:

* Variables
* Input and Output
* Arithmetic & Comparison Operators
* Operator Precedence
* Strings
* Lists
* Loops (`for` and `while`)
* Conditional Statements (`if`, `elif`, `else`)
* Pattern Printing
* Walrus Operator (`:=`)

---

## 📚 Projects Included

### 1. 🎓 Student Result Calculator

The **Student Result Calculator** is a command-line application that automates the process of evaluating a student's academic performance. The user enters the student's name and marks for five subjects, after which the program performs various calculations and displays a detailed result summary.

The application calculates the **total marks, average, percentage, highest score, lowest score**, and counts the number of subjects with marks greater than or equal to **90**. It also determines the student's **grade** based on the percentage and checks whether the student has **passed or failed** by ensuring the minimum passing marks are met in every subject.

This project provides practical experience with user input, data storage using lists, loops, conditional statements, mathematical operations, and formatted output, making it an excellent first project for learning Python fundamentals.

**Key Features**

* Accepts student name and marks for five subjects.
* Calculates total, average, and percentage.
* Finds the highest and lowest marks.
* Counts subjects scoring **90 or above**.
* Assigns a grade based on percentage.
* Displays the final result as **Pass** or **Fail**.
* Presents all information in a clean and readable format.

**Concepts Used**

* Variables
* Input & Output
* Lists
* Loops
* Arithmetic & Comparison Operators
* Operator Precedence
* Conditional Statements
* String Formatting

> *(The remaining projects will be added as they are completed.)*

---

## 🚀 How to Run

1. Install Python 3.
2. Open a terminal in the project directory.
3. Run the desired Python file:

```bash
python Student_result_calculator.py
```

---

## 💡 Why This Repository?

The goal of this repository is to build a strong foundation in Python before moving on to advanced topics such as functions, dictionaries, file handling, object-oriented programming, databases, and frameworks.

---

---------------------------------------------------------------------------------------------------

---

## 2. 🔢 Number Analyzer

The **Number Analyzer** is a menu-driven command-line application that performs a variety of mathematical operations on numbers. Users can repeatedly choose different operations from the menu, making it a practical project for learning loops, decision-making, and mathematical problem-solving.

The application includes several commonly used number-based algorithms such as checking whether a number is **Even or Odd**, determining if it is a **Prime Number**, verifying **Armstrong Numbers** and **Palindrome Numbers**, calculating the **Factorial**, generating the **Fibonacci Series**, displaying a **Multiplication Table**, finding the **Sum of Digits**, and reversing a number. The program continues running until the user chooses to exit, demonstrating the use of the **Walrus Operator (`:=`)** in a real-world scenario.

This project strengthens logical thinking and introduces mathematical algorithms while improving confidence with menu-driven programming.

### Key Features

* Menu-driven interface for easy navigation.
* Checks whether a number is Even or Odd.
* Determines whether a number is Prime.
* Identifies Armstrong Numbers.
* Identifies Palindrome Numbers.
* Calculates the Factorial of a number.
* Generates the Fibonacci Series.
* Displays the Multiplication Table.
* Calculates the Sum of Digits.
* Reverses a given number.
* Uses the Walrus Operator (`:=`) for continuous user interaction.

### Mathematical Concepts

**Even/Odd:** Determines whether a number is divisible by **2**.

**Prime Number:** A number greater than **1** that has exactly two factors: **1** and itself.

**Armstrong Number:** A number that is equal to the sum of its own digits, where each digit is raised to the power of the total number of digits.

* Example: **153 = 1³ + 5³ + 3³ = 153**

**Palindrome Number:** A number that remains the same when read from left to right or right to left.

* Example: **121, 1331, 4554**

**Factorial:** The product of all positive integers from **1** to a given number.

* Example: **5! = 5 × 4 × 3 × 2 × 1 = 120**

**Fibonacci Series:** A sequence in which each number is the sum of the previous two numbers.

* Example: **0, 1, 1, 2, 3, 5, 8, 13...**

**Sum of Digits:** Adds all the digits of a number together.

* Example: **456 → 4 + 5 + 6 = 15**

**Reverse Number:** Reverses the order of digits in a number.

* Example: **12345 → 54321**

### Concepts Used

* Variables
* Input & Output
* Arithmetic & Comparison Operators
* Assignment Operators
* Operator Precedence
* Conditional Statements
* `for` Loops
* `while` Loops
* Walrus Operator (`:=`)
* String Formatting
* Mathematical Algorithms
* Menu-Driven Programming

> *(The remaining projects will be added as they are completed.)*

---

## 🚀 How to Run

1. Install Python 3.
2. Open a terminal in the project directory.
3. Run the desired Python file:

```bash
python Number_Analyzer.py
```

---

## 💡 Why This Repository?

The goal of this repository is to build a strong foundation in Python before moving on to advanced topics such as functions, dictionaries, file handling, object-oriented programming, databases, and frameworks.

---

---------------------------------------------------------------------------------------------------

---

## 3. ⭐ Pattern Generator

The **Pattern Generator** is a menu-driven command-line application that generates a variety of star, number, and alphabet patterns based on the user's selection. This project is designed to strengthen the understanding of **nested loops**, one of the most important concepts in Python programming.

Users can choose from multiple pattern types, including square, triangle, pyramid, diamond, number, alphabet, and hollow patterns. Each pattern demonstrates how different combinations of loops and conditions can produce unique outputs. The program continues running until the user selects the exit option, utilizing the **Walrus Operator (`:=`)** for efficient menu handling.

This project focuses on developing logical thinking by teaching how rows, columns, spaces, and symbols interact within nested loops, making it an excellent exercise for mastering pattern-based programming.

### Key Features

* Menu-driven interface for selecting different patterns.
* Generates Square Pattern.
* Generates Right Triangle Pattern.
* Generates Inverted Triangle Pattern.
* Generates Pyramid Pattern.
* Generates Inverted Pyramid Pattern.
* Generates Diamond Pattern.
* Generates Number Triangle.
* Generates Floyd's Triangle.
* Generates Alphabet Triangle.
* Generates Hollow Square Pattern.
* Uses the Walrus Operator (`:=`) for continuous execution until the user exits.

### Pattern Concepts

**Square Pattern:** Prints a fixed number of rows and columns, forming a complete square.

**Right Triangle:** Prints symbols in increasing order, where the number of symbols equals the current row number.

**Inverted Triangle:** Prints symbols in decreasing order, reducing one symbol in each row.

**Pyramid:** Combines leading spaces and an increasing odd number of symbols to create a centered pyramid.

**Inverted Pyramid:** Reverses the pyramid logic by increasing spaces and decreasing the number of symbols.

**Diamond:** Forms a diamond by combining a pyramid and an inverted pyramid while avoiding duplication of the middle row.

**Number Triangle:** Displays numbers in increasing order on each row, beginning from **1**.

**Floyd's Triangle:** Prints consecutive numbers continuously without restarting from **1** on each new row.

**Alphabet Triangle:** Displays alphabets in increasing order using the `chr()` function and ASCII values.

**Hollow Square:** Prints symbols only along the border of the square while leaving the inner area empty.

### Concepts Used

* Variables
* Input & Output
* Strings
* Nested `for` Loops
* `while` Loop
* Walrus Operator (`:=`)
* Conditional Statements (`if`, `elif`, `else`)
* Pattern Printing Logic
* Character Manipulation using `chr()`
* Arithmetic & Comparison Operators
* Operator Precedence
* Menu-Driven Programming

---

---------------------------------------------------------------------------------------------------

---

**Language:** Python 3
