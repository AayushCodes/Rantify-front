from curses.textpad import Textbox
from tkinter import *
from tkinter.scrolledtext import ScrolledText

win = Tk()

win.geometry('500x450')


head1 = Label(win, text="Rantify", font=("Lovelo", 20, "bold")).pack()
head2 = Label(win, text="The Music You Like", font=("Roboto", 15, "italic")).pack()

rt = Label(win, text="Title").place(x = 40, y = 70)
e1 = Entry(win).place(x = 80, y = 70)

rant = Label(win, text="RANT:").place(x = 40, y = 100) 


rant_text = ScrolledText(win, height = 10, width = 50)
rant_text.place(x = 40, y = 130)
rant_text.insert("1.0", "Type Here...")

but1 = Button(win, text="I Am Done!").place(x = 320, y = 280)


win.mainloop()