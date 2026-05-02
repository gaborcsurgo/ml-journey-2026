"""Feature importance with random forest"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


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

# 6. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42,
    stratify=y
)

# 7. Modell
model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

# 8. Modellek futtatása
model.fit(X_train, y_train)

# 9. Feature importance
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

# 10. Sorbarendezés
importance = importance.sort_values(ascending=False)

# 11. Kiírás
print("Feature Importance:\n")
print(importance)

# 12. Plot
plt.figure(figsize=(10, 6))

importance.plot(kind="bar")

plt.title("Feature Importance")

plt.xlabel("Features")
plt.ylabel("Importance Score")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
