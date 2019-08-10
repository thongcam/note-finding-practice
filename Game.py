import tkinter as tk
import os

padding_x = 5
padding_y = 7

def fret():
    master.destroy()
    os.system('python src/Fret_finding_practice.py')

def note():
    master.destroy()
    os.system('python src/Note_finding_practice.py')

master = tk.Tk()

tk.Label(master, text='Choose a game mode:', font='bold').grid(row=0, column=0, columnspan=2, padx = padding_x, pady = padding_y)
tk.Button(master, text='Find Fret', command=fret, width=10).grid(row=4, column=0, pady=4)
tk.Button(master, text='Find Note', command=note,width=10).grid(row=4, column=1, pady=4)


master.mainloop()
