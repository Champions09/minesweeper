import tkinter as tk
import random

a = tk.Tk()
a.title("Minesweeper")
a.geometry("612x657")

rows, cols = 9, 9
total_cells = rows * cols
total_mines= 10

mines = []
while len(mines) < total_mines:
    n = random.randint(1, total_cells)
    if n not in mines:
        mines.append(n)
mines.sort()
print(mines)

def convert_num_to_grid(num):
    row = (num - 1) // cols
    col = (num - 1) % cols
    return row, col

grid =[]
for r in range(rows):
    grid.append([])
    for c in range(cols):
        grid[r].append(0)

'''
(r-1,c-1)  (r-1,c)  (r-1,c+1)
(r,  c-1)  (r,  c)  (r,  c+1)
(r+1,c-1)  (r+1,c)  (r+1,c+1)
'''
for num in mines:
    r,c = convert_num_to_grid(num)
    grid[r][c] = -1 #mine is present at this position
    
    #adding plus one to the neighbouring boxes
    l=[r-1,r,r+1]
    m=[c-1,c,c+1]
    
    for i in l:
        for j in m:
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] != -1:
                grid[i][j] += 1

l=[]
for r in range(rows):
    for c in range(cols):
        val = grid[r][c]
        if val == -1:
            text = "💣"
            bgc='red'
        elif val == 0:
            text = "0"
            bgc='white'
        else:
            text = str(val)
            bgc='white'

        label = tk.Label(a, text=text, width=8, height=4, bg=bgc,relief='solid')
        label.grid(row=r, column=c, padx=0.5, pady=0.5)

        button = tk.Button(a, text="", width=8, height=4, relief="raised", bg="grey")
        button.grid(row=r, column=c, padx=0.5, pady=0.5)
        
        l.append(button)
        

for i in l:
    def on_click(b=i):
        b.destroy()
    i.config(command=on_click)
a.mainloop()
