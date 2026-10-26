
from pathlib import Path
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Iris Model API", version="1.0.0")

# Load the trained model
BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / "models" / "iris_model.joblib"
model = joblib.load(model_path)


# Input data validation
class IrisRequest(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)


# Home endpoint
@app.get("/")
def home():
    return {"message": "API is ready to serve predictions."}


# Health-check endpoint
@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": True}


# Prediction endpoint
@app.post("/predict")
def predict(data: IrisRequest):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction = model.predict(features)

    return {"prediction": int(prediction[0])}
