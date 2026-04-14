#!/usr/bin/env python3
"""Modify expense tracker to use pandas for data handling and analysis.

Only use existing expense file.
"""

import pandas as pd

# load data from csv
filepath = "expenses/expenses.csv"
df = pd.read_csv(filepath)

# calculate statistics
total = df["amount"].sum()
avg = df["amount"].mean()
max_amount = df["amount"].max()
min_amount = df["amount"].min()
count = len(df)
above_avg = (df["amount"] > avg).sum()
category_totals = df.groupby("category")["amount"].sum()
max_category = category_totals.idxmax()

# print results
print("\nÖsszesen:", total)
print(f"Átlag: {avg:.3f}")
print("Maximum kiadás:", max_amount)
print("Minimum kiadás:", min_amount)
print("Bevitt kiadások száma:", count)
print("Átlag feletti kiadások száma:", above_avg)

print("\nKiadások kategóriánként:")
print(category_totals)

print("\nLegnagyobb kiadás kategóriája:", max_category)
