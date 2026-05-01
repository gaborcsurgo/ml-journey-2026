"""Confusion Matrix + Threshold tuning"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
)

# 1. Load CSV
df = pd.read_csv("expenses/expenses.csv")

# 2. Target
df["high_expense"] = (df["amount"] >= 6000).astype(int)

# 3. Feature engineering
df["category_avg"] = df.groupby("category")["amount"].transform("mean")
df["category_count"] = df.groupby("category")["amount"].transform("count")

df["is_essential"] = df["category"].isin(
    ["food", "rent", "utils", "transport"]
).astype(int)

# 4. Features
X = pd.concat(
    [
        pd.get_dummies(df["category"]),
        df[["category_avg", "category_count", "is_essential"]],
    ],
    axis=1,
)

# 5. Target
y = df["high_expense"]

# 6. Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42,
    stratify=y,
)

# 7. Pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

# 8. Train
pipe.fit(X_train, y_train)

# 9. Probabilities
probs = pipe.predict_proba(X_test)

# 10. Custom threshold
predictions = (probs[:, 1] > 0.7).astype(int)

# 11. Accuracy
acc = accuracy_score(y_test, predictions)

# 12. Confusion matrix
cm = confusion_matrix(y_test, predictions)

# 13. Output
print("Predictions:")
print(predictions.tolist())

print("\nAccuracy:", round(acc, 3))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(cm)

# 14. Plot confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot()

plt.title("Confusion Matrix")

plt.show()
