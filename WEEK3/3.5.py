import tkinter as tk
from tkinter import ttk, colorchooser
import os

FILE = "color.txt"

def load_color():
    if os.path.exists(FILE):
        return open(FILE).read().strip()
    return "#ffffff"

def save_color(c):
    open(FILE, "w").write(c)

root = tk.Tk()
root.title("Notebook")
root.geometry("300x200")

bg = load_color()

nb = ttk.Notebook(root)
nb.pack(expand=True, fill="both")

tab1 = tk.Frame(nb, bg=bg)
tab2 = tk.Frame(nb, bg=bg)
tab3 = tk.Frame(nb, bg=bg)

nb.add(tab1, text="головна")
nb.add(tab2, text="налаштування")
nb.add(tab3, text="про програму")

tk.Label(tab1, text="введіть дані:", bg=bg).pack()
tk.Entry(tab1).pack(pady=10)

def choose():
    global bg
    c = colorchooser.askcolor()[1]
    if c:
        bg = c
        tab1.config(bg=c)
        tab2.config(bg=c)
        tab3.config(bg=c)
        save_color(c)

tk.Button(tab2, text="обрати колір фону", command=choose).pack(pady=20)

tk.Label(tab3, text="автор: Я :) ", bg=bg).pack(pady=20)

root.mainloop()

