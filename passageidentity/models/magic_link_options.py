"""Defines options for creating a Magic Link."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from passageidentity.openapi_client.models.magic_link_language import MagicLinkLanguage


class MagicLinkOptions:
    """Options for creating a Magic Link."""

    language: MagicLinkLanguage | None
    magic_link_path: str | None
    redirect_url: str | None
    ttl: int | None

    def __init__(
        self,
        *,
        language: MagicLinkLanguage | None = None,
        magic_link_path: str | None = None,
        redirect_url: str | None = None,
        ttl: int | None = None,
    ) -> None:
        """Initialize the options with the given values."""
        self.language = language
        self.magic_link_path = magic_link_path
        self.redirect_url = redirect_url
        self.ttl = ttl
