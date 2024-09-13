"""
# Factorial Calculator

## Metadata
- Level: 1
- Title: Factorial Calculator
- Topics: Functions, Recursion, Error Handling

## Instructions
Write a function called `calculate_factorial(n)` that computes the factorial of a given 
number `n`. The function should return the factorial value. Raise `ValueError` if
input is not a positive integer.

## How to Test
Run the following command in your terminal:
```bash
python -m unittest tests.test_ex_03
```

## Hints
- Factorial of n is the product of all positive integers less than or equal to n.
- You can use recursion or a loop to calculate the factorial.
- Remember to handle edge cases (0, 1) correctly.
- Be careful with large inputs to avoid reaching Python's maximum recursion depth.

## Notes
- Do not remove or rename `calculate_factorial()`, it's required and should not be altered.-
- You can create your own helper functions if needed.
- Make sure your implementation can handle large inputs efficiently.
"""


def calculate_factorial(n):
    result = 1
    if not isinstance(n,int):
        raise ValueError
    elif isinstance(n,bool):
        raise ValueError
    elif n < 0:
        raise ValueError
    for i in range(1,n+1):
        result = result * i
    return result
    