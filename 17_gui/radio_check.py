import tkinter as tk


def colorChecked():
    labelHello.config(fg=color.get())


def typeChecked():
    textType = typeBlod.get() + typeItalic.get()

    if textType == 1:

        labelHello.config(font=("Arial", 12, "bold"))

    elif textType == 2:

        labelHello.config(font=("Arial", 12, "italic"))

    elif textType == 3:

        labelHello.config(font=("Arial", 12, "bold italic"))

    else:

        labelHello.config(font=("Arial", 12))


top = tk.Tk()

top.title("Radio & Check Test")

labelHello = tk.Label(top, text="Check the format of text.", height=3, font=("Arial", 12))

labelHello.pack()

color = tk.StringVar()

tk.Radiobutton(top, text="Red", variable=color, value="red", command=colorChecked).pack(side=tk.LEFT)

tk.Radiobutton(top, text="Blue", variable=color, value="blue", command=colorChecked).pack(side=tk.LEFT)

tk.Radiobutton(top, text="Green", variable=color, value="green", command=colorChecked).pack(side=tk.LEFT)

typeBlod = tk.IntVar()

typeItalic = tk.IntVar()

tk.Checkbutton(top, text="Blod", variable=typeBlod, onvalue=1, offvalue=0, command=typeChecked).pack(side=tk.LEFT)

tk.Checkbutton(top, text="Italic", variable=typeItalic, onvalue=2, offvalue=0, command=typeChecked).pack(side=tk.LEFT)

top.mainloop()