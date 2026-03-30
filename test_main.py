from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_loan_approved():
    payload = {
        "no_of_dependents": 0,
        "education": 0,
        "self_employed": 1,
        "income_annum": 25000.0,
        "loan_amount": 250000.0,
        "loan_term": 20,
        "cibil_score": 800,
        "residential_assets_value": 0.0,
        "commercial_assets_value": 0.0,
        "luxury_assets_value": 0.0,
        "bank_asset_value": 0.0
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    assert response.json()["prediction"] == "Approved"