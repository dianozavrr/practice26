import tkinter as tk

root = tk.Tk()
root.title("перша програма")
root.geometry("1024x768")

label = tk.Label(root, text="Hello, world!")
label.pack()

button = tk.Button(root, text="закрити", command=root.destroy)
button.pack()

root.mainloop()
