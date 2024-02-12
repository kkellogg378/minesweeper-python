# Collaborators: Kyler Kellogg, Zac Harris

import tkinter as tk
import random

# Flags
debug_mode = True
isGameOver = False
isShowBombsEnabled = False

# Define tkinter window
window = tk.Tk()

# tkinter window setup
window.grid()
window.title("Minesweeper Python")
window['padx'] = 10
window['pady'] = 10
#window.maxsize(500, 500)

# Define images
empty = tk.PhotoImage(width = 1, height = 1)
safe1 = tk.PhotoImage(file = './assets/1.png')
safe2 = tk.PhotoImage(file = './assets/2.png')
safe3 = tk.PhotoImage(file = './assets/3.png')
safe4 = tk.PhotoImage(file = './assets/4.png')
safe5 = tk.PhotoImage(file = './assets/5.png')
safe6 = tk.PhotoImage(file = './assets/6.png')
safe7 = tk.PhotoImage(file = './assets/7.png')
safe8 = tk.PhotoImage(file = './assets/8.png')
bomb = tk.PhotoImage(file = './assets/bomb.png')
bomb_red = tk.PhotoImage(file = './assets/bomb_red.png')
flag = tk.PhotoImage(file = './assets/flag.png')

#############
# Functions #
#############

# Function for when the game ends
def endGame(i, j):
    # Define global variables
    global isShowBombsEnabled, isGameOver
    
    # Update flags
    isGameOver = True
    isShowBombsEnabled = False
    
    # Show bomb locations
    ShowBombs()
    
    # Mark the bomb the user clicked with red
    grid[i][j].config(image = bomb_red)
    
    # Destroy any debug buttons 
    debugButton.destroy()
    return

# Function for left-clicking a button
def left(i, j):
    # Check whether the game is over or if the square is locked
    if (isGameOver == True or locked[i][j] == True): 
        return
    
    # Check whether the square hides a bomb
    if (isBomb[i][j] == True):
        endGame(i, j)
        return
    
    # Lock button in flat state
    grid[i][j].config(relief = 'flat')
    
    # Debug output
    if (debug_mode == True):
        print('clicked left', i, j)

# Function for right-clicking a button
def right(i, j):
    # Check whether the game is over or if the square has already been clicked
    if (isGameOver == True or grid[i][j]["relief"] == 'flat'):
        return
    
    # Check whether there is already a flag there
    if (locked[i][j] == True):
        grid[i][j].config(image = empty)
        locked[i][j] = False
        # Debug output
        if (debug_mode == True):
            print('unlocked', i, j)
    else:
        grid[i][j].config(image = flag)
        locked[i][j] = True
        # Debug output
        if (debug_mode == True):
            print('locked', i, j)
    
    return

# Function for generating a new game
def generate_board(h, w, m):
    # Define global variables
    global height, width, grid, locked, isBomb
    
    # TODO: implement difficulty selection button/label removal
    
    # Define variables
    height = h # i'th row
    width = w  # j'th column
    grid = [[0]*width for _ in range(height)]
    k = 0 # was getting issues with first variable of lambda function without this
    
    # Define 2D array for locking squares
    locked = [[False]*width for _ in range(height)]
    for i in range(0, height):
        for j in range(0, width):
            locked[i][j] = False
    
    # Generate board
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = tk.Button(window, image = empty, width = 15, height = 15, command = None)
            grid[i][j].grid(column = j, row = i)
            grid[i][j].bind('<ButtonRelease-1>', lambda k=k, i=i, j=j: left(i, j))
            grid[i][j].bind('<Button-3>', lambda k=k, i=i, j=j: right(i, j))
    
    # Generate bomb locations
    isBomb = [[False]*width for _ in range(height)]
    for _ in range(0, m):
        while True:
            bombi = random.randint(0, height - 1)
            bombj = random.randint(0, width - 1)
            if (isBomb[bombi][bombj] == True):
                continue
            isBomb[bombi][bombj] = True
            break
    
    return

# Function for showing bomb locations
def ShowBombs():
    # Define global variables
    global isShowBombsEnabled
    
    # Check whether bombs are already being shown
    if (isShowBombsEnabled == True):
        debugButton.config(text = "show bombs")
        isShowBombsEnabled = False
    else:
        debugButton.config(text = "hide bombs")
        isShowBombsEnabled = True
    
    # Show or hide bombs
    for i in range(0, height):
        for j in range(0, width):
            if (isBomb[i][j] == True):
                if (isShowBombsEnabled == True):
                    grid[i][j].config(image = bomb)
                else:
                    # Check whether the square holds a flag
                    if (locked[i][j] == True):
                        grid[i][j].config(image = flag)
                    else:
                        grid[i][j].config(image = empty)
    
    return

########
# Main #
########

# TODO: implement difficulty selection

generate_board(15, 15, 20)

# This can only be enabled after board generation because the 'width' and 'height' variables need to be defined
debugButton = tk.Button(window, text = "show bombs", command = lambda: ShowBombs())
debugButton.grid(column = width, row = height)
if (debug_mode == False):
    debugButton.destroy()


window.mainloop()