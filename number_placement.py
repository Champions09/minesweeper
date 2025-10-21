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

current_grid_number = 1 

l=[]

for r in range(rows):
    rows_buttons = []
    for c in range(cols):
        if current_grid_number in mines:
            label=tk.Label(a,text="💣",width=8,height=4)
            button=tk.Button(a,text="",width=8,height=4,relief="raised",bg="white")
            l.append(button)
        else:
            label=tk.Label(a,text="",width=8,height=4)
            button=tk.Button(a,text="",width=8,height=4,relief="raised",bg="grey")
            l.append(button)
        label.grid(row=r, column=c, padx=0.5, pady=0.5)
        button.grid(row=r, column=c, padx=0.5, pady=0.5)
        current_grid_number+=1
    
for i in l:
    def on_click(b=i):
        b.destroy()
    i.config(command=on_click)
a.mainloop()