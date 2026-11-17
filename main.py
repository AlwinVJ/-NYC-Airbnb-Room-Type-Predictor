import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel, Field
import joblib


app = FastAPI(title="NYC Airbnb Room Type Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "Model_Pipeline.pkl"

COLUMNS = [
    "latitude", "longitude", "price", "minimum_nights",
    "number_of_reviews", "reviews_per_month",
    "calculated_host_listings_count", "availability_365",
    "neighbourhood_group", "neighbourhood",
]

model = joblib.load(MODEL_PATH)  # Load the pre-trained model pipeline

# Pydantic Model for input validation
class Features(BaseModel):
    latitude: float = Field(..., ge=-90, le=90, description="Latitude coordinate")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude coordinate")
    price: float = Field(..., gt=0, description="Price per night, must be positive")
    minimum_nights: int = Field(..., ge=1, le=365, description="Minimum nights required for booking")
    number_of_reviews: int = Field(..., ge=0, description="Total number of reviews")
    reviews_per_month: float = Field(..., ge=0, description="Average reviews per month")
    calculated_host_listings_count: int = Field(..., ge=0, description="Number of listings by this host")
    availability_365: int = Field(..., ge=0, le=365, description="Days available out of 365")
    neighbourhood_group: str = Field(..., min_length=1, description="Borough or neighbourhood group")
    neighbourhood: str = Field(..., min_length=1, description="Specific neighbourhood name")


@app.get("/")
def root():
    index_file = BASE_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return {"status": "ok", "message": "NYC Airbnb Room Type Prediction API"}


@app.get("/style.css")
def get_style():
    style_file = BASE_DIR / "style.css"
    if style_file.exists():
        return FileResponse(style_file, media_type="text/css")
    return {"error": "Not found"}


@app.get("/script.js")
def get_script():
    script_file = BASE_DIR / "script.js"
    if script_file.exists():
        return FileResponse(script_file, media_type="application/javascript")
    return {"error": "Not found"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/api")
def api_info():
    return {"status": "ok", "message": "NYC Airbnb Room Type Prediction API"}


@app.post("/predict")
def predict(features: Features):
    feature_data = features.model_dump() if hasattr(features, "model_dump") else features.dict()
    row = pd.DataFrame([feature_data], columns=COLUMNS)
    prediction = model.predict(row)
    probability = model.predict_proba(row)

    return {
        "Predicted_room_type": prediction[0],
        "Probability": probability.tolist()[0]
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
