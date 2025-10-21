import tkinter as tk
import random

a=tk.Tk()
f=0 
a.geometry("612x657")
for r in range(9):
    for c in range(9):
        x=random.randint(0,100)
        if x==0:
            label=tk.Label(a,text="",width=8,height=4)
            button=tk.Button(a,text="",width=8,height=4,relief="raised",bg="black")
        if x>=0 and x<=15 and f<10:
            label=tk.Label(a,text="💣",width=8,height=4)
            button=tk.Button(a,text="",width=8,height=4,relief="raised",bg="white")
            f+=1    
        if x>=16 and x<=30:
            label=tk.Label(a,text="",width=8,height=4)
            button=tk.Button(a,text="",width=8,height=4,relief="raised",bg="black")
        if x>=31 and x<=50:
            label=tk.Label(a,text="",width=8,height=4)
            button=tk.Button(a,text="",width=8,height=4,relief="raised",bg="black")
        if x>51 :
            label=tk.Label(a,text="",width=8,height=4)
            button=tk.Button(a,text="",width=8,height=4,relief="raised",bg="black")
        label.grid(row=r, column=c, padx=0.5, pady=0.5)
        button.grid(row=r, column=c, padx=0.5, pady=0.5)

a.mainloop()