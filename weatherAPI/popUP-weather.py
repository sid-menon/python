from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkmb
import weather
from time import gmtime, strftime
from datetime import datetime

x = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #time in this timezone

def write_slogan():
    # info message box
    str = weather.weath("Bursa") #use callback to get weather at location
    info_message = str
    tkmb.showinfo("Current Weather", info_message) #shows info in another window

master = tk.Tk()
e = Entry(master)
e.pack()

e.focus_set()

def callback():
    return e.get() #returns value from text input for later use

write_slogan()
master.mainloop()