#!/usr/bin/env bash

python -m pip install --upgrade pip

pip install \
  -r requirements.txt \
  -r requirements-extra.txt \
  -e .

pre-commit install --install-hooks
