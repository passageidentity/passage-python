import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="passage-identity",
    version="2.5.1",
    author="Passage by 1Password",
    author_email="support@passage.id",
    description="Passkey Complete for Python - Integrate into your Python API or service to enable a completely passwordless standalone auth solution with Passage by 1Password",
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
    packages = [
        'passageidentity', 
        'passageidentity.models', 
        'passageidentity.openapi_client', 
        'passageidentity.openapi_client.api', 
        'passageidentity.openapi_client.models'
    ],
    package_dir = {
        'passageidentity': 'passageidentity',
        'passageidentity.models': 'passageidentity/models',
        'passageidentity.openapi_client': 'passageidentity/openapi_client',
        'passageidentity.openapi_client.api': 'passageidentity/openapi_client/api',
        'passageidentity.openapi_client.models': 'passageidentity/openapi_client/models',
    },
    install_requires=[
        'aenum',
        'cryptography',
        'importlib-metadata >= 1.0 ; python_version < "3.12"',
        'pydantic',
        'pyjwt',
        "python-dateutil",
        'requests', 
        "typing_extensions >= 4.7.1",
        "urllib3 >= 1.25.3, < 2.1.0",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.3'],
    test_suite='tests',
    python_requires=">=3.7",
)
