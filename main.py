import tkinter as tk
import random

a=tk.Tk()

def main_screen():
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

def easy_mode_file():
    a.destroy()
    b=tk.Tk()
    b.title("Easy Mode")
    b.geometry("594x639")

    rows, cols = 9, 9
    total_cells = rows * cols
    total_mines= 10

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

    l=[]
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            if val == -1:
                text = "💣"
                bgc='red'
            elif val == 0:
                text = ""
                bgc='white'
            else:
                text = str(val)
                bgc='white'

            label = tk.Label(b, text=text, width=8, height=4, bg=bgc,relief='solid')
            label.grid(row=r, column=c, padx=0, pady=0)

            if c%2==0 and r%2!=0 or c%2!=0 and r%2==0:
                colour="grey"
            else:
                colour="white"
            button = tk.Button(b, text="", width=8, height=4, relief="raised", bg=colour)
            button.grid(row=r, column=c)
        
            l.append(button)
        
    for i in l:
        def on_click(b=i):
            b.destroy()
        if text=="💣":
            game_over_screen=tk.Tk()
            game_over_screen.title("GAME OVER")
            game_over_screen.geometry("100x100")
            game_over_label=tk.Label(game_over_screen, text="GAME OVER", width=16, height=8)
            game_over_button=tk.Button(game_over_screen, text="MAIN MENU", width=10, height=2,font=("Arial",14))
            game_over_label.place(x=10,y=20)
            game_over_button.place(x=20,y=30)
            game_over_screen.mainloop()
        i.config(command=on_click)

def medium_mode_file():
    a.destroy()
    b=tk.Tk()
    b.title("Medium Mode")
    b.geometry("676x728")

    rows, cols = 13, 13
    total_cells = rows * cols
    total_mines= 21

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

    l=[]
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            if val == -1:
                text = "💣"
                bgc='red'
            elif val == 0:
                text = ""
                bgc='white'
            else:
                text = str(val)
                bgc='white'

            label = tk.Label(b, text=text, width=6, height=3, bg=bgc,relief='solid')
            label.grid(row=r, column=c, padx=0, pady=0)

            if c%2==0 and r%2!=0 or c%2!=0 and r%2==0:
                colour="grey"
            else:
                colour="white"
            button = tk.Button(b, text="", width=6, height=3, relief="raised", bg=colour)
            button.grid(row=r, column=c)
        
            l.append(button)
        
    for i in l:
        def on_click(b=i):
            b.destroy()
        i.config(command=on_click)

def hard_mode_file():
    a.destroy()
    b=tk.Tk()
    b.title("Hard Mode")
    b.geometry("646x698")

    rows, cols = 17, 17
    total_cells = rows * cols
    total_mines= 35

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

    l=[]
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            if val == -1:
                text = "💣"
                bgc='red'
            elif val == 0:
                text = ""
                bgc='white'
            else:
                text = str(val)
                bgc='white'

            label = tk.Label(b, text=text, width=4, height=2, bg=bgc,relief='solid')
            label.grid(row=r, column=c, padx=0, pady=0)

            if c%2==0 and r%2!=0 or c%2!=0 and r%2==0:
                colour="grey"
            else:
                colour="white"
            button = tk.Button(b, text="", width=4, height=2, relief="raised", bg=colour)
            button.grid(row=r, column=c)
        
            l.append(button)
        
    for i in l:
        def on_click(b=i):
            b.destroy()
        i.config(command=on_click)

main_screen()