"""This code creates a simple linear regression model that predicts expenses based on a given day.
The model is provided with training data containing days and their corresponding expenses.
After training the model, it predicts the expenses for day 6 and displays the daily growth and the starting value.
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Tanító adatok (napok)
X = np.array([[1], [2], [3], [4], [5]])

# 2. Célértékek (kiadások)
#y = np.array([1000, 1200, 1400, 1600, 1800])
y = np.array([1500, 2200, 1800, 2500, 3000])

# 3. Modell létrehozása
model = LinearRegression()

# 4. Modell tanítása
model.fit(X, y)

# 5. Jóslás a 6. napra
prediction = model.predict([[6]])

# 6. Eredmény kiírása
print("6. nap becsült kiadás:", prediction[0])

# 7. Meredekség (napi növekedés)
print("Napi növekedés:", model.coef_[0])

# 8. Kezdőérték
print("Kezdő érték:", model.intercept_)