![passage-python](https://storage.googleapis.com/passage-docs/github-md-assets/passage-python.png)

[![PyPI version](https://badge.fury.io/py/passage-identity.svg)](https://badge.fury.io/py/passage-identity) [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#) ![GitHub License](https://img.shields.io/github/license/passageidentity/passage-python)
![Static Badge](https://img.shields.io/badge/Built_by_1Password-grey?logo=1password)

## About

[Passage by 1Password](https://1password.com/product/passage) unlocks the passwordless future with a simpler, more secure passkey authentication experience. Passage handles the complexities of the [WebAuthn API](https://blog.1password.com/what-is-webauthn/), and allows you to implement passkeys with ease.

Use [Passkey Flex](https://docs.passage.id/flex) to add passkeys to an existing authentication experience.

Use [Passkey Complete](https://docs.passage.id/complete) as a standalone passwordless auth solution.

Use [Passkey Ready](https://docs.passage.id/passkey-ready) to determine if your users are ready for passkeys.

### In passage-python

Use passage-python to implement Passkey Complete into your Python backend to authenticate requests and manage users.

| Product                                                                                                                                  | Compatible                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| ![Passkey Flex](https://storage.googleapis.com/passage-docs/github-md-assets/passage-passkey-flex-icon.png) Passkey **Flex**             | ✖️ For Passkey Flex, check out the [Passkey Flex APIs](https://docs.passage.id/flex/apis)                 |
| ![Passkey Complete](https://storage.googleapis.com/passage-docs/github-md-assets/passage-passkey-complete-icon.png) Passkey **Complete** | ✅                                                                                                        |
| ![Passkey Ready](https://storage.googleapis.com/passage-docs/github-md-assets/passage-passkey-ready-icon.png) Passkey **Ready**          | ✖️ For Passkey Ready, check out [Authentikit](https://www.npmjs.com/package/@passageidentity/authentikit) |

## Getting Started

### Check Prerequisites

<p>
 You'll need a free Passage account and a Passkey Complete app set up in <a href="https://console.passage.id/">Passage Console</a> to get started. <br />
 <sub><a href="https://docs.passage.id/home#passage-console">Learn more about Passage Console →</a></sub>
</p>

### Install

Install this package using [pip](https://pypi.org/project/passage-identity/).

```shell
pip install passage-identity
```

### Import

```python
import os
from passageidentity import Passage
```

### Initialize

Passage has three arguments that can be used for initialization: `app_id`, `api_key`, and `auth_strategy`.

- `app_id` is the Passage App ID that specifies which app should be authorized. It has no default value and must to be set upon initialization.
- `api_key` is an API key for the Passage app, which can be generated in the 'App Settings' section of the [Passage Console](https://console.passage.id). It is an optional parameter and not required for authenticating requests. It is required to get or update user information.
- **Deprecated** `auth_strategy` defines where the Passage SDK should look for the authentication token. It is set by default to `Passage.COOKIE_AUTH`, but can be changed to `Passage.HEADER_AUTH`.

```python
PASSAGE_APP_ID = os.environ.get("YOUR_PASSAGE_APP_ID")
PASSAGE_API_KEY = os.environ.get("YOUR_PASSAGE_API_KEY")

psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY)
```

### Go Passwordless

Find all core functions, user management details, and more implementation guidance on our [Passkey Complete Python Documentation](https://docs.passage.id/complete/backend-sdks/python) page.

## Support & Feedback

We are here to help! Find additional docs, the best ways to get in touch with our team, and more within our [support resources](https://github.com/passageidentity/.github/blob/main/SUPPORT.md).

<br />

---

<p align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://storage.googleapis.com/passage-docs/github-md-assets/passage-by-1password-dark.png">
      <source media="(prefers-color-scheme: light)" srcset="https://storage.googleapis.com/passage-docs/github-md-assets/passage-by-1password-light.png">
      <img alt="Passage by 1Password Logo" src="https://storage.googleapis.com/passage-docs/github-md-assets/passage-by-1password-light.png">
    </picture>
</p>

<p align="center">
    <sub>Passage is a product by <a href="https://1password.com/product/passage">1Password</a>, the global leader in access management solutions with nearly 150k business customers.</sub><br />
    <sub>This project is licensed under the MIT license. See the <a href="LICENSE">LICENSE</a> file for more info.</sub>
</p>
