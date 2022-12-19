#
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text='Label Clássico Tkinter').pack()
ttk.Label(root, text='Label Tema do Ttk').pack()

root.mainloop()
