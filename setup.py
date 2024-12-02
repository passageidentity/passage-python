"""Setup configuration for the Passage Identity Python package."""

from pathlib import Path

import setuptools

with Path("README.md").open(encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="passage-identity",
    version="2.5.1",
    author="Passage by 1Password",
    author_email="support@passage.id",
    description=(
        "Passkey Complete for Python - Integrate into your Python API or service to enable "
        "a completely passwordless standalone auth solution with Passage by 1Password"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.passage.id/complete",
    project_urls={
        "Bug Tracker": "https://github.com/passageidentity/.github/blob/main/SUPPORT.md",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=[
        "passageidentity",
        "passageidentity.models",
        "passageidentity.openapi_client",
        "passageidentity.openapi_client.api",
        "passageidentity.openapi_client.models",
    ],
    package_dir={
        "passageidentity": "passageidentity",
        "passageidentity.models": "passageidentity/models",
        "passageidentity.openapi_client": "passageidentity/openapi_client",
        "passageidentity.openapi_client.api": "passageidentity/openapi_client/api",
        "passageidentity.openapi_client.models": "passageidentity/openapi_client/models",
    },
    install_requires=[
        "aenum >= 3.1.15",
        "cryptography >= 44.0.0",
        "importlib-metadata >= 8.5.0",
        "pydantic >= 2.10.2",
        "pyjwt >= 2.10.1",
        "python-dateutil >= 2.9.0.post0",
        "requests >= 2.32.3",
        "typing_extensions >= 4.12.2",
        "urllib3 >= 2.2.3",
    ],
    extras_require={
        "dev": [
            "pytest >= 8.3.4",
            "python-dotenv >= 1.0.1",
            "faker >= 33.1.0",
            "build >= 1.2.2.post1",
            "ruff >= 0.8.1",
        ],
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
    python_requires=">=3.7",
)
