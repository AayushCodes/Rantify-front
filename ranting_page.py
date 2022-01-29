from curses.textpad import Textbox
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image

win = Tk()
win.title("UI-4")
win.iconbitmap('icon.ico')
win.geometry('1920x1080')

#win.wm_attributes('-transparent', '#ab23ff')


'''filename = PhotoImage(file = "gradnew.png")
background_label = Label(win, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)'''

#bg 
canvas1 = Canvas(win, width = 1920, height = 1080, bd=0, highlightthickness=0, relief='ridge')
canvas1.place(x=0,y=0)
mg = PhotoImage(file="GRADNEW2 (1).png")
canvas1.create_image(0,0, anchor=NW, image=mg)

#logo
canvas = Canvas(win, width = 39, height = 39)
canvas.place(x=3,y=3)
img = PhotoImage(file="ewlog.png")
canvas.create_image(1,1, anchor=NW, image=img)

#head1 = Label(win, text="Rantify", font=("Lovelo", 40, "bold")).pack()
canvas1.create_text(645,25,text='Rantify',font=("Lovelo", 40, "bold"),fill='black')
#head2 = Label(win, text="The Music You Like", font=("Roboto", 30, "italic")).pack()
canvas1.create_text(645,70,text="The Music You Like", font=("Roboto", 30, "italic"),fill ='black')


#rt = Label(win, text="Title", font=("", 30)).place(x = 300, y = 160)
canvas1.create_text(332, 180, text="Title:", fill='black', font=("", 30))
e1 = Entry(win, font=('',20)).place(x = 370, y = 165, width=500, height=37)

#rant = Label(win, text="RANT:", font=("", 27)).place(x = 300, y = 220) 
canvas1.create_text(338, 255, text="Rant:", fill='black', font=("", 27))

check = True

def temp_text(e):
   global check
   if check:
      check = False
      rant_text.delete("1.0","end")
      rant_text.configure(font=("",20), fg='black')
   
rant_text = ScrolledText(win, height = 10, width = 50)
rant_text.place(x = 305, y = 280)
rant_text.configure(font=("",20, "italic"), fg='grey')
rant_text.insert("1.0", "Type Here...")
rant_text.bind("<FocusIn>", temp_text)

but1 = Button(win, text="I Am Done!",font=("", 25)).place(x = 850, y = 550)


win.mainloop()