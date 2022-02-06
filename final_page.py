from curses.textpad import Textbox
from this import d
from tkinter.font import Font
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from turtle import width
from PIL import ImageTk, Image
import webbrowser
from ranting_page import dummy


win = Tk()
win.title("UI-Final")
win.geometry('1920x1080')


def rant():
        from ranting_page import dummy
        dummy()
        pred= dummy()
        if pred == 1:
                canvas1 = Canvas(win, width=1920, height=1080, bd=0, highlightthickness=0, relief='ridge')
                canvas1.place(x=0, y=0)
                mg = PhotoImage(file="finalpage_bg.png")
                canvas1.create_image(0, 0, anchor=NW, image=mg)

                #-----------------------------------------------------------------------------------------------------------
                # logo
                canvas = Canvas(win, width=39, height=39)
                canvas.place(x=3, y=3)
                i = PhotoImage(file="logo.png")
                canvas.create_image(1, 1, anchor=NW, image=i)
                canvas1.create_text(130,27,text='Rantify',font=("Kollektif", 30),fill='black')
                
                
                #-----------------------------------------------------------------------------------------------------------   
                canvas1.create_text(450, 180, text="Looks like you're in a good mood.... \nLet's help you keep it that way",font=("Comic Sans", 28), fill='white')

                canvas1.create_text(
                        630, 320, text="PlayLists For You To Choose From", font=("", 25), fill='white')

                def callback(url):
                        webbrowser.open_new_tab(url)


                

                l1 = Label(win, text="Motivated", font=('Courier', 28),
                                fg="blue", bg='black', cursor="hand2")
                l1.place(x=180, y=430)
                l1.bind("<Button-1>", lambda e:
                        callback("https://www.youtube.com/watch?v=U1UtRnGn5hc"))


                l1 = Label(win, text="In Love", font=('Courier', 28),
                        fg="white", bg='#748EFF', cursor="hand2")
                l1.place(x=420, y=430)
                l1.bind("<Button-1>", lambda e:
                        callback("https://www.youtube.com/watch?v=U1UtRnGn5hc"))


                l1 = Label(win, text="Just Happy", font=('Courier', 28),
                                fg="white", bg='black', cursor="hand2")
                l1.place(x=650, y=430)
                l1.bind("<Button-1>", lambda e:
                        callback("https://www.youtube.com/watch?v=U1UtRnGn5hc"))

                l1 = Label(win, text="Wanna Vibe", font=('Courier', 28),
                        fg="white", bg='black', cursor="hand2")
                l1.place(x=900, y=430)
                l1.bind("<Button-1>", lambda e:
                        callback("https://www.youtube.com/watch?v=U1UtRnGn5hc"))

        else:
                canvas1 = Canvas(win, width=1920, height=1080, bd=0,
                                highlightthickness=0, relief='ridge')
                canvas1.place(x=0, y=0)
                mg = PhotoImage(file="finalpage_bg.png")
                canvas1.create_image(0, 0, anchor=NW, image=mg)

                # logo
                canvas = Canvas(win, width=39, height=39)
                canvas.place(x=3, y=3)
                i = PhotoImage(file="logo.png")
                canvas.create_image(1, 1, anchor=NW, image=i)

                
                canvas1.create_text(130,27,text='Rantify',font=("Kollektif", 30),fill='black')
                
                
                canvas1.create_text(510, 110, text="Looks like you are feeling sad....🙁 \nLet's embrace it, shall we? ",font=("Comic Sans", 28), fill='white')


                def callback(url):
                        webbrowser.open_new_tab(url)

                canvas1.create_text(650, 320, text="PlayLists For You To Choose From", font=("", 25), fill='white')

                l1 = Label(win, text="Melancholic", font=('Courier', 28),
                        fg="white", bg='black', cursor="hand2")
                l1.place(x=230, y=430)
                l1.bind("<Button-1>", lambda e:
                        callback("https://www.youtube.com/watch?v=U1UtRnGn5hc"))

                l1 = Label(win, text="Motivated", font=('Courier', 28),
                        fg="white", bg='black', cursor="hand2")
                l1.place(x=580, y=430)
                l1.bind("<Button-1>", lambda e:
                        callback("https://www.youtube.com/watch?v=U1UtRnGn5hc"))

                l1 = Label(win, text="Wanna Vibe", font=('Courier', 28),
                        fg="white", bg='black', cursor="hand2")
                l1.place(x=940, y=430)
                l1.bind("<Button-1>", lambda e:
                        callback("https://www.youtube.com/watch?v=U1UtRnGn5hc"))

def nextPage():
        win.destroy()
        import forum

rant()

rbutton=Button(win,text='yes',command=nextPage).place(x=100,y=100)   
win.mainloop()
