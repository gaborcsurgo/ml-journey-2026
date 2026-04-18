"""This code trains a simple linear regression model on a small dataset. 
Then tests the model's performance and makes predictions.
"""


import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Adatok
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

y = np.array([1000, 1200, 1400, 1600, 1800, 2100, 2300, 2500, 2700, 3000])

# 2. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)

# 3. Modell
model = LinearRegression()

# 4. Tanítás
model.fit(X_train, y_train)

# 5. Jóslás teszt adatokra
predictions = model.predict(X_test)

# 6. Hibák mérése
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# 7. Kiírás
print("Valódi értékek:", y_test)
print("Predikciók:", predictions)

print("\nMAE:", round(mae, 2))
print("R2 Score:", round(r2, 3))

# 8. Új predikció
future = model.predict([[12]])
print("\n12. nap becsült kiadás:", round(future[0], 2))