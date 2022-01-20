from curses.textpad import Textbox
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image

win = Tk()
win.title("UI-4")
win.iconbitmap('icon.ico')
win.geometry('1920x1080')

#win.wm_attributes('-transparent', '#ab23ff')

'''logo = Image.open("logo.png")
logo_res = logo.resize(70, 70)
img = Label(win, image=logo).place(x=10, y=30)'''

filename = PhotoImage(file = "gradnew.png")
background_label = Label(win, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


head1 = Label(win, text="Rantify", font=("Lovelo", 40, "bold")).pack()
head2 = Label(win, text="The Music You Like", font=("Roboto", 30, "italic")).pack()

rt = Label(win, text="Title", font=("", 30)).place(x = 300, y = 160)
e1 = Entry(win, font=('',20)).place(x = 370, y = 165, width=500, height=37)

rant = Label(win, text="RANT:", font=("", 27)).place(x = 300, y = 220) 

rant_text = ScrolledText(win, height = 10, width = 50)
rant_text.place(x = 305, y = 280)
rant_text.configure(font=("",20))
rant_text.insert("1.0", "Type Here...")

but1 = Button(win, text="I Am Done!",font=("", 25)).place(x = 850, y = 550)


win.mainloop()