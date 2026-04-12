#!/usr/bin/env python3
"""Modify expenses to include categories.

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
        amount_input = input("Kiadás összege (ha végeztél, írd be, hogy stop): ")
    
        if amount_input.lower() == "stop":
            break

        try:
            value = int(amount_input)
        except ValueError:
            print("Érvénytelen összeg, próbáld újra.")
            continue

        category_input = input("Kiadás kategóriája: ").strip()

        expenses.append({
            "amount": value,
            "category": category_input
        })

    # print ("Bevitt kiadások és kategóriák:", expenses)
    return expenses


def calculate_total(expenses):

    total = sum(e["amount"] for e in expenses)

    # print("Kiadások összege:", total)
    return total


def calculate_avg(expenses):

    total = calculate_total(expenses)
    avg = total / len(expenses)

    # print("Kiadások átlaga:", avg)
    return avg


def calculate_max_min(expenses):

    max_expense = max(e["amount"] for e in expenses)
    min_expense = min(e["amount"] for e in expenses)

    # print("Max and min:", max_expense, min_expense)
    return max_expense, min_expense
    

def calculate_counts(expenses, avg):

    count = len(expenses)
    above_avg_count = sum(1 for e in expenses if e["amount"] > avg)

    # print("Count and above avg count:", count, above_avg_count)
    return count, above_avg_count


def calculate_mean_median(expenses):

    amounts = [e["amount"] for e in expenses]
    mean = sum(amounts) / len(amounts)

    sorted_amounts = sorted(amounts)
    n = len(sorted_amounts)

    if n % 2 == 1:
        median = sorted_amounts[n // 2]
    else:
        median = (sorted_amounts[n // 2 - 1] + sorted_amounts[n // 2]) / 2

    # print("Mean and median:", mean, median)
    return mean, median


def calculate_by_category(expenses):
    
    results = {}

    for e in expenses:
        category = e["category"]
        amount = e["amount"]

        if category not in results:
            results[category] = 0

        results[category] += amount

    max_category = max(results, key=results.get)
    
    # print("Amounts by category:", results)
    return results, max_category


def main():

    exp = get_expenses()

    if not exp:
        print("Nem adtál meg egyetlen kiadást sem. Indítsd újra a programot és adj meg legalább egy kiadást.")
        return
    
    total = calculate_total(exp)
    avg = calculate_avg(exp)
    max_expense, min_expense = calculate_max_min(exp)
    count, above_avg_count = calculate_counts(exp, avg)
    mean, median = calculate_mean_median(exp)
    amount_by_category, max_category = calculate_by_category(exp)

    print("\nÖsszesen:", total)
    print(f"Átlag: {avg:.3f}")
    print("Maximum kiadás:", max_expense)
    print("Minimum kiadás:", min_expense)
    print("Bevitt kiadások száma:", count)
    print("Átlag feletti kiadások száma:", above_avg_count)
    print(f"Mean: {mean:.3f}")
    print(f"Median: {median:.3f}")
    print("\nKiadások kategóriánként:")
    for cat, cat_total in amount_by_category.items():
        print(f"{cat}: {cat_total}")
    print(f"\nLegnagyobb kiadás kategóriája: {max_category}: {amount_by_category[max_category]}")

    if total > 10000:
        print("\nTúl sokat költöttél ma!")


if __name__ == "__main__":
        main()
