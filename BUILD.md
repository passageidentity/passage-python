# Instructions for Building

### Install dependencies

Use a virtual environment and install dependencies

```
> python3 -m venv venv
> source venv/bin/activate
> pip install build

python3 -m venv venv; source venv/bin/activate; pip install build
```

### Build the project

This will create the `/dist` directory
```
python -m build
```

### Run tests

```
pytest
```
