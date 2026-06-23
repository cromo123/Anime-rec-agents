from app.schemas import AnimeListEntry
from app.services.mal_import_service import get_fake_user_anime_list


def test_fake_mal_import_returns_anime_entries() -> None:
    anime_list = get_fake_user_anime_list("beginner-user")

    assert len(anime_list) > 0
    assert all(isinstance(anime, AnimeListEntry) for anime in anime_list)
    assert anime_list[0].title == "Steins;Gate"
