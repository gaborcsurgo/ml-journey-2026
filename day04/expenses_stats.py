#!/usr/bin/env python3
"""Modify expenses_simple.py to use functions for better organization and readability.

Adding more statistical metrics to the expenses program. 
In addition to calculating the total and average of the entered expenses, 
also calculate and display the minimum and maximum expense. 
Also show, how many inputs were entered and how many of them ara above the average.
Mean and median should also be calculated and displayed.
If the total exceeds 10,000, it should still display a warning message.
"""

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


def calculate_max_min(expenses):

    max_expense = max(expenses)
    min_expense = min(expenses)

    return max_expense, min_expense
    

def calculate_counts(expenses):

    count = len(expenses)
    avg = calculate_avg(expenses)
    above_avg_count = sum(1 for e in expenses if e > avg)

    return count, above_avg_count


def calculate_mean_median(expenses):

    mean = sum(expenses) / len(expenses)

    sorted_expenses = sorted(expenses)
    n = len(expenses)

    if n % 2 == 1:
        median = sorted_expenses[n // 2]
    else:
        median = (sorted_expenses[n // 2 - 1] + sorted_expenses[n // 2]) / 2

    return mean, median


def main():

    exp = get_expenses()

    if not exp:
        print("Nem adtál meg egyetlen kiadást sem. Indítsd újra a programot és adj meg legalább egy kiadást.")
        return
    
    total = calculate_total(exp)
    avg = calculate_avg(exp)
    max_expense, min_expense = calculate_max_min(exp)
    count, above_avg_count = calculate_counts(exp)
    mean, median = calculate_mean_median(exp)

    print("Összesen:", total)
    print(f"Átlag: {avg:.3f}")
    print("Maximum kiadás:", max_expense)
    print("Minimum kiadás:", min_expense)
    print("Bevitt kiadások száma:", count)
    print("Átlag feletti kiadások száma:", above_avg_count)
    print(f"Mean: {mean:.3f}")
    print(f"Median: {median:.3f}")

    if total > 10000:
        print("Túl sokat költöttél ma!")


if __name__ == "__main__":
        main()
