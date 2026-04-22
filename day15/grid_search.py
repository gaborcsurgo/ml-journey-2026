"""Grid Search example using Random Forest Regressor on expenses dataset."""

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Adat betöltés
df = pd.read_csv("expenses/expenses.csv")

# 2. Feature engineering
df["category_avg"] = df.groupby("category")["amount"].transform("mean")
df["category_count"] = df.groupby("category")["amount"].transform("count")

df["is_essential"] = df["category"].isin(
    ["food", "rent", "utils", "toiletery", "transport", "adhoc"]
).astype(int)

df["is_fun"] = df["category"].isin(
    ["beer", "hobbies", "presents"]
).astype(int)

# 3. Input / target
X = pd.concat(
    [
        pd.get_dummies(df["category"]),
        df[["category_avg", "category_count", "is_essential", "is_fun"]],
    ],
    axis=1
)

y = df["amount"]

# 4. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 5. Paraméterek
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10, None]
}

# 6. Modell
rf = RandomForestRegressor(random_state=42)

# 7. Grid Search
grid = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=3,
    scoring="r2",
    n_jobs=-1
)

# 8. Tanítás
grid.fit(X_train, y_train)

# 9. Legjobb modell
best_model = grid.best_estimator_

# 10. Predikció
predictions = best_model.predict(X_test)

# 11. Score
score = best_model.score(X_test, y_test)
mae = mean_absolute_error(y_test, predictions)

# 12. Output
print("Legjobb paraméterek:")
print(grid.best_params_)

print("\nR2 Score:", round(score, 3))
print("MAE:", round(mae, 2))

print("\nPredictions:")
print(predictions.round(2).tolist())

print(df.head(15))
