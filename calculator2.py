import tkinter as tk
from tkinter import *

root = tk.Tk()

def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

def button_click_clear():
    entry.delete(0,END)

def button_eqal():
    second_number = entry.get()
    entry.delete(0,END)

    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    elif math == "minus":
        entry.insert(0,f_num - int(second_number))
    elif math == "devide":
        entry.insert(0,f_num / int(second_number))
    elif math == "multiply":
        entry.insert(0,f_num * int(second_number))



def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0,END)
    
def button_minus():
    first_number = entry.get()
    global f_num
    global math
    math = "minus"
    f_num = int(first_number)
    entry.delete(0,END)

def button_devide():
    first_number = entry.get()
    global f_num
    global math
    math = "devide"
    f_num = int(first_number)
    entry.delete(0,END)


def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    entry.delete(0,END)

entry = Entry(root, width = 35)

b1 =Button(root, text="1", width=5,height=4,command= lambda : button_click(1))
b2 =Button(root, text="2", width=5,height=4,command= lambda : button_click(2))
b3 =Button(root, text="3", width=5,height=4,command= lambda : button_click(3))
b4 =Button(root, text="4", width=5,height=4,command= lambda : button_click(4))
b5 =Button(root, text="5", width=5,height=4,command= lambda : button_click(5))
b6 =Button(root, text="6", width=5,height=4,command= lambda : button_click(6))
b7 =Button(root, text="7", width=5,height=4,command= lambda : button_click(7))
b8 =Button(root, text="8", width=5,height=4,command= lambda : button_click(8))
b9 =Button(root, text="9", width=5,height=4,command= lambda : button_click(9))
b0 =Button(root, text="0", width=5,height=4,command= lambda : button_click(0))

b10 =Button(root, text="+", width=5,height=4,command = button_add)
b11 =Button(root, text="-", width=5,height=4,command = button_minus)
b12 =Button(root, text="*", width=5,height=4,command = button_multiply)
b13 =Button(root, text="/", width=5,height=4,command = button_devide)
b14 =Button(root, text="=", width=14,height=4,command=button_eqal)
b15 =Button(root, text="C", width=5,height=4,command = button_click_clear)





entry.grid(row=0,columnspan=4)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)

b10.grid(row=1,column=3)
b11.grid(row=2,column=3)
b12.grid(row=3,column=3)
b13.grid(row=4,column=3)

b14.grid(row=4,columnspan=2)
b15.grid(row=4,column=2)


root.mainloop()

 
