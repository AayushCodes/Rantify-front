from curses.textpad import Textbox
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
from ranting import*
import webbrowser
import random

root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('icon.ico')
root.geometry('1920x1080')

#----------------------------------------------------------------------------------------------------

canvas1 = Canvas(root, width=1920, height=1080, bd=0,highlightthickness=0, relief='ridge')
canvas1.place(x=0, y=0)
mg = PhotoImage(file="finalpage_bg.png")
canvas1.create_image(0, 0, anchor=NW, image=mg)
#--------------------------------------------------------------------------------------------------------------
# logo
canvas = Canvas(root, width=39, height=39)
canvas.place(x=3, y=3)
i = PhotoImage(file="logo.png")
canvas.create_image(1, 1, anchor=NW, image=i)
canvas1.create_text(130,27,text='Rantify',font=("Kollektif", 30),fill='#748EFF')
#-----------------------------------------------------------------------------------------------------------------

canvas1.create_text(650, 100, text="Looks like you are feeling sad....🙁 \nLet's embrace it, shall we? ",font=("Patrick Hand", 40,'bold'), fill='#BFF0CF')
canvas1.create_text(610, 240, text="Some playlists to compliment your mood 😉", font=("Patrick Hand", 20), fill='white')
#------------------------------------------------------------------------------------------------------------------------
sad = ['https://open.spotify.com/playlist/0nK8XuVZOMGgpAEZAiDcvJ?si=600dbd60cbee4a7b', 'https://open.spotify.com/playlist/44rW9IiTo3nwnCUZ6TcPm9?si=4be0e44af3a14f1d', 'https://open.spotify.com/playlist/6sJOj7IeAfGYgMa7K0SKV1?si=98488cc1bef749c8']
angry = ['https://open.spotify.com/playlist/1o4EL5f8kAy3hFEbhnSepG?si=04b12e9ade564ca2' , 'https://open.spotify.com/playlist/2VsCCUPJOVJC4fm6ehjOGh?si=db22f524fe464c53' , 'https://open.spotify.com/playlist/5X7JBNkfpIRN9RQ4vGwR3s?si=57d61df139224314']
vibe = ['https://open.spotify.com/playlist/45rSanWaqUS3CfjVLpug4f?si=951ad5d693184b1c', 'https://open.spotify.com/playlist/0lkvKHCQiiEE9aL9PHwVXU?si=fe5b7ded712948ee', 'https://open.spotify.com/playlist/5uGok6lOvApECG3pWzMuHp?si=ef9a1f17ef414592']
sadrandom=random.choice(sad)
angryrandom=random.choice(angry)
viberandom=random.choice(vibe)

def callback(url):
        webbrowser.open_new_tab(url)

l1 = Label(root, text="Melancholic", font=('helvetica', 20,'bold'),
        fg='black', bg='#748EFF', cursor="hand2")
l1.place(x=250, y=300)
l1.bind("<Button-1>", lambda e:
        callback(sadrandom))

l1 = Label(root, text="Enraged", font=('helvetica', 20,'bold'),
        fg='black', bg='#748EFF', cursor="hand2")
l1.place(x=530, y=300)
l1.bind("<Button-1>", lambda e:
        callback(angryrandom))

l1 = Label(root, text="Wanna Vibe", font=('helvetica', 20,'bold'),
        fg='black', bg='#748EFF', cursor="hand2")
l1.place(x=770, y=300)
l1.bind("<Button-1>", lambda e:
        callback(viberandom))
#----------------------------------------------------------------------------------------------------------------------------
#Next page functionality
def nextPage():
    root.destroy()
    import forum 

#------------------------------------------------------------------------------------------------------------
canvas1.create_text(600,500,text='Would you like to read some random rants?',font=('Patrick Hand',25),fill='white')
button=Button(root,text='Yes',command=nextPage,font=("",15),bg='#748EFF').place(x=880,y=480)   
#---------------------------------------------------------------------------------------------------------------   


root.mainloop()