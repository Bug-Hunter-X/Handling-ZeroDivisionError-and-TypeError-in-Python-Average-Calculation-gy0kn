# Python Average Calculation with Error Handling

This repository demonstrates a common coding error in Python: the `ZeroDivisionError` that occurs when dividing by zero and `TypeError` that occurs when performing arithmetic operations with incompatible data types.  The code calculates the average of a list of numbers.  The initial version lacks error handling. A refined version includes robust input validation to prevent these errors and provide more user-friendly output.

## Bug

The original code fails if the input list is empty or contains non-numeric values.

## Solution

The solution adds checks to handle these cases gracefully, returning 0 for empty lists and raising a more informative error message for non-numeric input.
