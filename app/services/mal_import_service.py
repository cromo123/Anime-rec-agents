"""Fake MyAnimeList import service.

This module uses deterministic sample data for the first project milestone.
Later, this service can be replaced with an official MyAnimeList API client
that handles OAuth, pagination, and real user anime history.
"""

from app.schemas import AnimeListEntry


def get_fake_user_anime_list(user_id: str) -> list[AnimeListEntry]:
    """Return a fake anime list for a user.

    The user_id is accepted now so the function already looks like a real
    import service. In this milestone, it returns the same fake data for every
    user.
    """
    return [
        AnimeListEntry(
            mal_id=9253,
            title="Steins;Gate",
            status="completed",
            score=10,
            watched_episodes=24,
            total_episodes=24,
            genres=["sci-fi", "thriller"],
        ),
        AnimeListEntry(
            mal_id=19,
            title="Monster",
            status="completed",
            score=10,
            watched_episodes=74,
            total_episodes=74,
            genres=["psychological", "thriller"],
        ),
        AnimeListEntry(
            mal_id=9756,
            title="Puella Magi Madoka Magica",
            status="completed",
            score=9,
            watched_episodes=12,
            total_episodes=12,
            genres=["psychological", "fantasy"],
        ),
        AnimeListEntry(
            mal_id=100001,
            title="Generic Isekai Adventure",
            status="dropped",
            score=4,
            watched_episodes=3,
            total_episodes=12,
            genres=["isekai", "fantasy", "action"],
        ),
        AnimeListEntry(
            mal_id=1,
            title="Cowboy Bebop",
            status="completed",
            score=8,
            watched_episodes=26,
            total_episodes=26,
            genres=["sci-fi", "action"],
        ),
    ]
