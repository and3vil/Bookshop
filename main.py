#Importing tkinter for window interaction
from tkinter import *

#Title of the project
window = Tk()
window.wm_title("Bookshop")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l1 = Label(window, text="Author")
l1.grid(row=0, column=2)

l1 = Label(window, text="Year")
l1.grid(row=1, column=0)

l1 = Label(window, text="ISBN")
l1.grid(row=1, column=2)

title_text = StringVar()
ent1 = Entry(window, textvariable = title_text)
ent1.grid(row=0, column=1)

author_text = StringVar()
ent2 = Entry(window, textvariable = title_text)
ent2.grid(row=0, column=3)

year_text = StringVar()
ent3 = Entry(window, textvariable = title_text)
ent3.grid(row=1, column=1)

isbn_text = StringVar()
ent4 = Entry(window, textvariable = title_text)
ent4.grid(row=1, column=3)

listb = Listbox(window, height=6, width=35)
listb.grid(row=2, column=0, rowspan=6, columnspan=2)


sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

listb.configure(yscrollcommand=sb.set)
sb.configure(command=listb.yview)

b1 = Button(window, text='view all', width=12)
b1.grid(row=2, column=3)

b1 = Button(window, text='Search entry', width=12)
b1.grid(row=3, column=3)

b1 = Button(window, text='Add entry', width=12)
b1.grid(row=4, column=3)

b1 = Button(window, text='Update Selected', width=12)
b1.grid(row=5, column=3)

b1 = Button(window, text='Delete Selected', width=12)
b1.grid(row=6, column=3)

b1 = Button(window, text='Close', width=12)
b1.grid(row=7, column=3)



window.mainloop()
