"""FastAPI entry point for anime-recommendation-agents."""

from fastapi import FastAPI

from app.schemas import RecommendationRequest, RecommendationResponse
from app.services.recommendation_service import generate_recommendation

app = FastAPI(title="anime-recommendation-agents")


@app.get("/health")
def health() -> dict[str, str]:
    """Return a simple health check response."""
    return {"status": "ok"}


@app.post("/recommend", response_model=RecommendationResponse)
def recommend(request: RecommendationRequest) -> RecommendationResponse:
    """Return one structured fake anime recommendation."""
    return generate_recommendation(request)
