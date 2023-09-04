import random
import string
import pyperclip
from tkinter import *
import tkinter.font as font

to_display = ""

def generator():
    global to_display
    password = []
    n = equation1.get()
    if n > 0 and n <= 30:
        while n > 0:
            char = random.choice(["Sym", "Char", "Num"])
            if char == "Sym":
                password.append(random.choice(string.punctuation))
            elif char == "Char":
                password.append(random.choice(string.ascii_letters))
            else:
                password.append(str(random.randrange(1,9)))
            n -= 1
        to_display += "".join(password)
        equation2.set(to_display)
    else:
        equation2.set("Select range between 1 and 30!")

def reset():
    global to_display
    to_display = ""
    equation2.set(to_display)
'''
def copy():
    global to_display
    pyperclip.copy(str(to_display))
    '''

if __name__ == "__main__":
    root = Tk()
    root.configure(background = "black")
    root.title("Password Generator")
    root.geometry("695x358")

    buttonFont_entry = font.Font(family = "Bell Gothic Std Black", size = 15, weight = "bold")
    equation1 = IntVar()
    equation2 = StringVar()
    equation1.set(0)

    expression1 = Entry(root, textvariable = equation1, font = buttonFont_entry)
    expression1.grid(row = 3, column = 1, columnspan = 1, ipadx = 58, ipady = 10)

    expression2 = Entry(root, textvariable = equation2, font = buttonFont_entry)
    expression2.grid(row = 5, column = 1, columnspan = 4, ipadx = 58, ipady = 10)

    buttonFont_title = font.Font(family = "Bell Gothic Std Black", size = 20, weight = "bold")
    buttonFont_title.configure(underline = True)

    text1 = Label(root, fg = "white", bg = "black", text = "Password Generator", font = buttonFont_title, justify = "center")
    text1.grid(row = 1, column = 1)

    text_empty1 = Label(root, fg = "black", bg = "black", text = "   ", font = buttonFont_title, justify = "center")
    text_empty1.grid(row = 2, column = 1)

    text_empty2 = Label(root, fg = "black", bg = "black", text = "   ", font = buttonFont_title, justify = "center")
    text_empty2.grid(row = 4, column = 1)

    text_empty3 = Label(root, fg = "black", bg = "black", text = "   ", font = buttonFont_title, justify = "center")
    text_empty3.grid(row = 6, column = 1)

    buttonFont = font.Font(family = "Bell Gothic Std Black", size = 15, weight = "bold")

    text1 = Label(root, fg = "white", bg = "black", text = "Enter password length:", font = buttonFont)
    text1.grid(row = 3, column = 0)

    text2 = Label(root, fg = "white", bg = "black", text = "Generated password:", font = buttonFont)
    text2.grid(row = 5, column = 0)

    Button1 = Button(root, text = "Generate", fg = "black", bg = "white", command = generator, font = buttonFont)
    Button1.grid(row = 7, column = 0)

    #Button2 = Button(root, text = "Copy to Clipboard", fg = "black", bg = "white", command = lambda: 2, font = buttonFont)
    #Button2.grid(row = 7, column = 1)
    
    Button3 = Button(root, text = "Reset", fg = "black", bg = "white", command = reset, font = buttonFont)
    Button3.grid(row = 7, column = 1)


    root.mainloop()