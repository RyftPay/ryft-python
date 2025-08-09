# Development

This document describes the process for setting up and developing the solution locally.

## Getting started

> [!IMPORTANT]
> Make sure you have installed the dependencies before running the unit tests or the linter
You will need a compatible `Python` installation. We recommend the latest version of Python but `>=3.6` is supported

### Setting up a (virtual) environment

For Python development, we recommend to create a virtual environment. Creating a Python virtual environment allows you to manage dependencies separately for different projects, preventing conflicts and maintaining cleaner setups. More info on `venv` [here](https://realpython.com/python-virtual-environments-a-primer/).

To create a virtual environment for Ryft, you can follow these steps:

```bash
# create the environment
python -m venv .ryft-env # this environment name is in .gitignore

# activate the environment
source ./.ryft-env/bin/activate

# python now runs from your venv
which python # make sure it returns the venv path

# install dependencies
pip3 install .
```

### Testing the solution

The solution consists of unit tests. To run the tests, you can use `pytest`

```bash
pytest
```

### Maintaining Coding Guidelines

We follow the PEP 8 Python formatting standard and we enforce linting using the [Black](https://github.com/psf/black) formatter

You can run the lint :

```bash
black --check --verbose .
```

Before raising a PR, please ensure you have formatted all code as follows:

```bash
black .
```
