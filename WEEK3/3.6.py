import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("блокнот")
root.geometry("400x300")

changed = False

def mark_change(event):
    global changed
    changed = True
    text.edit_modified(False)

def open_file():
    global changed
    path = filedialog.askopenfilename(filetypes=[("txt", "*.txt")])
    if not path: return
    try:
        text.delete("1.0", tk.END)
        text.insert("1.0", open(path, encoding="utf-8").read())
        changed = False
    except:
        messagebox.showerror("помилка", "не вдалося відкрити файл")

def save_file():
    global changed
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not path: return
    try:
        open(path, "w", encoding="utf-8").write(text.get("1.0", tk.END))
        changed = False
    except:
        messagebox.showerror("помилка", "не вдалося зберегти файл")

def exit_app():
    if changed:
        if not messagebox.askyesno("увага", "є незбережені зміни. вийти?"):
            return
    root.destroy()

text = tk.Text(root)
text.pack(expand=True, fill="both")
text.bind("<<Modified>>", mark_change)

menu = tk.Menu(root)
root.config(menu=menu)

m = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="файл", menu=m)
m.add_command(label="відкрити", command=open_file)
m.add_command(label="зберегти", command=save_file)
m.add_command(label="вийти", command=exit_app)

root.protocol("WM_DELETE_WINDOW", exit_app)
root.mainloop()
