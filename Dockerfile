# 1. Używamy oficjalnego, lekkiego obrazu Pythona
FROM python:3.10-slim

# 2. Ustawiamy katalog roboczy wewnątrz kontenera
WORKDIR /app

# 3. Kopiujemy pliki z wymaganiami i instalujemy biblioteki
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopiujemy kod naszej aplikacji i wytrenowany model
COPY main.py .
COPY loan_approval_model.pkl .

# 5. Informujemy, że aplikacja będzie działać na porcie 8000
EXPOSE 8000

# 6. Komenda uruchamiająca serwer FastAPI (przyjmuje ruch z zewnątrz)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]