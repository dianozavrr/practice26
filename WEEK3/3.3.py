import tkinter as tk

root = tk.Tk()
root.title("анкета")
root.geometry("300x200")

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
tk.Label(root, text="Ім'я:").grid(row=0, column=0)

sex = tk.StringVar()
tk.Radiobutton(root, text="чоловіча", variable=sex, value="Чоловіча").grid(row=1, column=0)
tk.Radiobutton(root, text="жіноча", variable=sex, value="Жіноча").grid(row=1, column=1)

agree = tk.BooleanVar()
tk.Checkbutton(root, text="погоджуюсь", variable=agree).grid(row=2, column=0, columnspan=2)

info = tk.Label(root, text="")
info.grid(row=4, column=0, columnspan=2, pady=10)

def save():
    if agree.get():
        info.config(text=f"ім'я: {name_entry.get()}\nСтать: {sex.get()}")

tk.Button(root, text="зберегти", command=save).grid(row=3, column=0, columnspan=2)

root.mainloop()
