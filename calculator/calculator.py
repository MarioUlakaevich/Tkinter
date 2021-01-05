from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from math import sqrt

root = Tk()
root.title("Calculator")

#Calculator Logic
def calc(key):
    if key == "=":
#avoid letters. Only numbers
        strl = "+-1234567890.*/"
        if calc_entry.get()[0] not in strl:
            calc_entry.insert(END, "Not a Number")
            messagebox.showerror("Error!", "Put a number!")
#calculation
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "="+str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the values!")
#clean input field
    elif key == "C":
        calc_entry.delete(0, END)
#switch + and -
    elif key == "+/-":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "sqrt":
        result = sqrt(int(calc_entry.get()))
        calc_entry.insert(END, "="+str(result))
    elif key == "del":
        length = len(calc_entry.get())
        calc_entry.delete(length-1)
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


# create all buttons
btn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "+/-", "=",
    "0", ".", "C", "sqrt", "del"
]

r = 1
c = 0

for i in btn_list:
    rel = ''
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c+=1
    if c>4:
        c = 0
        r += 1

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()
