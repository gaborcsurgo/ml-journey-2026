#!/usr/bin/env python3
"""Modify expense tracker to use pandas for data handling and analysis.

Only use existing expense file.
"""

import pandas as pd
import matplotlib.pyplot as plt

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

# plot category totals
plt.figure()
category_totals.sort_values().plot(kind="bar")
plt.title("Kiadások kategóriánként")
plt.xlabel("Kategória")
plt.xticks(rotation=0)
plt.ylabel("Összeg")
plt.tight_layout()
plt.savefig("expenses/bar_chart.png")
plt.show()

plt.figure()
category_totals.plot(kind="pie", autopct="%1.1f%%")
plt.title("Kiadások megoszlása kategóriánként")
plt.ylabel("")
plt.savefig("expenses/pie_chart.png")
plt.show()

plt.figure()
df["amount"].plot(kind="hist")
plt.title("Kiadások eloszlása")
plt.xlabel("Összeg")
plt.savefig("expenses/histogram.png")
plt.show()
