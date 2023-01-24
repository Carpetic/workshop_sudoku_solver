
# Workshop
## How to solve a sudoku with the help of image recognition


## Installation

Check your version of python3, If you don't have it you will need to install it, after that you can get Pip :

```bash
    python3 --version
    sudo apt-get install python3
    sudo apt-get install python3-pip
```

Now that you got pip, you can install the rest of the dependencies
```bash
    pip3 install opencv-python
    pip3 install base64
    pip3 install numpy
    pip3 install selenium
```

## Solve a sudoku

Now that everything is installed we are going to try to solve a sudoku, 

if you don't know the rule of the game you can check them here https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/

We are going to use a method call backtracking to solve it https://en.wikipedia.org/wiki/Backtracking

First, we are going to create an array to simulate a grid
```python
tab = [
    [9, 0, 0, 4, 0, 0, 0, 0, 0],
    [8, 0, 3, 0, 7, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 2, 7, 0, 0],
    [3, 0, 4, 0, 0, 5, 0, 0, 8],
    [0, 9, 0, 0, 3, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 4, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 5],
    [7, 0, 1, 0, 2, 0, 0, 8, 0]
    ]
```

Don't worry later we are going to replace it by an empty one that just to make sure that your solving algorithm is working

To solve this sudoku we need to iterate over all the number of the grid, and when we find an empty cell (with number 0), we need to get all the possible number that can go in this cell. Once we have those number, we can replace the cell by one of the possible number and try to solve the tab again (recursive)

```python
def solve():
    for x in range(9):
        for y in range(9):
            // Code a recursive call of the updated tab with a possible number
```


## Training of the model
## Start Selenium and get the grid
