"""Random Forest model for the preediction of expenses based on category."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. CSV betöltés
df = pd.read_csv("expenses/expenses.csv")

# 2. Feature / target
X = pd.get_dummies(df["category"])
y = df["amount"]

# 3. Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Modell létrehozása
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# 5. Tanítás
model.fit(X_train, y_train)

# 6. Predikció
predictions = model.predict(X_test)

# 7. Mérőszámok
score = model.score(X_test, y_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# 8. Kiírás
print("Valódi értékek:")
print(y_test.to_string(index=False))

print("\nPredikciók:")
print(predictions.round(2).tolist())

print("\nR2 Score:", round(score, 3))
print("MAE:", round(mae, 2))

# 9. Feature importance
importance = pd.Series(model.feature_importances_, index=X.columns)
print("\nFeature importance:")
print(importance.sort_values(ascending=False))