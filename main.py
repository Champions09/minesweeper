import tkinter as tk
from tkinter import messagebox
import random


def main_screen():
    global a
    a=tk.Tk()
    a.geometry("600x600")
    a.title("Minesweeper")
    
    name_of_game=tk.Label(a,text="MINESWEEPER",font=("Arial",24))
    name_of_game.place(x=180,y=10)
    
    choose_mode=tk.Label(a,text="Choose Mode:-",font=("Arial",16))
    choose_mode.place(x=225,y=150)
    
    easy_mode=tk.Button(a,text="EASY",font=("Arial",14),width=10,height=2,relief="raised",command=easy_mode_file)
    easy_mode.place(x=65,y=225)
    
    medium_mode=tk.Button(a,text="MEDIUM",font=("Arial",14),width=10,height=2,relief="raised",command=medium_mode_file)
    medium_mode.place(x=230,y=225)
    
    hard_mode=tk.Button(a,text="HARD",font=("Arial",14),width=10,height=2,relief="raised",command=hard_mode_file)
    hard_mode.place(x=395,y=225)
    
    instructions=tk.Label(a,text='''                            Instructions:-
                      
                           1.Left click to reveal peice.
                      
                         2.Right click to place flag.
              
                  3.Look out for mines.''',font=("Arial",16))
    instructions.place(x=10,y=350)
    
    a.mainloop()

def create_grid(rows,cols,total_mines):
    total_cells = rows * cols
   
    mines = []
    while len(mines) < total_mines:
        n = random.randint(1, total_cells)
        if n not in mines:
            mines.append(n)
    mines.sort()

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
        
    return grid

def create_UI(rows, cols, mines, window_size, mode, element_width, element_height):
    a.destroy()
    b = tk.Tk()
    b.title(mode + " Mode")
    b.geometry(window_size)

    grid = create_grid(rows, cols, mines)
    buttons = {}

    # Create flagged grid using loop style (like grid)
    flagged = []
    for r in range(rows):
        flagged.append([])
        for c in range(cols):
            flagged[r].append(0)  # 0 = not flagged, 1 = flagged

    def on_right_click(event, r, c):
        btn = buttons[(r, c)]
        if btn["state"] == "disabled":
            return  # can't flag revealed cells

        if flagged[r][c] == 1:
            # unflag
            btn.config(text="", bg="grey")
            flagged[r][c] = 0
        else:
            # flag
            btn.config(text="🚩", bg="lightblue")
            flagged[r][c] = 1

    def on_click(r, c):
        if flagged[r][c] == 1:
            return  # ignore click if flagged

        btn = buttons[(r, c)]
        if btn["state"] == "disabled":
            return  # already revealed

        val = grid[r][c]

        if val == -1:
            btn.config(text="💣", bg="red", state="disabled")
            response = messagebox.askyesno(
                    "Game Over", " You Lost\n Return to Main Menu?", icon='warning')
            if response:
                b.destroy()
                main_screen()
            else:
                b.destroy()
        elif val > 0:
            btn.config(text=str(val), bg="white", relief="sunken", state="disabled", disabledforeground="red")
        else:
            btn.config(text="", bg="white", relief="sunken", state="disabled")

            l = [r-1, r, r+1]
            m = [c-1, c, c+1]
            
            for i in l:
                for j in m:
                    if 0 <= i < rows and 0 <= j < cols and not (i == r and j == c):
                        neighbor_btn = buttons[(i, j)]
                        if neighbor_btn["state"] != "disabled":
                            neighbor_btn.invoke()

    for r in range(rows):
        for c in range(cols):
            button = tk.Button(
                b,
                text="",
                width=element_width,
                height=element_height,
                relief="raised",
                bg="grey",
                command=lambda r=r, c=c: on_click(r, c)
            )
            button.grid(row=r, column=c)
            button.bind("<Button-3>", lambda e, r=r, c=c: on_right_click(e, r, c))
            buttons[(r, c)] = button

def easy_mode_file():
    create_UI(9,9,10,"594x639", 'EASY',8,4)

def medium_mode_file():
    create_UI(13,13,21,"676x728", 'MEDIUM',6,3)

def hard_mode_file():
    create_UI(17,17,35,"646x698", 'HARD',4,2)

def login_screen_ui():
    global login_screen
    login_screen = tk.Tk()
    login_screen.title("Minesweeper")
    login_screen.geometry("600x600")

    tk.Label(login_screen, text="Welcome to Minesweeper", font=("Arial", 36)).place(x=15, y=50)
    tk.Label(login_screen, text="Username:", font=("Arial", 18)).place(x=150, y=200)
    e1 = tk.Entry(login_screen)
    e1.place(x=280, y=210)
    tk.Label(login_screen, text="Password:", font=("Arial", 18)).place(x=150, y=250)
    e2 = tk.Entry(login_screen, show="*")
    e2.place(x=280, y=260)

    btn = tk.Button(login_screen, text="Login", width=10, command=lambda: chk(e1.get(), e2.get()))
    btn.place(x=350, y=300)

    login_screen.mainloop()

# ---------- LOGIN CHECK ----------
def chk(x, y):
    # dummy user dictionary for login check
    d = {"user": "1234", "admin": "admin"}
    if x in d and d[x] == y:
        login_screen.destroy()
        main_screen()
    else:
        messagebox.showerror("Error", "Invalid username or password")
login_screen_ui()