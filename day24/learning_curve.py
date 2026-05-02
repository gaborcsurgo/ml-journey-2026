"""Learning curve for overfitting visualization"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import learning_curve, train_test_split
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

def plot_learning_curve(model, name, X, y):
    train_sizes, train_scores, test_scores = learning_curve(
        model, X, y, cv=5, n_jobs=-1, 
        train_sizes=np.linspace(0.1, 1.0, 5),
        scoring='accuracy'
    )
    
    train_mean = np.mean(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)

    plt.plot(train_sizes, train_mean, 'o-', label=f"Tanítási hiba ({name})")
    plt.plot(train_sizes, test_mean, 's-', label=f"Validációs hiba ({name})")
    plt.title(f"Learning Curve: {name}")
    plt.xlabel("Tanító adatok mennyisége")
    plt.ylabel("Accuracy")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()


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

    print(f"Tanulási görbe generálása: {name}...")
    plot_learning_curve(model, name, X_train, y_train)
