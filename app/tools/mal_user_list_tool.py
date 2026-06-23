"""Future CrewAI tool for importing a user's MyAnimeList anime list.

This is currently fake and deterministic. Later, this tool should use the
official MyAnimeList OAuth/API flow through a service class.

Agents should use tools like this instead of directly calling external APIs.
That keeps API details, credentials, retries, and test doubles outside of the
agent definitions.
"""

from app.schemas import AnimeListEntry
from app.services.mal_import_service import get_fake_user_anime_list


class MyAnimeListUserListTool:
    """Placeholder tool for retrieving a user's anime history."""

    name = "my_anime_list_user_list_tool"
    description = "Fetches a user's anime list. Currently returns fake data."

    def run(self, user_id: str) -> list[AnimeListEntry]:
        """Return fake user anime list entries for now."""
        return get_fake_user_anime_list(user_id)
