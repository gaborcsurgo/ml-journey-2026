"""Model validation of the expense dataset"""

import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. CSV betöltés
df = pd.read_csv("expenses/expenses.csv")

# 2. Target létrehozás
df["high_expense"] = (df["amount"] >= 6000).astype(int)

# 3. Feature engineering
df["category_avg"] = df.groupby("category")["amount"].transform("mean")
df["category_count"] = df.groupby("category")["amount"].transform("count")

df["is_essential"] = df["category"].isin(
    ["food", "rent", "utils", "toiletery", "transport", "adhoc"]
).astype(int)

# 4. Input
X = pd.concat(
    [
        pd.get_dummies(df["category"]),
        df[["category_avg", "category_count", "is_essential"]],
    ],
    axis=1
)

# 5. Target
y = df["high_expense"]

# 6. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42, stratify=y
)

# 7. Modell
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 8. Tanítás
model.fit(X_train, y_train)

# 9. Predikció
predictions = model.predict(X_test)

# 10. Mérőszámok
acc = accuracy_score(y_test, predictions)

# 11. Cross validation
scores = cross_val_score(model, X, y, cv = 5, scoring="f1")

# 12. Output
print("Valódi értékek:")
print(y_test.to_string(index=False))

print("\nPredikciók:")
print(predictions.tolist())

print("\nAccuracy:", round(acc, 3))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("Cross validation:", scores)
print("Mean:", scores.mean())
print("Std:" ,scores.std())


# Logistic regression
lr_model = LogisticRegression(max_iter=1000)

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

lr_acc = accuracy_score(y_test, lr_predictions)

lr_scores = cross_val_score(lr_model, X, y, cv=5, scoring="f1")

print("\n===== LOGISTIC REGRESSION =====")

print("Valódi értékek:")
print(y_test.to_string(index=False))

print("\nPredikciók:")
print(lr_predictions.tolist())

print("\nAccuracy:", round(lr_acc, 3))

print("\nClassification Report:")
print(classification_report(y_test, lr_predictions))

print("Cross validation F1:", lr_scores)
print("Mean:", round(lr_scores.mean(), 3))
print("Std:", round(lr_scores.std(), 3))
