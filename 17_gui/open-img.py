import tkinter as tk
from PIL import Image, ImageTk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=300)
        self.pack()
        self.pilImage = Image.open("R9.jpg")
        self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
        self.label = tk.Label(self, image=self.tkImage)
        self.label.pack()

    def processEvent(self, event):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()