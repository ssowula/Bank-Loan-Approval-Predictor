# 🏦 Loan Approval Prediction – ML + EDA Project

## 📌 Opis projektu

Projekt przedstawia analizę danych oraz model uczenia maszynowego służący do przewidywania decyzji o przyznaniu kredytu (`Approved` / `Rejected`).

Celem projektu jest zrozumienie, jakie czynniki mają największy wpływ na decyzję kredytową oraz zbudowanie modelu klasyfikacyjnego, który potrafi tę decyzję przewidywać.

Projekt obejmuje:

* eksploracyjną analizę danych (**EDA**)
* przygotowanie i czyszczenie danych
* budowę modelu **Random Forest**
* ocenę jakości modelu
* interpretację wyników

---

## 🛠 Technologie

* **Python**
* **Pandas** – analiza danych
* **Matplotlib / Seaborn** – wizualizacja
* **Scikit-learn** – model ML

---

## 📂 Struktura projektu

```
├── data/
│   └── loan_approval_dataset.csv
├── Analiza.ipynb        # notebook z pełną analizą (EDA + model)
├── index.html         # wersja HTML notebooka
├── model.py             # skrypt treningowy modelu
└── README.md
```

---

## 📊 Eksploracyjna analiza danych (EDA)

Pełna analiza dostępna tutaj:
👉 **[Zobacz analizę (HTML)](analiza.html)**

Najważniejsze wnioski:

* **cibil_score** (historia kredytowa) ma największy wpływ na decyzję (~0.77 korelacji)
* bardzo silna współliniowość między cechami majątkowymi (>0.90)
* cechy demograficzne (wykształcenie, samozatrudnienie) mają marginalny wpływ

---

## ⚙️ Przygotowanie danych

* usunięcie błędnych wartości (ujemny majątek mieszkaniowy)
* mapowanie zmiennych kategorycznych na wartości binarne
* przeliczenie walut (INR → USD)
* podział danych: **80% trening / 20% test**

---

## 🤖 Model

Zastosowany model:

* **Random Forest Classifier**

Dlaczego:

* dobrze radzi sobie ze współliniowością
* nie wymaga skalowania danych
* jest odporny na szum

---

## 📈 Wyniki

* **Accuracy:** ~98%
* **Precision:**

  * Approved: 99%
  * Rejected: 97%
* **Recall:**

  * Rejected: 99% (ważne biznesowo)
* **F1-score:** ~0.98–0.99

Model bardzo dobrze rozróżnia przypadki i minimalizuje ryzyko błędnego przyznania kredytu.

---

## 🔍 Najważniejsze cechy (Feature Importance)

1. **cibil_score** – ~80% wpływu
2. **loan_term** – ~10%
3. reszta cech – marginalna

## 💡 Wnioski biznesowe

* historia kredytowa jest kluczowym czynnikiem decyzji
* majątek i dochody są mniej istotne niż można się spodziewać
* model może skutecznie wspierać decyzje kredytowe banku
