from curses.textpad import Textbox
from re import L
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from turtle import width
from PIL import ImageTk, Image
import webbrowser
#from tkHyperLinkManager import HyperlinkManager

win = Tk()
win.title("UI-Final")
win.geometry('1920x1080')

#bg 
canvas1 = Canvas(win, width = 1920, height = 1080, bd=0, highlightthickness=0, relief='ridge')
canvas1.place(x=0,y=0)
mg = PhotoImage(file="GRADNEW2 (1).png")
canvas1.create_image(0,0, anchor=NW, image=mg)

#logo
canvas = Canvas(win, width = 39, height = 39)
canvas.place(x=3,y=3)
i = PhotoImage(file="ewlog.png")
canvas.create_image(1,1, anchor=NW, image=i)

#head1 = Label(win, text="Rantify", font=("Lovelo", 40, "bold")).pack()
canvas1.create_text(645,25,text='Rantify',font=("Lovelo", 40, "bold"),fill='white')
#head2 = Label(win, text="The Music You Like", font=("Roboto", 30, "italic")).pack()
canvas1.create_text(645,65,text="The Music You Like", font=("Roboto", 30, "italic"),fill ='white')
#head3 = Label(win, text="HMM......Feeling Better", font=("Comic Sans", 20)).place(x = 250, y = 150)
canvas1.create_text(343, 180, text="HMM......Feeling Better", font=("Comic Sans", 20), fill='white')
#head4 = Label(win, text="Here's Your Personalized Spotify Playlist",font=("", 20)).place(x = 250, y = 200)
canvas1.create_text(420, 220,text="Here's Your Personalized Spotify Playlist",font=("", 20), fill='white')


def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = Label(win, text="Click Me",font=('Helveticabold', 25), fg="yellow",bg='#295464', cursor="hand2")
link.place(x = 250, y = 270)
link.bind("<Button-1>", lambda e:
callback("https://www.youtube.com/watch?v=LIIDh-qI9oI"))

canvas1.create_text(440, 340, text="Few Articles You Might Want To Checkout.. ",font=("", 20), fill='white')

#ar1
img1 = Image.open('ar1.png')
rimg1 = ImageTk.PhotoImage(img1)
l1= Label(win, image=rimg1, cursor="hand2")
l1.place(x = 260, y = 400)
l1.bind("<Button-1>", lambda e:
callback("https://www.youtube.com/watch?v=LIIDh-qI9oI"))

#ar2
img2 = Image.open('ar1.png')
rimg2 = ImageTk.PhotoImage(img2)
l2= Label(win, image=rimg2, cursor="hand2")
l2.place(x = 600, y = 400)
l2.bind("<Button-1>", lambda e:
callback("https://www.youtube.com/watch?v=LIIDh-qI9oI"))

#ar2
img3 = Image.open('ar1.png')
rimg3 = ImageTk.PhotoImage(img3)
l3= Label(win, image=rimg3, cursor="hand2")
l3.place(x = 940, y = 400)
l3.bind("<Button-1>", lambda e:
callback("https://www.youtube.com/watch?v=LIIDh-qI9oI"))

win.mainloop()