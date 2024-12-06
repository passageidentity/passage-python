"""Defines options for creating a Magic Link."""

from __future__ import annotations


class MagicLinkOptions:
    """Options for creating a Magic Link."""

    language: str | None
    magic_link_path: str | None
    redirect_url: str | None
    ttl: int | None
