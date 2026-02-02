import tkinter as tk

root = tk.Tk()
root.title("калькулятор")

e1 = tk.Entry(root); e1.grid(row=0, column=0)
e2 = tk.Entry(root); e2.grid(row=0, column=1)
res = tk.Label(root, text=""); res.grid(row=2, column=0, columnspan=2)

def c(o):
    try:
        a, b = float(e1.get()), float(e2.get())
        if o == "+": r = a + b
        elif o == "-": r = a - b
        elif o == "*": r = a * b
        else: r = "помилка" if b == 0 else a / b
    except:
        r = "помилка"
    res.config(text=r)

for i, op in enumerate(["+", "-", "*", "/"]):
    tk.Button(root, text=op, command=lambda o=op: c(o)).grid(row=1, column=i)

root.mainloop()
