import tkinter as tk
import logic

class App:
    def __init__(self, root):
        self.root = root
        root.title("Demo")

        self.e1 = tk.Entry(root)
        self.e2 = tk.Entry(root)
        self.e1.pack()
        self.e2.pack()

        self.btn = tk.Button(root, text="додати", command=self.calculate)
        self.btn.pack()

        self.result = tk.Label(root, text="")
        self.result.pack()

    def calculate(self):
        a = self.e1.get()
        b = self.e2.get()
        r = logic.add(a, b)
        self.result.config(text=r)
