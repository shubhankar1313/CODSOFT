import string
from tkinter import *
import tkinter.font as font

todo, data = [], ""

def remove_all():
    global data
    data = ""
    expression2.insert('end -1 chars', data)
    
def add_task():
    global todo, data, text_error

    text_error.destroy()

    if line.get() != "":
        todo.append(line.get())

        for task in todo:
            data += f"{task}\n"

        expression2.insert('end -1 chars', data)

        line.set("")
        todo, data = [], ""

    else:
        text_error = Label(root, fg = "red", bg = "black", text = "Enter task!", font = font_entry)
        text_error.grid(row = 4, column = 0, sticky = 'w', padx = 200)


if __name__ == "__main__":
    root = Tk()
    root.configure(background = "black")
    root.title("To-Do List")
    root.geometry("595x730")

    font_title = font.Font(family = "Bell Gothic Std Black", size = 25, weight = "bold")
    font_title.configure(underline = True)
    title = Label(root, fg = "white", bg = "black", text = "To-Do List\n", font = font_title)
    title.grid(row = 0, column = 0, sticky = 'w', padx = 200)
    
    font_subtitle = font.Font(family = "Bell Gothic Std Black", size = 20)
    text_add = Label(root, fg = "white", bg = "black", text = "Add Items", font = font_subtitle)
    text_add.grid(row = 2, column = 0, sticky = 'w')


    font_line = font.Font(family = "Bell Gothic Std Black", size = 15, weight = "bold")
    line = StringVar(root)

    font_entry = font.Font(family = "Bell Gothic Std Black", size = 15)
    expression1 = Entry(root, textvariable = line, font = font_entry)
    expression1.grid(row = 3, column = 0, ipadx = 120, ipady = 5, padx = 10, sticky = 'w')

    font_button = font.Font(family = "Bell Gothic Std Black", size = 15)
    button1 = Button(root, text = "Submit", fg = "black", bg = "white", command = add_task, font = font_button)
    button1.grid(row = 3, column = 0, padx = 500)

    font_subtitle = font.Font(family = "Bell Gothic Std Black", size = 20)
    text_task = Label(root, fg = "white", bg = "black", text = "\nTasks", font = font_subtitle)
    text_task.grid(row = 4, column = 0, sticky = 'w')

    todolist = StringVar(root)

    font_entry = font.Font(family = "Bell Gothic Std Black", size = 15)
    expression2 = Text(root, height = 5, width = 20, font = font_entry)
    expression2.grid(row = 5, column = 0, ipadx = 120, ipady = 150, padx = 10, sticky = 'w')

    text_error = Label(root, fg = "red", bg = "black", text = "   ", font = font_entry)
    text_error.grid(row = 4, column = 0, sticky = 'w', padx = 200)

    text_empty = Label(root, fg = "red", bg = "black", text = "   ", font = font_entry)
    text_empty.grid(row = 6, column = 0, sticky = 'w', padx = 200)

    button2 = Button(root, text = "Remove All", fg = "black", bg = "red", command = remove_all, font = font_button)
    button2.grid(row = 7, column = 0, sticky = 'w', padx = 20)

    button3 = Button(root, text = "Remove Entry:", fg = "black", bg = "red", command = remove_all, font = font_button)
    button3.grid(row = 7, column = 0, sticky = 'w', padx = 200)

    remove_entry = IntVar(root)
    expression3 = Text(root, height = 1, width = 3, font = font_entry)
    expression3.grid(row = 7, column = 0, ipadx = 1, ipady = 1, padx = 360)

    root.mainloop()

    
