"""Probability and ROC curve"""

import pandas as pd

from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve

import matplotlib.pyplot as plt

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

# 12. Probability prediction
probs = grid.predict_proba(X_test)

# 13. ROC curve
fpr, tpr, thresholds = roc_curve(y_test, probs[:, 1])

# 14. AUC score
auc = roc_auc_score(y_test, probs[:, 1])

# 15. Score
acc = accuracy_score(y_test, predictions)

# 16. Output
print("Valódi értékek:")
print(y_test.to_string(index=False))

print("\nPredikciók:")
print(predictions.tolist())

print("\nProbability-k:")
print(probs[:, 1].round(3))

print("\nAccuracy:", round(acc, 3))

print("\nAUC Score:", round(auc, 3))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("Legjobb paraméterek:", grid.best_params_)
print("Legjobb érték:", round(grid.best_score_, 3))

# 17. ROC plot
plt.figure(figsize=(6, 6))

plt.plot(fpr, tpr, label=f"AUC = {auc:.3f}")

plt.plot([0, 1], [0, 1], linestyle="--")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.grid()

plt.show()
