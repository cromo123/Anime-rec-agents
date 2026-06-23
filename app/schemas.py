"""Pydantic models used by the API and services."""

from pydantic import BaseModel, Field


class AnimeListEntry(BaseModel):
    mal_id: int
    title: str
    status: str
    score: int | None = None
    watched_episodes: int | None = None
    total_episodes: int | None = None
    genres: list[str] = Field(default_factory=list)


class UserTasteProfile(BaseModel):
    user_id: str
    favorite_genres: list[str]
    disliked_genres: list[str]
    high_score_anime: list[str]
    low_score_anime: list[str]
    taste_summary: str


class RecommendationRequest(BaseModel):
    user_id: str
    message: str
    mood: str | None = None
    available_time: str | None = None
    disliked_genres: list[str] = Field(default_factory=list)
    preferred_genres: list[str] = Field(default_factory=list)


class WatchPlan(BaseModel):
    episodes_per_week: int
    estimated_weeks: int


class RecommendationResponse(BaseModel):
    recommended_anime: str
    confidence: float
    reason: str
    watch_plan: WatchPlan
    agents_used: list[str]
