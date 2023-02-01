# Workshop

## How to solve a sudoku with the help of image recognition

<center>
  <img
  src="misc/solving.gif">
</center>

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
    pip3 install numpy
    pip3 install selenium
    pip3 install pillow
```

## Solve a sudoku

Now that everything is installed, let's try solving a Sudoku puzzle.

If you're unfamiliar with the rules of the game, you can find them [here](https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/):

We will use a method called backtracking to solve it. You can learn more about backtracking [here](https://en.wikipedia.org/wiki/Backtracking):

First, let's create an array to simulate a grid.

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

Don't worry, later we will replace it with an empty grid. It's just to make sure that your solving algorithm is working.

Next, let's create a function that returns all the possible numbers for a cell.

```python
def posibility(board, x, y):
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # find posibility in row and col

    # find posibility in 3x3

    return number
```

Once we have all the possible numbers for each cell, we need to iterate over the entire grid and get the possible numbers for every cell. Then, we will test them using a backtracking algorithm.

```python
def solve():
    for x in range(9):
        for y in range(9):
            # Code a recursive call of the updated tab with a possible number for th cell
```

When you call the solve function your tab should look like this

```python
[9, 7, 2, 4, 1, 3, 8, 5, 6]
[8, 5, 3, 9, 7, 6, 4, 1, 2]
[4, 1, 6, 8, 5, 2, 7, 3, 9]
[3, 6, 4, 7, 9, 5, 1, 2, 8]
[1, 9, 8, 2, 3, 4, 5, 6, 7]
[5, 2, 7, 1, 6, 8, 9, 4, 3]
[6, 4, 5, 3, 8, 7, 2, 9, 1]
[2, 8, 9, 6, 4, 1, 3, 7, 5]
[7, 3, 1, 5, 2, 9, 6, 8, 4]
```

## Start Selenium and get the grid

Okay, now we know how to solve a Sudoku.

Let's take it a step further and try solving a Sudoku on a website.

We will use [Selenium](https://selenium-python.readthedocs.io/) and the website https://sudoku.com/fr.

In the main function, you will need to initialize the driver using Selenium (here, I am using Firefox) and the "action" variable, which will allow us to interact with the browser.

```python
    driver = webdriver.Firefox()
    action = webdriver.ActionChains(driver)
```

Now, let's create a function named get_board_image that takes the driver as its parameter. This function will open the Sudoku website, capture the grid, and save it as a PNG image in a variable.

```python
def get_board_image(driver, action):
    # Open the url and put the window in fullscreen

    # wait for the page to load
    sleep(2)
    cookies = driver.find_element(by=By.ID, value="Here Id of the accept bouton for cookies")
    action.move_to_element(cookies).click().perform()
    sleep(3)

    canvas = driver.find_element(by=By.TAG_NAME, value="Get the board by its TAG")
    # Take a screeshot of the canvas

    # Here we are going to get the canvas and we are going to resize it to a size of 2000x2000
    img = Image.open("board.png")

    size = canvas.size
    size = size["width"]


    img = img.crop((5, 5, size - 5, size - 5))
    img = img.resize((2000, 2000))

    # Convert png image to byte
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="PNG")
    canvas_png = img_byte_arr.getvalue()


    # save result into a file
    with open(r"canvas.png", 'wb') as f:
        f.write(canvas_png)

    size = size - 10

    return canvas, size, canvas_png
```

## Training of the model

Okay, now we know how to solve a Sudoku puzzle. Let's try solving it automatically.

To do that, we will first train our model. It will be very easy, I already provided the code in the IA folder. Now you just need to set the path to the training PNG images.

Now start the training :

```bash
python3 ia-train.py
```

A window will open, and numbers will be displayed. You just need to tell the AI what number is in each square.

Once this is done, two files should be created.

```
generalsamples.data
generalresponses.data
```

## Using the model

Ok, So now we can finally get the number of this screen. For that we are going to work on this function.

```python
def get_board_value(canvas_size, img):
    size = 222
    sclice: int = canvas_size / 10

    # Convert img to a Numpy array in uint8, after that use cv2 to decode the array using the IMREAD_COLOR params

    if (not np.any(img)):
        raise Exception("Image not found")

    for i in range(1, 10):
        for j in range(1, 10):
            # Crop the img to only have a single cell

            # Call the predict_digit function with the crop img and put it into tab and ref
```

## Solving on the site

We are on the final step, now we just need to put number into the canvas.

First we are going to code two last function:

```python
def get_key(number):
    # return the keypad number corresponding to number using Keys
```

```python
def update_slot(action, number):
    # get the key from get_key and use action to press the key
```

Now we can do the loop to update all the slot on the canvas

```python
for i in range(9):
    for j in range(9):
        if ref[i][j] == 0:
            update_slot(action, tab[i][j])
        # move the offset to the left by 55
    # move the offset to the left by -495 (the start) and down by 55
```

Your main should look to something like this

```python
def main():
    try:
        driver = webdriver.Firefox()
        action = webdriver.ActionChains(driver)

        canvas, canvas_size, canvas_png = get_board_image(driver, action)
        action.move_to_element(canvas).click().perform()
        action.move_by_offset(-230, -230).click().perform()
        get_board_value(canvas_size, canvas_png)
        solve()
        for i in range(9):
            for j in range(9):
                if ref[i][j] == 0:
                    update_slot(action, tab[i][j])
                # move the offset to the left by 55
    # move the offset to the left by -495 (the start) and down by 55
    except Exception as e:
        print(e)
        driver.quit()
```

## More ?

Now you can do anything you want.

Optimize to be even faster, or you can use a loop to solve Sudoku for the rest of your life.

The possibilities are infinite, it all depends on you.
