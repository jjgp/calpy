# calpy

A calculator in Python

## Getting started

Install the dependencies and the entry script:

```
pip install \
  -r requirements.txt \
  -r requirements-extra.txt \
  -e .
```

For development standards make sure to install [pre-commit](https://github.com/pre-commit/pre-commit):

```
pre-commit install --install-hooks
```

To run the tests:

```
python -m pytest
```

If using an environment that supports [devcontainers](https://github.com/microsoft/vscode-dev-containers)
there is a configuration in the [.devcontainer](.devcontainer/devcontainer.json) directory.

## Usage

For Reverse Polish notation:

```
calpy --postfix "21 21 +"
```

For infix notation:

```
calpy --infix "21 + 21"
```
