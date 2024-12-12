# Changelog

All notable changes to this project will be documented in this file.

## [2.6.0](https://github.com/passageidentity/passage-python/compare/v2.5.1...v2.6.0) (2024-12-12)


### Features

* add new method signatures ([#105](https://github.com/passageidentity/passage-python/issues/105)) ([9246e3c](https://github.com/passageidentity/passage-python/commit/9246e3c8ec65eaa810cc881fb16ed0c75550fa51))
* add parameter guards to all methods to return early on invalid values ([83cd628](https://github.com/passageidentity/passage-python/commit/83cd6283c6b6df092a40e18818a3076261682ac3))
* **codegen:** create magic link request fields are now optional ([#115](https://github.com/passageidentity/passage-python/issues/115)) ([b1f164b](https://github.com/passageidentity/passage-python/commit/b1f164bf00bbbebdf50dfe6a6e45510098fe4eec))
* guard against empty params in deprecated magic link method ([f168b8c](https://github.com/passageidentity/passage-python/commit/f168b8cd7e80557c304837ce0b65e4c3323445d6))
* updates create_magic_link method to use stronger typed parameters ([83cd628](https://github.com/passageidentity/passage-python/commit/83cd6283c6b6df092a40e18818a3076261682ac3))

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
