# Python Stack Implementation & Parentheses Checker

This project is a hands-on exercise to build a fundamental data structure, the Stack, from scratch in Python. It also includes a practical application of the Stack to solve the classic "Balanced Parentheses" problem.


## My Learning Journey

The primary goal of this project was to deepen my understanding of data structures by moving from knowledge to practical implementation. Building the Stack class and then immediately using it to solve a problem helped solidify concepts like LIFO (Last-In, First-Out) and how a stack's methods (`push`, `pop`, `peek`) are used in algorithms.

### The Power of Debugging

A significant part of my learning process involved debugging. While developing the `parenthesis_checker`, I encountered issues where the logic wasn't behaving as expected. To solve this, I relied heavily on using **breakpoints** in my code editor.

By placing a breakpoint inside the `for` loop of the `parenthesis_checker` function, I was able to:

*   **Step through the code line by line:** This allowed me to watch the execution flow and see exactly which `if/elif` block was being entered for each character in the input string.
*   **Inspect variables in real-time:** I could constantly monitor the state of the stack (`s1.data` and `s1.top`) and the value of the current character `x`.
*   **Identify flawed logic:** This process was crucial in identifying a key bug where I was incorrectly trying to get the ASCII value of a method (`s1.peek`) instead of calling the method to get its return value (`s1.peek()`). Seeing the unexpected value of the variable at the breakpoint made the error immediately obvious.

Using the debugger was a powerful lesson in how to effectively troubleshoot and understand what your code is *actually* doing versus what you *think* it's doing.

## Project Components

### 1. The Stack (`stack.py`)

This file contains a custom `Stack` class. It's a fixed-size stack implemented using a Python list as the underlying data store.

#### Core Methods:
*   `__init__(self, height)`: Initializes the stack with a maximum capacity.
*   `push(self, x)`: Adds an element to the top of the stack if it's not full.
*   `pop(self)`: Removes and returns the top element from the stack.
*   `is_empty(self)`: Returns `True` if the stack is empty.
*   `peek(self)`: Returns the top element without removing it.

### 2. The Use Case: Parentheses Checker (`stack_usecase.py`)

This script imports the `Stack` class to solve the "Balanced Parentheses" problem.

#### The Algorithm:

The function `parenthesis_checker(input)` takes a string and determines if the brackets (`()`, `[]`, `{}`) are balanced and correctly nested.

1.  It iterates through each character of the input string.
2.  If an **opening bracket** (`(`, `[`, `{`) is found, it is **pushed** onto the stack.
3.  If a **closing bracket** (`)`, `]`, `}`) is found, the script **peeks** at the character on top of the stack.
4.  If the character on top is the corresponding opening bracket, the script **pops** it from the stack, effectively canceling out the pair.
5.  If the stack is empty when a closing bracket is found, or if the peeked character is not the correct opening bracket, the string is declared unbalanced.
6.  After the entire string has been processed, if the stack is empty, it means every bracket was correctly matched and the string is **balanced**. If the stack is not empty, it means there are unmatched opening brackets, and the string is **unbalanced**.
