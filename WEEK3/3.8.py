import tkinter as tk
from tkinter import colorchooser, filedialog

color = "black"
mode = "line"
start_x = start_y = None

def choose_color():
    global color
    c = colorchooser.askcolor()[1]
    if c: color = c

def clear_canvas():
    canvas.delete("all")

def save_canvas():
    path = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript files","*.ps")])
    if path: canvas.postscript(file=path)

def toggle_mode():
    global mode
    mode = "circle" if mode=="line" else "line"
    mode_button.config(text=f"Режим: {'Коло' if mode=='circle' else 'Лінія'}")

def start_draw(e):
    global start_x, start_y
    start_x, start_y = e.x, e.y
    if mode=="circle":
        r=10
        canvas.create_oval(e.x-r,e.y-r,e.x+r,e.y+r,fill=color,outline=color)

def draw(e):
    global start_x, start_y
    if mode=="line" and start_x is not None:
        canvas.create_line(start_x,start_y,e.x,e.y,fill=color,width=2)
        start_x, start_y = e.x, e.y

root = tk.Tk()
root.title("Графіка")

tk.Button(root,text="Вибрати колір",command=choose_color).pack(side="left",padx=5,pady=5)
tk.Button(root,text="Очистити",command=clear_canvas).pack(side="left",padx=5,pady=5)
tk.Button(root,text="Зберегти",command=save_canvas).pack(side="left",padx=5,pady=5)
mode_button = tk.Button(root,text="Режим: Лінія",command=toggle_mode)
mode_button.pack(side="left",padx=5,pady=5)

canvas = tk.Canvas(root,width=600,height=400,bg="white")
canvas.pack()
canvas.bind("<ButtonPress-1>",start_draw)
canvas.bind("<B1-Motion>",draw)

root.mainloop()
