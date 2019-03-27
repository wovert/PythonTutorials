import tkinter as tk


def btnHelloClicked():
    labelHello.config(text="Hello Tkinter!")


top = tk.Tk()

top.title("Button Test")

labelHello = tk.Label(top, text="Press the button...", height=5, width=20, fg="blue")

labelHello.pack()

btn = tk.Button(top, text="Hello", command=btnHelloClicked)

btn.pack()

top.mainloop()