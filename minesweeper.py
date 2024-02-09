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

# Define board grid
height = 15 # i
width = 15  # j
grid = [[0]*width]*height
k = 0 # was getting issues with first variable of lambda without this

def left(i, j):
    print('clicked left', i, j)

def right(i, j):
    print('clicked right', i, j)

# Generate board
for i in range(0, height):
    for j in range(0, width):
        grid[i][j] = tk.Button(window, image = empty, width = 15, height = 15, command = None)
        grid[i][j].grid(column = j, row = i)
        grid[i][j].bind('<Button-1>', lambda k=k, i=i, j=j: left(i, j))
        grid[i][j].bind('<Button-3>', lambda k=k, i=i, j=j: right(i, j))











window.mainloop()