#!/usr/bin/env python3
"""Modify expenses_simple.py to use functions for better organization and readability."""

def get_expenses():
    expenses = []

    while True:
        user_input = input("Add meg a kiadást, vagy ha végeztél, írd be, hogy stop: ")
        
        if user_input.lower() == "stop":
            break

        try:
            value = int(user_input)
            expenses.append(value)
        except ValueError:
            print("Érvénytelen bemenet. Kérem, adjon meg egy számot vagy írja be 'stop'-ot a befejezéshez.")

    # print ("Bevitt kiadások:", expenses)
    return expenses


def calculate_total(expenses):

    total = sum(expenses)

    # print("Kiadások összege:", total)
    return total


def calculate_avg(expenses):

    avg = sum(expenses) / len(expenses)

    # print("Kiadások átlaga:", avg)
    return avg


def main():
    exp = get_expenses()
    total = calculate_total(exp)
    avg = calculate_avg(exp)

    print("Összesen:", total)
    print("Átlag:", avg)

    if total > 10000:
        print("Túl sokat költöttél ma!")


if __name__ == "__main__":
        main()