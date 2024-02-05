import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="passage-identity",
    version="2.3.1",
    author="Passage Identity, Inc",
    author_email="support@passage.id",
    description="Python library to help manage your Passage application and users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/passageidentity/passage-python",
    project_urls={
        "Bug Tracker": "https://github.com/passageidentity/passage-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages(where='passageidentity'),
    package_dir = {
        'passageidentity': 'passageidentity',
        'openapi_client': 'passageidentity/openapi_client'
    },
    install_requires=[
        'aenum',
        'cryptography',
        'django < 5', 
        'Flask', 
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
