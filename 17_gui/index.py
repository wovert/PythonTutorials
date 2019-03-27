import tkinter as tk

# 建立tkinter窗口，设置窗口标题
top = tk.Tk()

top.title("Hello Test")

# 在窗口中创建标签

labelHello = tk.Label(top, text="Hello Tkinter!")

labelHello.pack()

# 运行并显示窗口

top.mainloop()