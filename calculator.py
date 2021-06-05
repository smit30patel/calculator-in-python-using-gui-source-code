from tkinter import *

"""
    @author = smit_patel
"""
#source code for calculator in python using gui

root = Tk()
root.title("smart smit's calculator")
e = Entry(root, width=35, bg="white", fg="black")
e.grid(row=0, column=0, columnspan=3)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, int(f_num / int(second_number)))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, bg="white", command=lambda : button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="white", command=lambda : button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="white", command=lambda : button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="white", command=lambda : button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="white", command=lambda : button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="white", command=lambda : button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="white", command=lambda : button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="white", command=lambda : button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="white", command=lambda : button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="white", command=lambda : button_click(0))
button_00 = Button(root, text="00", padx=36, pady=20, bg="white", command=lambda : button_click(00))

button_clear = Button(root, text="clear", padx=28, pady=20, bg="red", command=button_clear)
button_equal = Button(root, text="=", padx=86, pady=20, bg="white", command=button_equal)
button_add = Button(root, text="+", padx=38, pady=20, bg="yellow", command=button_add)
button_sub = Button(root, text="-", padx=41, pady=20, bg="green", command=button_sub)
button_mul = Button(root, text="*", padx=41, pady=20, bg="pink", command=button_mul)
button_div = Button(root, text="/", padx=41, pady=20, bg="orange", command=button_div)

button_9.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=0)

button_6.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)

button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=0)

button_0.grid(row=4, column=0)
button_00.grid(row=4, column=1)
button_clear.grid(row=4, column=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()