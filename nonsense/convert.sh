#! /bin/bash

# Read in the pyproject.toml file and make needed jq transformations
yq '
  (.tool.poetry.requires-python = .tool.poetry.dependencies.python) |
  del(.tool.poetry.dependencies.python) |
  .tool.poetry.dependencies = [.tool.poetry.dependencies | to_entries[] | {"dep": .key, "version": .value}] |
  .tool.poetry.dev-dependencies = [.tool.poetry.dev-dependencies | to_entries[] | {"dep": .key, "version": .value}] |
  .project.urls = [.project.urls | to_entries[] | {"name": .key, "url": .value}]
  ' pyproject.toml -ojson > poetry.json