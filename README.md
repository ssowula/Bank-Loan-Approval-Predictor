# 🏦 Loan Approval Prediction - End-to-End ML Project

## 📌 Opis Projektu
Projekt ten to kompletny rurociąg uczenia maszynowego (End-to-End Machine Learning Pipeline) służący do przewidywania decyzji o przyznaniu kredytu bankowego. Analizuje on profil klienta (m.in. historię kredytową, zarobki, wykształcenie, posiadany majątek) i na tej podstawie ocenia ryzyko, automatycznie klasyfikując wniosek jako `Approved` lub `Rejected`. 

Projekt obejmuje pełen cykl życia modelu: od Eksploracyjnej Analizy Danych (EDA) i czyszczenia, przez trening algorytmu **Random Forest**, aż po wdrożenie (Deployment) w formie skonteneryzowanego API (Docker + FastAPI/Flask).

## 🛠 Technologie
* **Język:** Python
* **Analiza i obróbka danych:** Pandas
* **Wizualizacja:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (RandomForestClassifier)
* **Deployment:** Docker, FastAPI/Flask

## 📊 Dane i Przetwarzanie (Data Pre-processing)
Zbiór danych składał się pierwotnie z 4269 kompletnych rekordów. W ramach przygotowania danych do modelu wykonano następujące kroki:
1. **Walidacja anomalii:** Zidentyfikowano i usunięto wiersze zawierające błędne wpisy systemowe (np. ujemna wartość majątku mieszkaniowego jako placeholder).
2. **Skalowanie walut:** Ze względu na czytelność biznesową dla międzynarodowego odbiorcy, wartości finansowe zostały przeliczone z rupii indyjskiej na dolary amerykańskie (USD) i zaokrąglone do dwóch miejsc po przecinku.
3. **Podział danych:** Zastosowano podział na zbiór treningowy i testowy w proporcji 80/20 (`random_state=42`), z wyodrębnieniem kolumny `loan_status` jako zmiennej objaśnianej.

## 📈 Eksploracyjna Analiza Danych (EDA) - Kluczowe wnioski
* **Silna korelacja główna:** Historia kredytowa (`cibil_score`) wykazuje najsilniejszą dodatnią korelację (0.77) z ostateczną decyzją kredytową.
* **Współliniowość (Multikolinearność):** Zaobserwowano ogromną korelację (rzędu >0.90) między atrybutami majątkowymi (zarobki, wartość dóbr luksusowych, kwota kredytu). Algorytm *Random Forest* został wybrany celowo, ponieważ jest w naturalny sposób odporny na to zjawisko statystyczne.
* **Cechy demograficzne:** Samozatrudnienie czy poziom wykształcenia mają marginalny (bliski zeru) wpływ liniowy na decyzję banku.

## 🤖 Budowa Modelu i Skuteczność (Performance)
Zastosowany model **Random Forest Classifier** osiągnął fenomenalne wyniki na zbiorze testowym:
* **Dokładność (Accuracy):** ~98%
* **Precyzja (Precision):** 99% dla przyznanych kredytów, 97% dla odrzuconych.
* **Czułość (Recall):** 99% dla odrzucanych wniosków, co oznacza znakomite minimalizowanie ryzyka banku.
* **F1-Score:** 0.98/0.99, co świadczy o idealnym zbalansowaniu modelu.

### Ważność Cech (Feature Importance)
Analiza sposobu podejmowania decyzji przez algorytm ostatecznie potwierdziła wnioski z EDA:
1. **Historia kredytowa (`cibil_score`):** ~80% wpływu na decyzję.
2. **Termin spłaty (`loan_term`):** ~10% wpływu.
3. Reszta parametrów (w tym wykształcenie i wielkość rodziny) miała znaczenie marginalne.

## 🚀 Jak uruchomić projekt lokalnie?

Dzięki konteneryzacji projekt można uruchomić jedną komendą, bez konieczności ręcznego konfigurowania środowiska.

1. Sklonuj to repozytorium:
   ```bash
   git clone https://github.com/TwojLogin/loan-approval-prediction.git
Przejdź do folderu z projektem:
Uruchom projekt za pomocą Dockera:
API będzie dostępne pod adresem: http://localhost:8000 (lub innym zdefiniowanym porcie). Możesz wysyłać zapytania POST z danymi klienta w formacie JSON, aby w czasie rzeczywistym otrzymać decyzję kredytową.
***