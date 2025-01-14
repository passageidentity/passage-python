"""Setup configuration for the Passage Identity Python package."""

from pathlib import Path

import setuptools

with Path("README.md").open(encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="passage-identity",
    version="3.0.0",
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
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
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
        "cryptography ~= 44.0",  # used by pyjwt
        "pydantic ~= 2.10",  # used by codgen
        "pyjwt ~= 2.9",
        "python-dateutil ~= 2.9",  # used by codegen
        "requests ~= 2.32",
    ],
    extras_require={
        "dev": [
            "pytest ~= 8.3",
            "python-dotenv ~= 1.0",
            "faker ~= 33.1",
            "build ~= 1.2",
            "ruff ~= 0.8",
        ],
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
    python_requires=">=3.8",
)
