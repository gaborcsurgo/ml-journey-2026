"""Feature engineering and model training for expense prediction based on category."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. CSV betöltés
df = pd.read_csv("expenses/expenses.csv")

# 2. Feature engineering

# kategória átlagos költése
df["category_avg"] = df.groupby("category")["amount"].transform("mean")

# kategória darabszám
df["category_count"] = df.groupby("category")["amount"].transform("count")

# essential flag
df["is_essential"] = df["category"].isin(
    ["food", "rent", "utils", "toiletery", "transport", "adhoc"]
).astype(int)

# fun flag
df["is_fun"] = df["category"].isin(
    ["beer", "hobbies", "presents"]
).astype(int)

# one-hot category
category_dummies = pd.get_dummies(df["category"])

# X összerakása
X = pd.concat(
    [
        category_dummies,
        df[["category_avg", "category_count", "is_essential", "is_fun"]],
    ],
    axis=1
)

# target
y = df["amount"]

# 3. split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. model
model = RandomForestRegressor(
    n_estimators=150,
    random_state=42
)

# 5. train
model.fit(X_train, y_train)

# 6. predict
predictions = model.predict(X_test)

# 7. metrics
score = model.score(X_test, y_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# 8. output
print("R2 Score:", round(score, 3))
print("MAE:", round(mae, 2))

print("\nPredictions:")
print(predictions.round(2).tolist())

print(df.head(15))

# 9. feature importance
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nFeature Importance:")
print(importance)