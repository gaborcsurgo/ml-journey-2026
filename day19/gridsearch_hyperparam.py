"""GridSearch + Hyperparameter Tuning"""

import pandas as pd

from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. CSV betöltés
df = pd.read_csv("expenses/expenses.csv")

# 2. Target változó
df["high_expense"] = (df["amount"] >= 6000).astype(int)

# 3. Feature engineering
df["category_avg"] = df.groupby("category")["amount"].transform("mean")
df["category_count"] = df.groupby("category")["amount"].transform("count")

df["is_essential"] = df["category"].isin(
    ["food", "rent", "utils", "toiletery", "transport", "adhoc"]
).astype(int)

# 4. Input features
X = pd.concat(
    [
        pd.get_dummies(df["category"]),
        df[["category_avg", "category_count", "is_essential"]],
    ],
    axis=1
)

# 5. Target
y = df["high_expense"]

# 6. Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42,
    stratify=y
)

# 7. Pipeline létrehozása
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

# 8. Param Grid
param_grid = {
    "model__C": [0.1, 1, 10],
    "model__solver": ["lbfgs", "liblinear"]
}

# 9. GridSearch
grid = GridSearchCV(
    pipe,
    param_grid,
    cv=5,
    scoring="accuracy"
)

# 10. Tanítás
grid.fit(X_train, y_train)

# 11. Predikció
predictions = grid.predict(X_test)

# 12. Score
acc = accuracy_score(y_test, predictions)

# 13. Output
print("Valódi értékek:")
print(y_test.to_string(index=False))

print("\nPredikciók:")
print(predictions.tolist())

print("\nAccuracy:", round(acc, 3))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("Legjobb paraméterek:", grid.best_params_)
print("Legjobb érték:", grid.best_score_, 3)
