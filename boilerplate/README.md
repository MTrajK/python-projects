# Python Boilerplate
Simple boilerplate for a Python project.

## Requirements
This project requires Python 3+.

## Installation
To install this project's package run:
```
pip install "/path/to/project"
```
To install the package in editable mode, use -e (-e stands for --editable):
```
pip install -e "/path/to/project"
```

## Usage
The package can be run from the command line with (this will invoke ```boilerplate.main.M()```):
```
boilerplate
```
or imported by another python module with:
```
import boilerplate
```

## Tests
Run all tests (you'll need to be in the root of the project ```cd "/path/to/project"```):
```
python -m unittest
```

## Notes
- When importing modules the relative paths aren't used because in that way isn't readable as when the absolute paths are used. Example (current location boilerplate/logic/main_logic.py):
  - Absolute paths:
     ```
     from boilerplate.logic.helper import H
     from boilerplate.utils.common import C
     ```
   - Relative paths:
     ```
     from .helper import H
     from ..utils.common import C
     ```
- "test" folder is excluded (in ```setup.py```) from the installation (it's used only for testing the project, also it need to be excluded as a package because it has ```__init__.py``` which is used for ```python -m unittest```).

## Project structure
```
boilerplate
├──────── boilerplate
│         ├──────── __init__.py
│         ├──────── main.py
│         ├──────── logic
│         │         ├──────── __init__.py
│         │         ├──────── main_logic.py
│         │         └──────── helper.py
│         └──────── utils
│                   ├──────── __init__.py
│                   └──────── common.py
├──────── tests
│         ├──────── __init__.py
│         ├──────── test_main.py
│         ├──────── test_logic.py
│         └──────── test_utils.py
├──────── setup.py
├──────── README.md
├──────── .gitignore
└──────── LICENSE
```