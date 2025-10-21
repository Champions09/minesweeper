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
    instructions=tk.Label(a,text='''Instructions:-
                      1.Left click to reveal peice.
                      2.Right click to place flag.
                      3.Look out for mines.''',font=("Arial",16))
    instructions.place(x=10,y=350)
    a.mainloop()

def easy_mode_file():
    a.destroy()
    b=tk.Tk()
    f=0
    b.title("Easy Mode")
    for r in range(9):  
        for c in range(9):
            if c%2==0 and r%2!=0 or c%2!=0 and r%2==0:
                colour="grey"
            else:
                colour="white"
            button=tk.Button(b,text="",width=8,height=4,relief="raised",bg=colour)
            button.grid(row=r, column=c, padx=0.5, pady=0.5)
            b.geometry("612x657")

def medium_mode_file():
    a.destroy()
    b=tk.Tk()
    b.title("Medium Mode")
    for r in range(13):
        for c in range(15):
            if c%2==0 and r%2!=0 or c%2!=0 and r%2==0:
                colour="grey"
            else:
                colour="white"
            button=tk.Button(b,text="",width=6,height=3,relief="raised",bg=colour)
            button.grid(row=r, column=c, padx=0.5, pady=0.5)
            b.geometry("703x755")

def hard_mode_file():
    a.destroy()
    b=tk.Tk()
    b.title("Hard Mode")
    for r in range(17):  
        for c in range(17):
            if c%2==0 and r%2!=0 or c%2!=0 and r%2==0:
                colour="grey"
            else:
                colour="white"
            button=tk.Button(b,text="",width=4,height=2,relief="raised",bg=colour)
            button.grid(row=r, column=c, padx=0.5, pady=0.5)
            b.geometry("600x645")

main_screen()