# Instructions for Deploying

### Install dependencies

Use a virtual environment and install dependencies

```
> python3 -m venv venv
> source venv/bin/activate
> pip install twine build
```

### Build the project

This will create the `/dist` directory
```
python setup.py sdist bdist_wheel
```

### Run tests

```
python setup.py pytest
```

### Publish the package

To publish the package, you need an API key on pypi.org. You can save this API key in a `.pypirc` file 

```
[pypi]
  username = __token__
  password = pypi__abc...
```

```
python3 -m twine upload dist/*
```