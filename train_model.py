import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

df = pd.read_csv("data/loan_approval_dataset.csv")
df.columns = df.columns.str.strip()
df['loan_status'] = df['loan_status'].str.strip()
df['education'] = df['education'].str.strip()
df['self_employed'] = df['self_employed'].str.strip()
df.drop(columns=['loan_id'], inplace=True)

# Słowniki z mapowaniem
status_map = {"Approved": 1, "Rejected": 0}
edu_map = {"Graduate": 1, "Not Graduate": 0}
emp_map = {"Yes": 1, "No": 0}

# Zastosowanie mapowania na kolumnach
df['loan_status'] = df['loan_status'].replace(status_map)
df['education'] = df['education'].replace(edu_map)
df['self_employed'] = df['self_employed'].replace(emp_map)

df['education'] = df['education'].astype(int)
df['self_employed'] = df['self_employed'].astype(int)
df['loan_status'] = df['loan_status'].astype(int)

df = df[df['residential_assets_value'] >= 0]

financial_columns = [
    'income_annum',
    'loan_amount',
    'residential_assets_value',
    'commercial_assets_value',
    'luxury_assets_value',
    'bank_asset_value'
]

exchange_rate = 83

for col in financial_columns:
    df[col] = round(df[col] / exchange_rate, 2)

X = df.drop(columns = ['loan_status'])
y = df['loan_status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train,y_train)
y_pred = rf_model.predict(X_test)

print("Dokładność (Accuracy):", accuracy_score(y_test, y_pred))
print("\nRaport klasyfikacji:\n", classification_report(y_test, y_pred))

joblib.dump(rf_model, 'loan_approval_model.pkl')