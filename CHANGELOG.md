# Changelog

All notable changes to this project will be documented in this file.

## [2.5.1] - 2024-10-23

### Changed

- chore: update README, licensefile, and repository metadata
- chore(deps): remove unused dependencies

## [2.5.0] - 2024-04-24

### Added

- feat: add support for OIDC token validation to authenticateJWT method

## [2.4.0] - 2024-03-21

### Added

- `GetUserByIdentifier` method has been added
- `ListPaginatedUsersItem` model has been added

## [2.3.2] - 2024-02-05

### Fixed

- Fixed another issue with the package names generating incorrect names

## [2.3.1] - 2024-02-05

### Fixed

- Fixed an error where the package `openapi_client` could not be found

## [2.3.0] - 2024-01-30

### Added

- `AppleUserSocialConnection` model has been added

### Changed

- `UserEventInfo` has been renamed to `UserRecentEvent`
- `GithubSocialConnection` has been renamed to `GithubUserSocialConnection`
- `GoogleSocialConnection` has been renamed to `GoogleUserSocialConnection`
