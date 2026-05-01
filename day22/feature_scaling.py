"""Compare multiple ML classifiers on the expense dataset"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

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

# 7. Modellek
models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "KNN": Pipeline([
        ("scaler", StandardScaler()),
        ("model", KNeighborsClassifier(n_neighbors=3))
    ])
}

# 8. Modellek futtatása
for name, model in models.items():

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    # tanítás
    model.fit(X_train, y_train)

    # predikció
    predictions = model.predict(X_test)

    # score
    acc = accuracy_score(y_test, predictions)

    # output
    print("\nPredictions:")
    print(predictions.tolist())

    print("\nAccuracy:", round(acc, 3))

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))
