"""Simple deterministic recommendation logic for the first milestone."""

from app.schemas import RecommendationRequest, RecommendationResponse, WatchPlan
from app.services.mal_import_service import get_fake_user_anime_list
from app.services.profile_service import build_user_taste_profile


AGENTS_USED = [
    "ProfileAgent",
    "RecommendationAgent",
    "CriticAgent",
    "ExplanationAgent",
    "ScheduleAgent",
]


def generate_recommendation(
    request: RecommendationRequest,
) -> RecommendationResponse:
    """Generate one fake anime recommendation from request and profile data."""
    anime_list = get_fake_user_anime_list(request.user_id)
    profile = build_user_taste_profile(request.user_id, anime_list)

    recommended_anime = _choose_anime(request, profile.favorite_genres)

    if recommended_anime in profile.high_score_anime:
        recommended_anime = _choose_backup_anime(recommended_anime)

    reason = (
        f"Recommended {recommended_anime} because the fake profile says: "
        f"{profile.taste_summary} The request message was '{request.message}', "
        "so this milestone uses simple deterministic matching instead of real AI."
    )

    return RecommendationResponse(
        recommended_anime=recommended_anime,
        confidence=0.82,
        reason=reason,
        watch_plan=WatchPlan(episodes_per_week=4, estimated_weeks=6),
        agents_used=AGENTS_USED,
    )


def _choose_anime(request: RecommendationRequest, favorite_genres: list[str]) -> str:
    search_text = " ".join(
        [
            request.message,
            request.mood or "",
            " ".join(request.preferred_genres),
            " ".join(favorite_genres),
        ]
    ).lower()

    if any(word in search_text for word in ["psychological", "sci-fi", "thriller"]):
        return "Psycho-Pass"

    if "action" in search_text:
        return "Fullmetal Alchemist: Brotherhood"

    return "Cowboy Bebop"


def _choose_backup_anime(original_choice: str) -> str:
    backup_choices = [
        "Psycho-Pass",
        "Fullmetal Alchemist: Brotherhood",
        "Samurai Champloo",
    ]

    for anime in backup_choices:
        if anime != original_choice:
            return anime

    return "Psycho-Pass"
