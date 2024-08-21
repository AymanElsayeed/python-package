# Developing Python Packages

## Project Description

this project is a template or a guide to help you develop your own python package.


## Project Structure
    .
    ├── python-package
    │   ├── python_package
    │   │   ├── __init__.py
    │   │   ├── sub_package
    │   │   │   ├── __init__.py
    │   │   │   └── module.py
    │   |── setup.py
    │   └── README.md


## Installation

```bash

pip install -e .

```

## How to build distribution package

```bash
python setup.py sdist bdist_wheel
```
sdidt: source distribution

bdist_wheel: wheel distribution

## Upload package to PyPi

```bash
twine upload dist/*
```

## Upload package to TestPyPi

```bash
twine upload -r testpypi dist/*
```