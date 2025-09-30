# QR Code Generator
Python package to be used for creating QR codes from given data

## Development Setup

### 1. Install [Python](https://www.python.org/) check version by running the command
```sh
python3 --version
```
The version should be compatible with the version listed in [pyproject.toml](pyproject.toml)

### 2. Install [Poetry](https://python-poetry.org/docs/) by following the installation instructions in the documentation. Then check the version by running the command
```sh
poetry --version
```
The version should be compatible with the version listed in [pyproject.toml](pyproject.toml)

### 3. Use git clone to get latest copy of [source code](https://github.com/Phoenix-Programming/QR-Code-Generator)
```sh
git clone https://github.com/Phoenix-Programming/QR-Code-Generator.git
cd QR-Code-Generator
```
### 4. Use poetry to install dependencies 
```sh
poetry install
```
### 5. Happy Developing :)

## Running Tests
Testing is being handled using the `pytest` library. When adding tests to the `tests` directory make sure function names start with `test_*`, or they will not be run. To run all tests use the command
```sh
poetry run pytest
```
