from curses.textpad import Textbox
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
from ranting import*
import webbrowser
import random
#-----------------------------------------------------------------------------------------------------------
#window
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('icon.ico')
root.geometry('1920x1080')

#------------------------------------------------------------------------------------------------------------
#bg
canvas1 = Canvas(root, width=1920, height=1080, bd=0, highlightthickness=0, relief='ridge')
canvas1.place(x=0, y=0)
mg = PhotoImage(file="final2.png")
canvas1.create_image(0, 0, anchor=NW, image=mg)

#-----------------------------------------------------------------------------------------------------------
# logo
canvas = Canvas(root, width=39, height=39)
canvas.place(x=3, y=3)
i = PhotoImage(file="logo.png")
canvas.create_image(1, 1, anchor=NW, image=i)
canvas1.create_text(130,27,text='Rantify',font=("Kollektif", 30),fill='black')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 
#headers
canvas1.create_text(650, 100, text="Looks like you're in a good mood ☺ \nLet's help you keep it that way!",font=("Patrick Hand", 40), fill='#BFF0CF')
canvas1.create_text(610, 240, text="Some playlists to compliment your mood 😉", font=("Patrick Hand", 20), fill='white')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#playlists
justhappy = ['https://open.spotify.com/playlist/7CcLabK7MLra4vkn4W5EHu?si=b0d50375936f47d5' , 'https://open.spotify.com/playlist/0rj2neNUVgP0fEPePgEmZt?si=13ecdff6e62f4eff' , 'https://open.spotify.com/playlist/1z3QRzbnhemLBksy7K3zdr?si=55745a6e86f5463f']
motivated = ['https://open.spotify.com/playlist/0uajNuwxkhFkRKOC278twE?si=578cfdffdae842f4' , 'https://open.spotify.com/playlist/5fjqX5vXrqb4vdeiVjZlLt?si=a2304588893c4271' , 'https://open.spotify.com/playlist/2YOlPM23duxiihTrDsGp0k?si=31f0dee5ec3d4ba3']
vibe = ['https://open.spotify.com/playlist/45rSanWaqUS3CfjVLpug4f?si=951ad5d693184b1c', 'https://open.spotify.com/playlist/0lkvKHCQiiEE9aL9PHwVXU?si=fe5b7ded712948ee', 'https://open.spotify.com/playlist/5uGok6lOvApECG3pWzMuHp?si=ef9a1f17ef414592']
love = ['https://open.spotify.com/playlist/2gpCJBiJGZ7uAAhXhEIOTq?si=660f8c161a6348dd' , 'https://open.spotify.com/playlist/4g3XTA5Yfy9a1GFh7Ct7Sw?si=c9ab9599cc3148f3' , 'https://open.spotify.com/playlist/4ZkmCEy8dumNLQLcgSsSiS?si=43a3ddfb356243fb']
happyrandom=random.choice(justhappy)
motivatedrandom=random.choice(motivated)
viberandom=random.choice(vibe)
loverandom=random.choice(love)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#function for playlist 
def callback(url):
    webbrowser.open_new_tab(url)

l1 = Label(root, text="Motivated", font=('helvetica', 20,'bold'),
            fg="black", bg='#748EFF', cursor="hand2")
l1.place(x=250, y=300)
l1.bind("<Button-1>", lambda e:
    callback(motivatedrandom))


l1 = Label(root, text="In Love", font=('helvetica', 20,"bold"),
    fg="black", bg='#748EFF', cursor="hand2")
l1.place(x=435, y=300)
l1.bind("<Button-1>", lambda e:
    callback(loverandom))


l1 = Label(root, text="Just Happy", font=('helvetica', 20,"bold"),
            fg="black", bg='#748EFF', cursor="hand2")
l1.place(x=600, y=300)
l1.bind("<Button-1>", lambda e:
    callback(happyrandom))

l1 = Label(root, text="Wanna Vibe", font=('helvetica', 20,"bold"),
    fg="black", bg='#748EFF', cursor="hand2")
l1.place(x=800, y=300)
l1.bind("<Button-1>", lambda e:
    callback(viberandom))

#-----------------------------------------------------------------------------------------------------------
#Next page functionality
def nextPage():
    root.destroy()
    import forum 
#------------------------------------------------------------------------------------------------------------
#text
canvas1.create_text(600,500,text='Would you like to read some random rants?',font=('Patrick Hand',25),fill='white')
button=Button(root,text='Yes',command=nextPage,font=("",15),bg='#748EFF').place(x=880,y=480)   
#---------------------------------------------------------------------------------------------------------------
root.mainloop()