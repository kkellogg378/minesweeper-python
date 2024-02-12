# Collaborators: Kyler Kellogg, Zac Harris

import tkinter as tk
import random
from base64 import b64decode

# Flags
debug_mode = True
isGameOver = False
isShowBombsEnabled = False
needGenerateBombs = True

# Define tkinter window
window = tk.Tk()

# tkinter window setup
window.grid()
window.title("Minesweeper Python")
window['padx'] = 10
window['pady'] = 10
#window.maxsize(500, 500)

# Define images (encoded with https://www.base64-image.de/)
empty = tk.PhotoImage(width = 1, height = 1)
safe1 = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAEhJREFUOE9jZKAAMFKgl4GA5v//IYYzYlWHRzNMI8makTWSpBldI0maYUFItrNBBgwxzdgCDBYOqPGNJZ4p0kx8gqVl2sbvCgCtJRQQZgBfgwAAAABJRU5ErkJggg=="))
safe2 = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAF9JREFUOE+1klEOwCAIQ8vNvflMljkZqykL01/zWlowFJ4VWDzhhkOKtclMOAMO5UuAw079nsSLv2A172eYRaGZvfMqf4iTa5t1ALhViRFZJRtWpZs/TX88T+UY/kvOHY2MFhDiFMvZAAAAAElFTkSuQmCC"))
safe3 = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAFRJREFUOE9jZKAAMFKglwGu+T8Dw39CBjEyINSD1JKkGaoBrocoZyO7Ctl26mvG5X+cfkYOLIo0o4c6bf1MTDzjjCpiNBMVYIRSGkyeqHjGZRhFmgHAdRQQiyS3RgAAAABJRU5ErkJggg=="))
safe4 = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAEdJREFUOE9jZKAAMFKglwGL5ob/CAMbgPLofIQsNTVjs4Vom8nWjKwRXzCCwgECkPxMkWZcthHtZ2wGDFHNuEOe2mmb+KwCAC7AHBCUCtM7AAAAAElFTkSuQmCC"))
safe5 = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAEpJREFUOE9jZKAAMFKglwGuuYGB4T8xBjUwIPRQXzOy6fhcg9VmijTjsg3dUOr4GZ/fkGMCa2hTpJnm8YwzwIhJXehqqJO2ybEZANVNFBCzlBrwAAAAAElFTkSuQmCC"))
safe6 = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAE9JREFUOE9jZKAAMFKglwFVc0PDf7yGNTSgqEdwCGkEmUqUZjRFuFyD3WaKNOOyiihn4ws1JAOIczZyYNJWM8nOhsQjmYmEjHRKxbRNou0AxOkkEEjhQL4AAAAASUVORK5CYII="))
safe7 = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAEZJREFUOE9jZKAAMFKglwFZ838iDYLroZpmfBYjuwqrzTTRjNVWkE3EhDbZmnFqJMZmsjXj1UjIZoo0E0xwxIQ2TkMo0gwAOZgKEFKsVmoAAAAASUVORK5CYII="))
safe8 = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAFFJREFUOE9jZKAAMFKglwFFc0NDw398hjU0NKCoh3MIaYQZimwAVs3oNiAbTH3NIGcRcjpOP1OkGZe/0A2lvp8J+RdvVFHkZ3KSKfXSNqm2AwB9QDgQM4mjgQAAAABJRU5ErkJggg=="))
bomb = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAGFJREFUOE9jZKAAMBLQ+5+BgQGnGqpqhtkEotEByCIUl2CzGZtGmEEo6tE1gzX+/w/Rz8iI1VdwQapoxudUXBGC4S5iDMHvbAJxj1MzOLzwaCYY2rD4JCuekTXRL3mSlMcA+jwXEI8MpjUAAAAASUVORK5CYII="))
bomb_red = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAGhJREFUOE9jfCuj8p+BTMCIT7PwkzsMb2VUcBpNPc0wm0A0OgC5AN0lGDZj0wgzCN0LKJphGv//h4QhIyMjVhfABCnXjM+puIIa5AWsNuOLdmR/U08zyEaKQhsWn2TFM7Im+iVPUjMXAEKeWaS+0+s1AAAAAElFTkSuQmCC"))
flag = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAFNJREFUOE9jZKAAMFKglwGn5v8MDP9BBjOCEXaAIQHTBFNOtGZ0jfSzGdlnZPkZLWhAgUZ8gFFDMziakABW29EF0TWhRzCKeqpqJim10iZtE+MEADQrDxCxpPdTAAAAAElFTkSuQmCC"))

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
    showBombs()
    
    # Mark the bomb the user clicked with red
    grid[i][j].config(image = bomb_red)
    
    # Destroy any debug buttons 
    debugButton.destroy()
    
    # Debug output
    if (debug_mode == True):
        print('Game over! Bomb at', i, j)
    
    return

# Function for left-clicking a button
def left(i, j):
    # Define global variables
    global needGenerateBombs
    
    # Check whether the game is over or if the square is locked
    if (isGameOver == True or locked[i][j] == True): 
        return
    
    # Check whether bombs need generated
    if (needGenerateBombs == True):
        generateBombsOnClick(i, j)
        needGenerateBombs = False
    
    # Check whether the square hides a bomb
    if (isBomb[i][j] == True):
        endGame(i, j)
        return
    
    # Lock button in flat state
    grid[i][j].config(relief = 'flat')
    
    # Debug output
    if (debug_mode == True):
        print('clicked left', i, j)
    
    return

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

# Function for generating the board
def generateBoard(h, w):
    # Define global variables
    global height, width, grid, locked
    
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
    
    return

# Function for generating bombs on the first click
def generateBombsOnClick(i, j):
    # Define global variables
    global isBomb
    
    # Generate bomb locations
    isBomb = [[False]*width for _ in range(height)]
    for _ in range(0, numBombs):
        while True:
            bombi = random.randint(0, height - 1)
            bombj = random.randint(0, width - 1)
            
            # Check if this location already has a bomb
            if (isBomb[bombi][bombj] == True):
                continue
            
            # Check if this is where the user clicked
            if (bombi == i and bombj == j):
                continue
            
            isBomb[bombi][bombj] = True
            break
    
    # Debug output
    if (debug_mode == True):
        print('Generated Bombs!')
    
    return

# Function for showing bomb locations
def showBombs():
    # Define global variables
    global isShowBombsEnabled
    
    # Check whether bombs need generated still
    if (needGenerateBombs == True):
        return
    
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

generateBoard(15, 15)
numBombs = 30

# This can only be enabled after board generation because the 'width' and 'height' variables need to be defined
debugButton = tk.Button(window, text = "show bombs", command = lambda: showBombs())
debugButton.grid(column = width, row = 0, rowspan = 2)
if (debug_mode == False):
    debugButton.destroy()


window.mainloop()