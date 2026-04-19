"""This code trains a simple linear regression model on dataset from a CSV file.
Then tests the model's performance and makes predictions.
"""


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("expenses/expenses.csv")
X = pd.get_dummies(df["category"])
y = df["amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
predictions = model.predict(X_test)
rounded_predictions = [float(round(p, 2)) for p in predictions]

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Valódi értékek:")
print(y_test.to_string(index=False))

print("\nPontosság (R2 Score):", round(score, 3))

print("Predikciók:", rounded_predictions)

print("\nMAE:", round(mae, 2))
print("R2 Score:", round(r2, 3))
