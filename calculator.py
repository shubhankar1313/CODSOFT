from tkinter import *
import tkinter.font as font

line = ""

def press(num):
    global line
    line += str(num)
    equation.set(line)

def ac():
    global line
    line = ""
    equation.set(line)

def ce():
    global line
    line = line[0:-1]
    equation.set(line)

def pressequal():
    try:
        global line
        line = str(eval(line))
        equation.set(str(eval(line)))
    except:
        equation.set("ERROR")
        line = ""

if __name__ == "__main__":

    root = Tk()
    root.configure(background = "black")
    root.title("Calculator")
    root.geometry("695x358")

    buttonFont_entry = font.Font(family = "Bell Gothic Std Black", size = 20, weight = "bold")
    equation = StringVar()
    expression = Entry(root, textvariable = equation, font = buttonFont_entry)
    expression.grid(columnspan = 4, ipadx = 195, ipady = 20)

    buttonFont = font.Font(family = "Bell Gothic Std Black", size = 20, weight = "bold")

    button1 = Button(root, text = '1', fg = 'black', bg = 'white', command = lambda: press(1), height = 1, width = 1, font = buttonFont)
    button1.grid(row = 2, column = 0, sticky = 'nsew')

    button2 = Button(root, text = '2', fg = 'black', bg = 'white', command = lambda: press(2), height = 1, width = 1, font = buttonFont)
    button2.grid(row = 2, column = 1, sticky = 'nsew')

    button3 = Button(root, text = '3', fg = 'black', bg = 'white', command = lambda: press(3), height = 1, width = 1, font = buttonFont)
    button3.grid(row = 2, column = 2, sticky = 'nsew')

    button4 = Button(root, text = '4', fg = 'black', bg = 'white', command = lambda: press(4), height = 1, width = 1, font = buttonFont)
    button4.grid(row = 3, column = 0, sticky = 'nsew')

    button5 = Button(root, text = '5', fg = 'black', bg = 'white', command = lambda: press(5), height = 1, width = 1, font = buttonFont)
    button5.grid(row = 3, column = 1, sticky = 'nsew')

    button6 = Button(root, text = '6', fg = 'black', bg = 'white', command = lambda: press(6), height = 1, width = 1, font = buttonFont)
    button6.grid(row = 3, column = 2, sticky = 'nsew')

    button1 = Button(root, text = '1', fg = 'black', bg = 'white', command = lambda: press(1), height = 1, width = 1, font = buttonFont)
    button1.grid(row = 4, column = 0, sticky = 'nsew')

    button8 = Button(root, text = '8', fg = 'black', bg = 'white', command = lambda: press(8), height = 1, width = 1, font = buttonFont)
    button8.grid(row = 4, column = 1, sticky = 'nsew')

    button9 = Button(root, text = '9', fg = 'black', bg = 'white', command = lambda: press(9), height = 1, width = 1, font = buttonFont)
    button9.grid(row = 4, column = 2, sticky = 'nsew')

    button0 = Button(root, text = '0', fg = 'black', bg = 'white', command = lambda: press(0), height = 1, width = 1, font = buttonFont)
    button0.grid(row = 5, column = 0, sticky = 'nsew')

    plus = Button(root, text = '+', fg = 'black', bg = 'gray80', command = lambda: press('+'), height = 1, width = 1, font = buttonFont)
    plus.grid(row = 2, column = 3, sticky = 'nsew')

    minus = Button(root, text = '-', fg = 'black', bg = 'gray80', command = lambda: press('-'), height = 1, width = 1, font = buttonFont)
    minus.grid(row = 3, column = 3, sticky = 'nsew')

    multiply = Button(root, text = 'x', fg = 'black', bg = 'gray80', command = lambda: press('*'), height = 1, width = 1, font = buttonFont)
    multiply.grid(row = 4, column = 3, sticky = 'nsew')

    divide = Button(root, text = '÷', fg = 'black', bg = 'gray80', command = lambda: press('/'), height = 1, width = 1, font = buttonFont)
    divide.grid(row = 5, column = 3, sticky = 'nsew')

    equal = Button(root, text = '=', fg = 'black', bg = 'cornflowerblue', command = pressequal, height = 1, width = 1, font = buttonFont)
    equal.grid(row = 5, column = 2, sticky = 'nsew')

    decimal = Button(root, text = '.', fg = 'black', bg = 'white', command = lambda: press('.'), height = 1, width = 1, font = buttonFont)
    decimal.grid(row = 5, column = 1, sticky = 'nsew')

    rbracket = Button(root, text = '(', fg = 'black', bg = 'gray80', command = lambda: press('('), height = 1, width = 1, font = buttonFont)
    rbracket.grid(row = 6, column = 0, sticky = 'nsew')

    lbracket = Button(root, text = ')', fg = 'black', bg = 'gray80', command = lambda: press(')'), height = 1, width = 1, font = buttonFont)
    lbracket.grid(row = 6, column = 1, sticky = 'nsew')

    ce = Button(root, text = 'CE', fg = 'black', bg = 'gray80', command = ce, height = 1, width = 1, font = buttonFont)
    ce.grid(row = 6, column = 2, sticky = 'nsew')

    ac = Button(root, text = 'AC', fg = 'black', bg = 'gray80', command = ac, height = 1, width = 1, font = buttonFont)
    ac.grid(row = 6, column = 3, sticky = 'nsew')

    root.mainloop()