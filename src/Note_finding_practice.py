from random import randint
import tkinter as tk
from tkinter import ttk, messagebox
import time as t
import sys

pause_timer = False
times = 1
time_limit = 1
corrects = 0
incorrects = 0
total_time = 0
padding_x = 5
padding_y = 7
close = True
already = []
note = ''
notesList = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
notes = {
        'E' : ['F','F#','G','G#','A','A#','B','C','C#','D','D#'],
        'A' : ['A#','B','C','C#','D','D#','E','F','F#','G','G#'],
        'D' : ['D#','E','F','F#','G','G#','A','A#','B','C','C#'],
        'G' : ['G#','A','A#','B','C','C#','D','D#','E','F','F#'],
        'B' : ['C','C#','D','D#','E','F','F#','G','G#','A','A#'],
        'e' : ['F','F#','G','G#','A','A#','B','C','C#','D','D#']
}

def done(event = None):
    global time_limit, times, close
    v1 = e1.get()
    v2 = e2.get()
    try:
        time_limit =int(v2)
        times = int(v1)
        master.destroy()
        close = False
    except:
        messagebox.showerror('Input Error', "Please input again")
        e2.delete(0, 'end')
        e1.delete(0, 'end')

master = tk.Tk()

tk.Label(master, text = "Welcome to Note Finding Practice.", font =' bold').grid(row = 0, column = 0, columnspan = 2, padx = padding_x, pady = padding_y)
tk.Label(master, text="How many times do you want to practice?").grid(row=1, padx = padding_x, pady = padding_y)
tk.Label(master, text="Time limit for each try: (seconds)").grid(row=2, padx = padding_x, pady = padding_y)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

tk.Button(master, text='Quit', command=quit).grid(row=3, column=0, sticky=tk.W + tk.E, pady=4)
tk.Button(master, text='Done', command=done).grid(row=3, column=1, sticky=tk.W + tk.E, pady=4)
master.bind('<Return>',done)

master.mainloop()

if close:
    sys.exit()

root = tk.Tk()
root.title('NOTE FINDING PRACTICE')

titulo = tk.Label(root, text = 'NOTE FINDING PRACTICE', font =  'Helvetica 18 bold').grid(row = 0, column = 0, columnspan = 5, sticky = tk.W+tk.E, padx = padding_x, pady = padding_y)

progress = ttk.Progressbar(root, value = 0, maximum = times, orient = tk.HORIZONTAL, length = 300, mode = 'indeterminate')
progress.grid(row = 1, column = 1, columnspan = 2, sticky = tk.W+tk.E, padx = padding_x, pady = padding_y)

progress_label = tk.Label(root, text = "Notes Completed")
progress_label.grid(row = 1, column = 0, padx = padding_x, pady = padding_y)

progress_num_label = tk.Label(root, text = str(corrects + incorrects) + '/' + str(times))
progress_num_label.grid(row = 1, column = 3, padx = padding_x, pady = padding_y)

time = ttk.Progressbar(root, value = 0, maximum = time_limit, orient = tk.HORIZONTAL, length = 300, mode = 'indeterminate')
time.grid(row = 2, column = 1, columnspan = 2, sticky = tk.W+tk.E, padx = padding_x, pady = padding_y + 6)

time_label = tk.Label(root, text = "Time")
time_label.grid(row = 2, column = 0, padx = padding_x, pady = padding_y)

time_num_label = tk.Label(root, text = str(time['value']) + '/' + str(time_limit))
time_num_label.grid(row = 2, column = 3, padx = padding_x, pady = padding_y)

description = tk.Label(root, text = '', font = 'Helvetica 18 ' )
description.grid(row = 3, column = 0,columnspan = 4, sticky = tk.W+tk.E,padx = padding_x, pady = padding_y)

correct_label = tk.Label(root, text = 'Corrects: ', font = 'Helvetica 12', fg = "#009900").grid(row = 4, column = 3, padx = padding_x, pady = padding_y-3)
correct = tk.Label(root, text = str(corrects), font = 'Helvetica 24', fg = "#009900")
correct.grid(row = 5, column = 3, padx = padding_x, pady = padding_y-3)

incorrect_label = tk.Label(root, text = 'Incorrects: ', font = 'Helvetica 12', fg = "#ff0000").grid(row = 6, column = 3, padx = padding_x, pady = padding_y-3)
incorrect = tk.Label(root, text = str(corrects), font = 'Helvetica 24', fg = "#ff0000")
incorrect.grid(row = 7, column = 3, padx = padding_x, pady = padding_y-3)

answer = tk.Label(root, text = '', font = 'Helvetica 28 bold', fg = "#009900")
answer.grid(row = 3, column = 3, sticky = tk.W + tk.E, padx = padding_x, pady = padding_y)

total_time_label = tk.Label(root, text = 'Total time: ' + str(total_time),  font = 'Helvetica 15 bold')
total_time_label.grid(row = 8, column = 0, columnspan = 3, sticky = tk.W+tk.E,padx = padding_x, pady = padding_y)

def random_note():
        string = list(notes.keys())[randint(0,5)]
        fret = randint(1,11)
        return string, fret

