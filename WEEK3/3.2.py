import tkinter as tk

root = tk.Tk()
root.title("привітання")
root.geometry("400x200")

label = tk.Label(root, text="")
label.pack(pady=20)

def greet():
    label.config(text="вітаю, користувач!")

def clear():
    label.config(text="")

btn_greet = tk.Button(root, text="привітати", command=greet)
btn_greet.pack()

btn_clear = tk.Button(root, text="очистити", command=clear)
btn_clear.pack()

btn_exit = tk.Button(root, text="вийти", command=root.destroy)
btn_exit.pack(pady=10)

root.mainloop()
