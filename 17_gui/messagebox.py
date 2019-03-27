import tkinter as tk

from tkinter import messagebox as msgbox


def btn1_clicked():
    msgbox.showinfo("Info", "Showinfo test.")


def btn2_clicked():
    msgbox.showwarning("Warning", "Showwarning test.")


def btn3_clicked():
    msgbox.showerror("Error", "Showerror test.")


def btn4_clicked():
    msgbox.askquestion("Question", "Askquestion test.")


def btn5_clicked():
    msgbox.askokcancel("OkCancel", "Askokcancel test.")


def btn6_clicked():
    msgbox.askyesno("YesNo", "Askyesno test.")


def btn7_clicked():
    msgbox.askretrycancel("Retry", "Askretrycancel test.")


top = tk.Tk()

top.title("MsgBox Test")

btn1 = tk.Button(top, text="showinfo", command=btn1_clicked)

btn1.pack(fill=tk.X)

btn2 = tk.Button(top, text="showwarning", command=btn2_clicked)

btn2.pack(fill=tk.X)

btn3 = tk.Button(top, text="showerror", command=btn3_clicked)

btn3.pack(fill=tk.X)

btn4 = tk.Button(top, text="askquestion", command=btn4_clicked)

btn4.pack(fill=tk.X)

btn5 = tk.Button(top, text="askokcancel", command=btn5_clicked)

btn5.pack(fill=tk.X)

btn6 = tk.Button(top, text="askyesno", command=btn6_clicked)

btn6.pack(fill=tk.X)

btn7 = tk.Button(top, text="askretrycancel", command=btn7_clicked)

btn7.pack(fill=tk.X)

top.mainloop()