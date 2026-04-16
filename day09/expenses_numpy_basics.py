#!/usr/bin/env python3
"""Modify expense tracker to use numpy."""

import numpy as np

arr = np.array([1000, 2000, 3000, 4000, 5000])
print("Array:", arr)
arr_w_inflation = arr * 1.05
print("With inflation:", arr_w_inflation)
print("Sum:", arr_w_inflation.sum())
avg = arr_w_inflation.mean()
print("Avg:", avg)
print("Max:", arr_w_inflation.max())
print("Min:", arr_w_inflation.min())
print("Expenses over average:", arr_w_inflation[arr_w_inflation > avg])


arr2 = np.random.randint(1000, 10000, size=10)
# np.random.seed(42)
print("Random array:", arr2)
print("Sum:", arr2.sum())
print("Mean:", arr2.mean())
print("Median:", np.median(arr2))
print("Standard deviation:", arr2.std())
print("Sorted:", np.sort(arr2))
