import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="passage-identity",
    version="1.1.3",
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
    #package_dir={"": "passage"},
    packages=["passageidentity"],
    install_requires=['pyjwt','cryptography','requests', 'Flask'],
    setup_requires=['pytest-runner', 'wheel'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    python_requires=">=3.6",
)
