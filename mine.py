import tkinter as tk
from tkinter import messagebox
import random
import os
import csv

# ---------- CREATE CREDENTIALS FILE IF NOT EXISTS ----------
if not os.path.exists("login_credentials.csv"):
    f= open("login_credentials.csv",'w',newline='')
    f.close()


# ---------- LOGIN SCREEN UI ----------
def login_screen_UI():
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
    btn1=tk.Button(login_screen,text="Sign up",width=10, command=lambda:[login_screen.destroy(),sign_up_screen()])
    btn1.place(x=150,y=300)
    login_screen.mainloop()

# ---------- LOGIN CHECK ----------
def chk(x, y):
    f=open("login_credentials.csv",'r',newline ='')
    d=csv.reader(f,delimiter=',')
    di={}
    for i in d:
        di[i[0]]=i[-1]
    if x in di:
        if di[x]==y:
            login_screen.destroy()
            main_screen()
        else:messagebox.showerror("Error","Please enter correct password")
    else:messagebox.showerror("Error","no such username,Kindly Sign up")
    f.close()

# ---------- SIGN UP SCREEN UI ----------
def sign_up_screen():
    global sign_up_screen
    sign_up_screen = tk.Tk()
    sign_up_screen.title("Minesweeper")
    sign_up_screen.geometry("600x600")
    username=tk.StringVar()
    password=tk.StringVar()
    tk.Label(sign_up_screen, text="Welcome to Minesweeper", font=("Arial", 36)).place(x=15, y=50)
    tk.Label(sign_up_screen, text="Username:", font=("Arial", 18)).place(x=150, y=200)
    e1 = tk.Entry(sign_up_screen,textvariable  = username )
    e1.place(x=280, y=210)
    tk.Label(sign_up_screen, text="Password:", font=("Arial", 18)).place(x=150, y=250)
    e2 = tk.Entry(sign_up_screen, textvariable= password ,show="*")
    e2.place(x=280, y=260)

    btn = tk.Button(sign_up_screen, text="Sign up", width=10, command=login_screen_UI)
    btn.place(x=350, y=300)
    def save_credentials():
        Name=username.get()
        Password=password.get()
        f=open("login_credentials.csv",'r',newline ='')
        d=csv.reader(f,delimiter=',')
        di={}
        for i in d:
            di[i[0]]=i[-1]
        if Name in di:
            messagebox.showerror("Error","Please enter different username")
        else:
            if Name=='' or Password=='':messagebox.showerror("Error","Please enter valid password or username")
            else:
                f= open("login_credentials.csv",'a',newline='')
                obj=csv.writer(f,delimiter=',')
                d=(Name,Password)
                obj.writerow(d)
                f.close()
                messagebox.showinfo("Succesful","Succesfully signed up! Go back to login again")
                sign_up_screen.destroy()
                login_screen_UI()
        f.close()
    btn = tk.Button(sign_up_screen, text="Sign up", width=10, command=save_credentials)
    btn.place(x=350, y=300)
    btn1=tk.Button(sign_up_screen,text="Go back to login screen",width=20,command=lambda:[sign_up_screen.destroy(),login_screen_UI()])
    btn1.place(x=100,y=300)

    sign_up_screen.mainloop()

# ---------- GAME WINDOW ----------
def main_screen():
    global menu_screen
    menu_screen=tk.Tk()
    menu_screen.geometry("600x600")
    menu_screen.title("Minesweeper")
    
    name_of_game=tk.Label(menu_screen,text="MINESWEEPER",font=("Arial",24))
    name_of_game.place(x=180,y=10)
    
    choose_mode=tk.Label(menu_screen,text="Choose Mode:-",font=("Arial",16))
    choose_mode.place(x=225,y=150)
    
    easy_mode=tk.Button(menu_screen,text="EASY\n(10 mines)",font=("Arial",14),width=10,height=2,relief="raised",command=easy_mode_file)
    easy_mode.place(x=65,y=225)
    
    medium_mode=tk.Button(menu_screen,text="MEDIUM\n(21 mines)",font=("Arial",14),width=10,height=2,relief="raised",command=medium_mode_file)
    medium_mode.place(x=230,y=225)
    
    hard_mode=tk.Button(menu_screen,text="HARD\n(35 mines)",font=("Arial",14),width=10,height=2,relief="raised",command=hard_mode_file)
    hard_mode.place(x=395,y=225)
    
    instructions=tk.Label(menu_screen,text='''                            Instructions:-
                      
                           1.Left click to reveal peice.
                      
                         2.Right click to place flag.
              
                  3.Look out for mines.''',font=("Arial",16))
    instructions.place(x=10,y=350)
    
    menu_screen.mainloop()

# ---------- GRID CREATION ----------
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
    menu_screen.destroy()
    game_screen = tk.Tk()
    game_screen.title(mode + " Mode")
    game_screen.geometry(window_size)

    grid = create_grid(rows, cols, mines)
    global buttons
    buttons = {}

    flagged = []
    no_of_flags = 0
    for r in range(rows):
        flagged.append([])
        for c in range(cols):
            flagged[r].append(0)  # 0 = not flagged, 1 = flagged

    def on_right_click(event, r, c):
        nonlocal no_of_flags
        btn = buttons[(r, c)]
        if btn["state"] == "disabled":
            return 

        if flagged[r][c] == 1:
            # unflag
            btn.config(text="", bg="grey")
            no_of_flags -= 1
            flagged[r][c] = 0
        else:
            # flag
            btn.config(text="🚩", bg="lightblue")
            flagged[r][c] = 1
            no_of_flags += 1

            
        #To end the game if all mines are flagged correctly
        if no_of_flags == mines:
            all_flags_correct = True
            for rr in range(rows):
                for cc in range(cols):
                    if flagged[rr][cc] == 1 and grid[rr][cc] != -1:
                        all_flags_correct = False
                        break
                if all_flags_correct==False:
                    break
                
            if all_flags_correct==True:
                response = messagebox.askyesno(
                    "Congratulations!", " You Won!\n Return to Main Menu?", icon='info')
                if response:
                    game_screen.destroy()
                    main_screen()
                else:
                    game_screen.destroy()

    def on_click(r, c):
        if flagged[r][c] == 1:
            return  

        btn = buttons[(r, c)]
        if btn["state"] == "disabled":
            return  # already revealed

        val = grid[r][c]

        if val == -1:
            btn.config(text="💣", bg="red", state="disabled")
            response = messagebox.askyesno(
                    "Game Over", " You Lost\n Return to Main Menu?", icon='warning')
            if response:
                game_screen.destroy()
                main_screen()
            else:
                game_screen.destroy()
        elif val > 0:
            btn.config(text=str(val), bg="white", relief="sunken", state="disabled", disabledforeground="red")
        else:
            btn.config(text="", bg="white", relief="sunken", state="disabled")
            for i in [r-1, r, r+1]:
                for j in [c-1, c, c+1]:
                    if 0 <= i < rows and 0 <= j < cols and not (i == r and j == c):
                        neighbor_btn = buttons[(i, j)]
                        if neighbor_btn["state"] != "disabled":
                            neighbor_btn.invoke()
                    
    # ---------- BUTTON CREATION ----------
    for r in range(rows):
        for c in range(cols):

            button = tk.Button(
                game_screen,
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

login_screen_UI()
 


    
