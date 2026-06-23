from app.services.mal_import_service import get_fake_user_anime_list
from app.services.profile_service import build_user_taste_profile


def test_profile_builder_identifies_high_score_anime() -> None:
    anime_list = get_fake_user_anime_list("beginner-user")
    profile = build_user_taste_profile("beginner-user", anime_list)

    assert "Steins;Gate" in profile.high_score_anime
    assert "Monster" in profile.high_score_anime


def test_profile_builder_identifies_low_score_anime() -> None:
    anime_list = get_fake_user_anime_list("beginner-user")
    profile = build_user_taste_profile("beginner-user", anime_list)

    assert "Generic Isekai Adventure" in profile.low_score_anime


def test_profile_builder_produces_favorite_genres() -> None:
    anime_list = get_fake_user_anime_list("beginner-user")
    profile = build_user_taste_profile("beginner-user", anime_list)

    assert len(profile.favorite_genres) > 0
    assert "sci-fi" in profile.favorite_genres
