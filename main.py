from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle


def enter(event):
    lista.insert(END, entry.get())
    entry.delete(0, END)


def add():
    item = entry.get()
    lista.insert(END, item)
    entry.delete(0, END)


def remove():
    lista.delete(ANCHOR)


def cross_item():
    lista.itemconfig(lista.curselection(), fg="#dedede")
    lista.selection_clear(0, END)


def uncross_item():
    lista.itemconfig(lista.curselection(), fg="black")
    lista.selection_clear(0, END)


def save_list():
    file_name = filedialog.asksaveasfilename(
        title="Save file", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f"{file_name}.dat"

    # grab all the stuff from the list
    stuff = lista.get(0, END)

    # open the file
    output_file = open(file_name, "wb")  # wb means write binary

    # adding the stuff to the file
    pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(title="Open file", filetypes=(
        ("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:

        # delete currently open list
        lista.delete(0, END)

        # open the file
        input_file = open(file_name, "rb")  # rb means write binary

        # load the stuff from the file
        stuff = pickle.load(input_file)

        # output stuff on the screen
        for item in stuff:
            lista.insert(END, item)


def clear_list():
    lista.delete(0, END)


# ____________________________________________________________________________________
window = Tk()
window.minsize(500, 600)
window.config(pady=10)
window.title("To-Do List")

# create menu
my_menu = Menu(window)
window.config(menu=my_menu)

# add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# add drop down items
file_menu.add_command(label="Save list", command=save_list)
file_menu.add_command(label="Open list", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear list", command=clear_list)

my_font = Font(family="Arial", size=20, weight="bold")

my_frame = Frame(window)
my_frame.pack()

lista = Listbox(my_frame, font=my_font, width=30, height=12, highlightthickness=0,
                selectbackground="#a6a6a6", activestyle=None)
lista.pack(side="left", fill="both")


my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side="right", fill="both")

lista.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=lista.yview)

entry = Entry(width=30, font=("Arial", 20))
entry.place(x=14, y=420)

entry.bind("<Return>", enter)

add_to_list = Button(text="ADD", width=15, command=add)
remove_from_list = Button(text="REMOVE", width=15, command=remove)
cross = Button(text="CROSS", width=15, command=cross_item)
uncross = Button(text="UNCROSS", width=15, command=uncross_item)

add_to_list.place(x=12, y=470)
remove_from_list.place(x=130, y=470)
cross.place(x=250, y=470)
uncross.place(x=370, y=470)

window.mainloop()