class choices():
    button_list = []
    def __init__(self,choice,x,y):
        self.value = choice
        self.notebutton = tk.Button(root, text = self.value,command = lambda: self.click(), height = 2, width = 7)
        self.notebutton.grid(row = 4 + x, column = y, padx = padding_x, pady = padding_y)
        self.color = self.notebutton.cget("background")

    def click(self):
        global corrects, incorrects, note, pause_timer, times, progress, answer
        progress['value'] += 1
        answer.config(text = note)
        for i in choices.button_list:
            i.notebutton['state'] = 'disabled'
        if self.value == note:
            corrects += 1
            correct.config(text = str(corrects))
            self.notebutton.config(bg = 'green')
            pause_timer = True
            root.after(1000,nextTry)
        else:
            incorrects += 1
            incorrect.config(text = str(incorrects))
            self.notebutton.config(bg = 'red')
            for i in choices.button_list:
                if i.value == note:
                    i.notebutton.config(bg = 'green')
                    pause_timer = True
                    root.after(1000,nextTry)

x = 0
y = 0

for i in notesList:
    if y != 3:
        choices(i, x, y)
        choices.button_list.append(choices(i, x, y))
        y += 1
    else:
        x += 1
        y = 1
        choices(i, x, 0)
        choices.button_list.append(choices(i, x, 0))

def updateClock():
    global total_time, total_time_label, pause_timer, time_limit, incorrects, incorrect
    if not pause_timer:
        total_time += 0.1
        total_time_label['text'] = 'Total time: ' + str(round(total_time,2))
        time['value'] += 0.1
        time_num_label.config( text = str(round(time['value'],2)) + '/' + str(time_limit))
    if time['value'] >= time_limit:
        incorrects += 1
        progress['value'] += 1
        incorrect.config(text = str(incorrects))
        answer.config(text = note)
        pause_timer = True
        for i in choices.button_list:
            i.notebutton['state'] = 'disabled'
            if i.value == note:
                i.notebutton.config(bg = 'green')
        root.after(1000, nextTry)
        root.after(1000,updateClock)
    else:
        root.after(100,updateClock)

def nextTry():
    global already, note, progress, pause_timer, progress_num_label, answer
    answer.config(text = '')
    progress_num_label.config(text = str(corrects + incorrects) + '/' + str(times))
    for i in choices.button_list:
        i.notebutton['state'] = 'normal'
        i.notebutton.config(bg = i.color)
    pause_timer = False
    if corrects + incorrects == times:
        root.destroy()
        endGame()
    else:
        string, fret = random_note()
        while (string,fret) in already:
            if times%66 == 0:
                    already = []
                    break
            string, fret = random_note()
        description.config(text = string + ' string, fret ' + str(fret))
        time['value'] = 0
        note = notes[string][fret-1]
        already.append((string,fret))


def endGame():
    global corrects, incorrects, total_time, padding_x, padding_y
    end_screen = tk.Tk()
    title_label = tk.Label(end_screen, text = "Ey you finished the practice!!!", font = "Helvetica 18", anchor ='w').grid(row = 0, column = 0, columnspan = 2, padx = padding_x, pady = padding_y + 6)

    cr_label = tk.Label(end_screen, text = 'How many you nailed: ', font = 'Helvetica 13').grid(row = 1, column = 0, padx = padding_x, pady = padding_y , sticky ='W')
    cr = tk.Label(end_screen, text = str(corrects), font = 'Helvetica 14', fg = '#009900').grid(row = 1, column = 1, padx = padding_x, pady = padding_y, sticky ='E')

    icr_label = tk.Label(end_screen, text = 'How many you failed: ', font = 'Helvetica 13').grid(row = 2, column = 0, padx = padding_x, pady = padding_y, sticky ='W')
    icr = tk.Label(end_screen, text = str(incorrects), font = 'Helvetica 14', fg = '#ff0000').grid(row = 2, column = 1, padx = padding_x, pady = padding_y, sticky ='E')

    tt_label = tk.Label(end_screen, text = 'Total time: ' + str(round(total_time,2)) + 's', font = 'Helvetica 13 bold').grid(row = 3, column = 0, columnspan = 2,  padx = padding_x, pady = padding_y, sticky ='W')

    aver_label = tk.Label(end_screen, text = 'Average per note: ' + str(round(total_time/(corrects + incorrects),2))  + 's', font = 'Helvetica 13 bold').grid(row = 4, column = 0, columnspan = 2, padx = padding_x, pady = padding_y, sticky ='W')

    if incorrects/(corrects + incorrects) >= 1/2:
        feedback = tk.Label(text = "Practice more!", font = 'Helvetica 14', anchor ='w').grid(row=5,column = 0, columnspan = 2, sticky = tk.W+tk.E, padx = padding_x, pady = padding_y + 6)
    elif incorrects/corrects <= 1/2 and incorrects:
        feedback = tk.Label(text = "That's not bad.", font = 'Helvetica 14', anchor ='w').grid(row=5,column = 0, columnspan = 2, sticky = tk.W+tk.E, padx = padding_x, pady = padding_y + 6)
    elif incorrects == 0:
        feedback = tk.Label(text = "WOWW!", font = 'Helvetica 14', anchor ='w').grid(row=5,column = 0, columnspan = 2, sticky = tk.W+tk.E, padx = padding_x, pady = padding_y + 6)
    end_screen.mainloop()
updateClock()
nextTry()

root.mainloop()
