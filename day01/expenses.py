#!/usr/bin/env python3
"""
Created by CoPilot on 2024-06-08
expenses.py

Collects between 5 and 10 expense amounts from the user, then prints the total and average.
If the total exceeds 10_000, prints a warning in Hungarian.

Design choices & complexity notes (brief):
- Time complexity: O(n) where n is number of expenses entered. Reading each input and updating a running total is inherently linear.
- Space complexity: O(1) extra memory. We do NOT store all inputs in a list; instead we maintain a running sum and a counter.
    This is more memory-efficient than collecting values into a list then calling sum()/len(), especially for large n.
    For this use-case (5-10 inputs) both approaches are fine, but O(1) is a better general pattern.
- Validation is done per-input to ensure numeric and non-negative values; this keeps the program robust.
"""

def read_int_in_range(prompt: str, min_v: int, max_v: int) -> int:
        """Prompt until the user enters an integer in [min_v, max_v]."""
        while True:
                try:
                        val = int(input(prompt).strip())
                        if min_v <= val <= max_v:
                                return val
                        print(f"Please enter an integer between {min_v} and {max_v}.")
                except ValueError:
                        print("Invalid integer. Try again.")

def read_nonnegative_float(prompt: str) -> float:
        """Prompt until the user enters a non-negative float."""
        while True:
                try:
                        val = float(input(prompt).strip())
                        if val >= 0:
                                return val
                        print("Please enter a non-negative number.")
                except ValueError:
                        print("Invalid number. Try again.")

def main() -> None:
        count = read_int_in_range("How many expenses will you enter? (5-10): ", 5, 10)

        total = 0.0  # running sum -> O(1) extra space
        for i in range(1, count + 1):
                amt = read_nonnegative_float(f"Expense #{i}: ")
                total += amt  # update running sum

        average = total / count if count else 0.0  # count is guaranteed non-zero here

        # Print results with two decimal places
        print(f"\nTotal: {total:.2f}")
        print(f"Average: {average:.2f}")

        # Business rule: warn if total exceeds 10,000
        if total > 10_000:
                print("Túl sokat, költöttél, holnap figyelj a költéseidre!")

if __name__ == "__main__":
        main()