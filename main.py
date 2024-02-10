from tkinter import *
from tkinter import filedialog, ttk, messagebox
import time

root = Tk()
root.title("Disappearing Text App")
root.geometry(("1200x700+250+250"))
root.typing = Text(root)
root.typing.config(font=("Arial", 18, "bold"))
root.typing.pack(expand=True, fill='both')

timer = 0


def key_press(event):
    global timer
    print("Key pressed:", event.keysym)
    timer = 0
    return True


def increase_timer():
    global timer
    timer += 1
    print(timer)
    if timer >= 5:
        root.typing.config(fg="orange")
    if timer >= 8:
        root.typing.config(fg="red")
    if timer >= 11:
        root.typing.delete(1.0, END)
        root.typing.config(fg="black")
    root.after(1000, increase_timer)


root.bind("<Key>", key_press)

if __name__ == "__main__":
    root.after(1000, increase_timer)
    root.mainloop()