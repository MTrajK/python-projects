# Pizzabot
A project that finds a path (not the best) and gives instructions on how to visit all houses and drop all pizzas.

## Requirements
This project requires Python 3.9.

## Installation
To install this project run:
```
pip install "/path/to/project"
```
To install the project in editable mode, use -e (-e stands for --editable):
```
pip install -e "/path/to/project"
```

## Usage
The project can be run from the command line with (this will invoke ```pizzabot.cli.run()```):
```
pizzabot "NUMxNUM (NUM, NUM) (NUM, NUM)"
```
or imported by another python module with:
```
import pizzabot
```

## Tests
Run all tests (you'll need to be in the root of the project ```cd "/path/to/project"```):
```
python -m unittest
```

## Project structure
```
pizzabot
├──────── pizzabot                          -> The whole Pizzabot code is here.
│         ├──────── __init__.py
│         ├──────── cli.py
│         ├──────── bot.py
│         ├──────── errors.py
│         ├──────── house.py
│         ├──────── input.py
│         └──────── instructions.py
├──────── tests                             -> All tests and resources used within the tests are located in this folder.
│         ├──────── resources
│         │         └──────── test_file.txt
│         ├──────── __init__.py
│         ├──────── test_bot.py
│         ├──────── test_house.py
│         ├──────── test_input.py
│         └──────── test_instruction.py
├──────── setup.py                          -> Setup configuration.
└──────── README.md                         -> Project description.
```

## Notes
This problem is called the "traveling salesman problem" and it's very popular in computer science.
Here I'll try to explain what are the pros and cons of several solutions.

1. If we don't want to optimize the number of the instructions, then we could read the coordinates like they are ordered in the input "first come first served". This will be the fastest solution from the software's aspect O(N) but it won't be optimized and in this case, we'll get the biggest number of instructions.
2. If we want to have the minimum number of instructions, then we'll need to use a brute force algorithm (check all paths using DFS or enumeration, O(N!)) or use dynamic programming approach O(N*2^N). Both solutions are exponential! That means if we have more than 100 houses the algorithm may never complete.
3. But there also exists solutions that are "mixins" of the previous solutions. We can have a fast algorithm that can give a good optimization of the number of instructions, but not always the best (like the previous step). There are several solutions like this, one of them is the nearest neighbor algorithm (greedy solution using simple heuristics O(N^2)), this is used as a current solution. Here is a simple comparison between this solution and the first one:
    ```
    Input: 5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)

    First come first served algorithm
    Path: (0, 0) -> (1, 3) -> (4, 4) -> (4, 2) -> (4, 2) -> (0, 1) -> (3, 2) -> (2, 3) -> (4, 1)
    Instructions: DENNNDEEENDSSDDWWWWSDEEENDWNDEESSD (34 instructions total)

    Nearest neighbor algorithm
    Path: (0, 0) -> (0, 1) -> (1, 3) -> (2, 3) -> (3, 2) -> (4, 2) -> (4, 2) -> (4, 1) -> (4, 4)
    Instructions: DNDENNDEDESDEDDSDNNND (20 instructions total, that's 14 instructions less = 41% less)
    ```

## Task

The task is to instruct Pizzabot on how to deliver pizzas to all the houses in a neighborhood.
In more specific terms, given a grid (where each point on the grid is one house) and a list of points representing houses in need of pizza delivery, return a list of instructions for getting Pizzabot to those locations and delivering. An instruction is one of:

```
N: Move north
S: Move south
E: Move east
W: Move west
D: Drop pizza
```

Pizzabot always starts at the origin point, (0, 0). As with a Cartesian plane, this point lies at the most south-westerly point of the grid.