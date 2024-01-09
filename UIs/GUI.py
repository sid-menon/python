import tkinter as tk
import insertIntoTXT

master = tk.Tk()
tk.Label(master, text="Filename").grid(row=0)
tk.Label(master, text="Text").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1,pady = 20,ipady = 100, ipadx = 175)

def intoFile():
    insertIntoTXT.insert(e1.get(),e2.get())

tk.Button(master, text='Insert Into File', command= intoFile).grid(row=3, column=1, sticky=tk.W, pady=4)

master.mainloop()
