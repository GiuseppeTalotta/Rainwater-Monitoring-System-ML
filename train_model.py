import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Dataset con esempi estremi aggiunti
dati = pd.DataFrame({
    "ph": [
        6.5, 7.0, 7.5, 8.0, 5.8, 6.2, 7.1, 7.3, 6.0, 6.8, 7.6, 8.1,  # originali
        1.4, 2.5, 3.0, 12.0, 13.5, 9.8, 10.5                         # pH estremi
    ],
    "conducibilita": [
        600, 150, 100, 90, 700, 800, 120, 130, 650, 170, 110, 85,     # originali
        120, 200, 400, 100, 90, 110, 95                              # associati agli estremi
    ],
    "etichetta": [
        0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1,  # etichette originali
        0, 0, 0, 0, 0, 0, 0                # tutti gli estremi → Non Buona
    ]
})

# Separazione input e target
X = dati[["ph", "conducibilita"]]
y = dati["etichetta"]

# Divisione in training e test set (20% per test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Addestramento del modello
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Valutazione
y_pred = model.predict(X_test)
print("📊 Report di classificazione:")
print(classification_report(y_test, y_pred))

# Salvataggio
joblib.dump(model, "model_acqua.pkl")
print("✅ Modello salvato come 'model_acqua.pkl'")
