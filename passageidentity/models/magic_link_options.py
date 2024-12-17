"""Defines options for creating a Magic Link."""

from __future__ import annotations


class MagicLinkOptions:
    """Options for creating a Magic Link."""

    language: str | None
    magic_link_path: str | None
    redirect_url: str | None
    ttl: int | None

    def __init__(
        self,
        *,
        language: str | None = None,
        magic_link_path: str | None = None,
        redirect_url: str | None = None,
        ttl: int | None = None,
    ) -> None:
        """Initialize the options with the given values."""
        self.language = language
        self.magic_link_path = magic_link_path
        self.redirect_url = redirect_url
        self.ttl = ttl
