"""Provides the User class for interacting with the Passage API."""

from __future__ import annotations

from typing import TYPE_CHECKING

from passageidentity.errors import PassageError
from passageidentity.openapi_client.exceptions import ApiException
from passageidentity.openapi_client.models.model404_error import Model404Error

from .openapi_client.api import (
    TokensApi,
    UserDevicesApi,
    UsersApi,
)

if TYPE_CHECKING:
    from .openapi_client.models import (
        CreateUserArgs,
        PassageUser,
        UpdateUserArgs,
        WebAuthnDevices,
    )


class User:
    """User class for handling operations to get and update user information."""

    def __init__(self, app_id: str, request_headers: dict[str, str]) -> None:
        """Initialize the User class with the app ID and request headers."""
        self.app_id = app_id
        self.request_headers = request_headers
        self.users_api = UsersApi()
        self.user_devices_api = UserDevicesApi()
        self.tokens_api = TokensApi()

    def get(self, user_id: str) -> PassageUser:
        """Get a user's object using their user ID."""
        if not user_id:
            msg = "user_id is required."
            raise ValueError(msg)

        try:
            return self.users_api.get_user(self.app_id, user_id, _headers=self.request_headers).user
        except ApiException as e:
            raise PassageError.from_response_error(e) from e

    def get_by_identifier(self, identifier: str) -> PassageUser:
        """Get a user's object using their user identifier."""
        if not identifier:
            msg = "identifier is required."
            raise ValueError(msg)

        try:
            users = self.users_api.list_paginated_users(
                self.app_id,
                limit=1,
                identifier=identifier.lower(),
                _headers=self.request_headers,
            ).users
        except ApiException as e:
            raise PassageError.from_response_error(e) from e

        if len(users) == 0:
            raise PassageError.from_response_error(
                ApiException(status=404, data=Model404Error(code="user_not_found", error="User not found.")),
            )

        return self.get(users[0].id)

    def activate(self, user_id: str) -> PassageUser:
        """Activate a user using their user ID."""
        if not user_id:
            msg = "user_id is required."
            raise ValueError(msg)

        try:
            return self.users_api.activate_user(self.app_id, user_id, _headers=self.request_headers).user
        except ApiException as e:
            raise PassageError.from_response_error(e) from e

    def deactivate(self, user_id: str) -> PassageUser:
        """Deactivate a user using their user ID."""
        if not user_id:
            msg = "user_id is required."
            raise ValueError(msg)

        try:
            return self.users_api.deactivate_user(self.app_id, user_id, _headers=self.request_headers).user
        except ApiException as e:
            raise PassageError.from_response_error(e) from e

    def update(self, user_id: str, options: UpdateUserArgs) -> PassageUser:
        """Update a user."""
        if not user_id:
            msg = "user_id is required."
            raise ValueError(msg)

        try:
            return self.users_api.update_user(self.app_id, user_id, options, _headers=self.request_headers).user
        except ApiException as e:
            raise PassageError.from_response_error(e) from e

    def create(self, args: CreateUserArgs) -> PassageUser:
        """Create a user."""
        if not args.email and not args.phone:
            msg = "At least one of args.email or args.phone is required."
            raise ValueError(msg)

        try:
            return self.users_api.create_user(self.app_id, args, _headers=self.request_headers).user
        except ApiException as e:
            raise PassageError.from_response_error(e) from e

    def delete(self, user_id: str) -> None:
        """Delete a user using their user ID."""
        if not user_id:
            msg = "user_id is required."
            raise ValueError(msg)

        try:
            self.users_api.delete_user(self.app_id, user_id, _headers=self.request_headers)
        except ApiException as e:
            raise PassageError.from_response_error(e) from e

    def list_devices(self, user_id: str) -> list[WebAuthnDevices]:
        """Get a user's devices using their user ID."""
        if not user_id:
            msg = "user_id is required."
            raise ValueError(msg)

        try:
            return self.user_devices_api.list_user_devices(self.app_id, user_id, _headers=self.request_headers).devices
        except ApiException as e:
            raise PassageError.from_response_error(e) from e

    def revoke_device(self, user_id: str, device_id: str) -> None:
        """Revoke a user's device using their user ID and the device ID."""
        if not user_id:
            msg = "user_id is required."
            raise ValueError(msg)

        if not device_id:
            msg = "device_id is required."
            raise ValueError(msg)

        try:
            self.user_devices_api.delete_user_devices(self.app_id, user_id, device_id, _headers=self.request_headers)
        except ApiException as e:
            raise PassageError.from_response_error(e) from e

    def revoke_refresh_tokens(self, user_id: str) -> None:
        """Revokes all of a user's Refresh Tokens using their User ID."""
        if not user_id:
            msg = "user_id is required."
            raise ValueError(msg)

        try:
            self.tokens_api.revoke_user_refresh_tokens(self.app_id, user_id, _headers=self.request_headers)
        except ApiException as e:
            raise PassageError.from_response_error(e) from e
