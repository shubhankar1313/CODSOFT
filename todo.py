import string
from tkinter import *
import tkinter.font as font

task_pos = 5

def remove_task(edit_pos):
    text1.destroy
    button_edit1.destroy()
    button_remove1.destroy()
    
def submit_edit(edit_pos):
    global button1

    text1.destroy()

    text_edit = Label(root, fg = "white", bg = "black", text = line.get(), font = font_task)
    text_edit.grid(row = edit_pos, column = 0, sticky = 'w')

    button2.destroy()

    font_button = font.Font(family = "Bell Gothic Std Black", size = 15)
    button1 = Button(root, text = "Submit", fg = "black", bg = "white", command = add_task, font = font_button)
    button1.grid(row = 3, column = 1, padx = 20)
    
def edit_task(entry, edit_pos):
    global button2

    line.set(entry)

    button1.destroy()

    font_button = font.Font(family = "Bell Gothic Std Black", size = 15)
    button2 = Button(root, text = "Edit", fg = "black", bg = "white", command = lambda: submit_edit(edit_pos), font = font_button)
    button2.grid(row = 3, column = 1, padx = 20)
    
def add_task():
    global task_pos, text1, font_task, button_edit, button_remove

    font_task = font.Font(family = "Bell Gothic Std Black", size = 15)
    locals()[f"text{task_pos-4}"] = Label(root, fg = "white", bg = "black", text = str(line.get()), font = font_task)
    locals()[f"text{task_pos-4}"].grid(row = task_pos, column = 0, sticky = 'w')

    edit_pos = task_pos-4
    font_edit = font.Font(family = "Bell Gothic Std Black", size = 15)
    locals()[f"button_edit{task_pos-4}"] = Button(root, text = "Edit", fg = "black", bg = "green", command = lambda: edit_task(edit_pos), font = font_button)
    locals()[f"button_edit{task_pos-4}"].grid(row = task_pos, column = 1, padx = 20)

    font_remove = font.Font(family = "Bell Gothic Std Black", size = 15)
    locals()[f"button_remove{task_pos-4}"] = Button(root, text = "Remove", fg = "black", bg = "red", command = lambda: remove_task(edit_pos), font = font_button)
    locals()[f"button_remove{task_pos-4}"].grid(row = task_pos, column = 2, padx = 20)
    
    line.set("")
    
    task_pos += 1
    
if __name__ == "__main__":
    root = Tk()
    root.configure(background = "black")
    root.title("To-Do List")
    root.geometry("695x358")

    font_title = font.Font(family = "Bell Gothic Std Black", size = 25, weight = "bold")
    font_title.configure(underline = True)
    title = Label(root, fg = "white", bg = "black", text = "To-Do List\n", font = font_title)
    title.grid(row = 0, column = 0)
    
    font_subtitle = font.Font(family = "Bell Gothic Std Black", size = 20)
    text_add = Label(root, fg = "white", bg = "black", text = "Add Items", font = font_subtitle)
    text_add.grid(row = 2, column = 0, sticky = 'w')


    font_line = font.Font(family = "Bell Gothic Std Black", size = 15, weight = "bold")
    line = StringVar(root)

    font_entry = font.Font(family = "Bell Gothic Std Black", size = 15)
    expression = Entry(root, textvariable = line, font = font_entry)
    expression.grid(row = 3, column = 0, ipadx = 120, ipady = 5)

    font_button = font.Font(family = "Bell Gothic Std Black", size = 15)
    button1 = Button(root, text = "Submit", fg = "black", bg = "white", command = add_task, font = font_button)
    button1.grid(row = 3, column = 1, padx = 20)

    font_subtitle = font.Font(family = "Bell Gothic Std Black", size = 20)
    text_task = Label(root, fg = "white", bg = "black", text = "\nTasks", font = font_subtitle)
    text_task.grid(row = 4, column = 0, sticky = 'w')

    root.mainloop()