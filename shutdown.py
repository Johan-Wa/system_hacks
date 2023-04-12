import os
import time
from tkinter import *
from tkinter import ttk


if int(time.strftime('%H')) < 2:
    text='Apagando'
    command = 'shutdown -h now'
else:
    text='Apagar a la media noche'
    command = 'shutdown -h 00:00'

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=text, font=('Helvetica', 38), foreground='red').grid(column=0, row=0)
root.after(5000,root.destroy)
root.mainloop()
os.system(command)
    