# Collaborators: Kyler Kellogg, Zac Harris

import tkinter as tk
import random

# Define tkinter window
window = tk.Tk()

# tkinter window setup
window.grid()
window.title("Minesweeper")
window['padx'] = 10
window['pady'] = 10
window.maxsize(500, 500)

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

# Define board grid
height = 15 # i'th row
width = 15  # j'th column
grid = [[0]*width for _ in range(height)]
k = 0 # was getting issues with first variable of lambda without this

# Define 2D array for locking squares
locked = [[False]*width for _ in range(height)]
for i in range(0,height):
    for j in range(0,width):
        locked[i][j] = False

# Function for left-clicking a button
def left(i, j):
    if (locked[i][j] == True): # check if square is locked
        return
    print('clicked left', i, j) # debug

# Function for right-clicking a button
def right(i, j):
    if (locked[i][j] == True):
        grid[i][j].config(image = empty)
        locked[i][j] = False
    else:
        grid[i][j].config(image = flag)
        locked[i][j] = True
    print('locked', i, j) # debug

# Generate board
for i in range(0, height):
    for j in range(0, width):
        grid[i][j] = tk.Button(window, image = empty, width = 15, height = 15, command = None)
        grid[i][j].grid(column = j, row = i)
        grid[i][j].bind('<Button-1>', lambda k=k, i=i, j=j: left(i, j))
        grid[i][j].bind('<Button-3>', lambda k=k, i=i, j=j: right(i, j))











window.mainloop()