import tkinter as tk


def drawCircle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


top = tk.Tk()

top.title("Canvas Test")

cvs = tk.Canvas(top, width=600, height=400)

cvs.pack()

cvs.create_line(50, 50, 50, 300)

cvs.create_line(100, 50, 200, 300, fill="red", dash=(4, 4), arrow=tk.LAST)

cvs.create_rectangle(200, 50, 400, 200, fill="blue")

cvs.create_oval(450, 50, 550, 200, fill="green")

drawCircle(cvs, 450, 300, 50, fill="red")

cvs.create_polygon(200, 250, 350, 250, 350, 350, 220, 300, fill="yellow")

top.mainloop()

