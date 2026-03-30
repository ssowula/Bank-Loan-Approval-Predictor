from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
app = FastAPI(title="Bank Loan Approval API")

model = joblib.load("loan_approval_model.pkl")

class ClientData(BaseModel):
    no_of_dependents: int
    education: int
    self_employed: int
    income_annum: float
    loan_amount: float
    loan_term: int
    cibil_score: int
    residential_assets_value: float
    commercial_assets_value: float
    luxury_assets_value: float
    bank_asset_value: float


# 4. Endpoint predykcyjny
@app.post("/predict")
def predict_loan_status(client: ClientData):
    input_data = pd.DataFrame([client.model_dump()])

    prediction = model.predict(input_data)

    result = "Approved" if prediction == 1 else "Rejected"

    return {"prediction": result, "status_code": 200}