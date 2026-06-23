"""Build a simple user taste profile from anime list entries."""

from collections import Counter

from app.schemas import AnimeListEntry, UserTasteProfile


def build_user_taste_profile(
    user_id: str,
    anime_list: list[AnimeListEntry],
) -> UserTasteProfile:
    """Create a deterministic taste profile from fake MyAnimeList history."""
    high_score_entries = [
        anime for anime in anime_list if anime.score is not None and anime.score >= 8
    ]
    low_score_entries = [
        anime for anime in anime_list if anime.score is not None and anime.score <= 5
    ]

    high_score_anime = [anime.title for anime in high_score_entries]
    low_score_anime = [anime.title for anime in low_score_entries]
    favorite_genres = _most_common_genres(high_score_entries)
    disliked_genres = _most_common_genres(low_score_entries)

    taste_summary = (
        f"User {user_id} tends to enjoy {', '.join(favorite_genres) or 'unknown genres'} "
        f"and seems less interested in {', '.join(disliked_genres) or 'unknown genres'}."
    )

    return UserTasteProfile(
        user_id=user_id,
        favorite_genres=favorite_genres,
        disliked_genres=disliked_genres,
        high_score_anime=high_score_anime,
        low_score_anime=low_score_anime,
        taste_summary=taste_summary,
    )


def _most_common_genres(anime_entries: list[AnimeListEntry]) -> list[str]:
    genre_counter: Counter[str] = Counter()

    for anime in anime_entries:
        genre_counter.update(anime.genres)

    return [genre for genre, count in genre_counter.most_common()]
