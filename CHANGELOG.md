# Changelog

All notable changes to this project will be documented in this file.

## [3.0.2](https://github.com/passageidentity/passage-python/compare/v3.0.1...v3.0.2) (2026-01-09)


### Documentation

* README for sunset ([#147](https://github.com/passageidentity/passage-python/issues/147)) ([015b5a7](https://github.com/passageidentity/passage-python/commit/015b5a77cdabbb88e3fb0813253d61f86969f421))

## [3.0.1](https://github.com/passageidentity/passage-python/compare/v3.0.0...v3.0.1) (2025-02-12)


### Bug Fixes

* add passage-version header to requests ([#142](https://github.com/passageidentity/passage-python/issues/142)) ([733203a](https://github.com/passageidentity/passage-python/commit/733203aad67ec1028ba2bf3bbcacedcccd015e3f))

## [3.0.0](https://github.com/passageidentity/passage-python/compare/v2.6.0...v3.0.0) (2025-01-14)


### ⚠ BREAKING CHANGES

* change language type to be more strict in magic link options ([#137](https://github.com/passageidentity/passage-python/issues/137))
* remove deprecated PassageError ctor ([#131](https://github.com/passageidentity/passage-python/issues/131))
* remove deprecated AppInfo code from codegen ([#127](https://github.com/passageidentity/passage-python/issues/127))
* update Passage ctor signature to remove deprecated args ([#132](https://github.com/passageidentity/passage-python/issues/132))
* remove deprecated methods and classes ([#126](https://github.com/passageidentity/passage-python/issues/126))
* rename codegen user models ([#125](https://github.com/passageidentity/passage-python/issues/125))

### Features

* change language type to be more strict in magic link options ([#137](https://github.com/passageidentity/passage-python/issues/137)) ([f8dccdd](https://github.com/passageidentity/passage-python/commit/f8dccdd9d6098e0f7938ea907fb2d59ba7e75096))
* export all models from passageidentity ([#133](https://github.com/passageidentity/passage-python/issues/133)) ([872ba81](https://github.com/passageidentity/passage-python/commit/872ba818feb62e5cf7be09052eb0430bf6513b6e))
* make magic link parameter classes kwargs only ([#130](https://github.com/passageidentity/passage-python/issues/130)) ([0f1613e](https://github.com/passageidentity/passage-python/commit/0f1613ea733672e488d242f3f368f07fc174058f))
* remove auth origin comparison from jwt audience validation ([#129](https://github.com/passageidentity/passage-python/issues/129)) ([52b6859](https://github.com/passageidentity/passage-python/commit/52b6859a72e2b1122be6b1b6e7261be9bbdd2639))
* remove deprecated AppInfo code from codegen ([#127](https://github.com/passageidentity/passage-python/issues/127)) ([236c989](https://github.com/passageidentity/passage-python/commit/236c989eab8605537041c48c0b96d493ae3f31f5))
* remove deprecated methods and classes ([#126](https://github.com/passageidentity/passage-python/issues/126)) ([d4a531e](https://github.com/passageidentity/passage-python/commit/d4a531ed6f268b792b8baf3e5e4d0e1a71badb7e))
* remove deprecated PassageError ctor ([#131](https://github.com/passageidentity/passage-python/issues/131)) ([19b09ca](https://github.com/passageidentity/passage-python/commit/19b09cab2dbdcfeb6db385d505738499beff8d8f))
* remove PassageError error message prefixes ([#136](https://github.com/passageidentity/passage-python/issues/136)) ([596f743](https://github.com/passageidentity/passage-python/commit/596f7439f48094a90e47069d1c5d6a33a73fb49b))
* rename codegen user models ([#125](https://github.com/passageidentity/passage-python/issues/125)) ([7af039c](https://github.com/passageidentity/passage-python/commit/7af039c4aa7ecdbd5ff909d678424ce50ab133c1))
* update Passage ctor signature to remove deprecated args ([#132](https://github.com/passageidentity/passage-python/issues/132)) ([ac802ca](https://github.com/passageidentity/passage-python/commit/ac802cabe0595299389e7072a4fead5a473d1ffe))


### Documentation

* remove API Refernce table from the README ([#138](https://github.com/passageidentity/passage-python/issues/138)) ([1972b91](https://github.com/passageidentity/passage-python/commit/1972b91112cc81dade0e6b772e1ebbf2f5302d42))

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
