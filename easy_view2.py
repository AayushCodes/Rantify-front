from tkinter import*
from PIL import ImageTk, Image
import tkinter.font

#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('icon.ico')
root.geometry('1920x1080')


'''img=PhotoImage(file ="log.png")
label = Label(root, image = img)
label.pack(side='right')'''


root.iconbitmap('icon.ico')
root.geometry('500x450')

#background of the landing page 
'''bg=PhotoImage(file = "gradnew.png")
bg1=Label(root,image=bg)
bg1.place(x=0,y=0,relwidth=1,relheight=1)'''

root.config(bg='#050A30')

#header
head=Label(root,text='Rantify',font=("Kollektif", 30),bg='#050A30',fg='white').place(x=75,y=3)
'''bg='#97D5FA'''

#sub-header
'''sub_head=Label(root,text='Music That You Like',font=("Roboto", 15, "italic")).place(x=200,y=1)'''
'''bg='#97D5FA'''

'''#logo resize
pic=Image.open('"D:/Github\Rantify-front\logo.png"')
resized=pic.resize((100,100),Image.ANTIALIAS)
newlogo=ImageTk.PhotoImage(resized)'''


#logo
'''canvas = Canvas(root, width = 100, height = 100)
canvas.pack()'''
img = PhotoImage(file="log.png")
#logo
canvas = Canvas(root, width = 99, height = 99)
canvas.place(x=0,y=0)
img = PhotoImage(file="log.png")
Button(root,  image = img).place()
#logo
canvas = Canvas(root, width = 39, height = 39)
canvas.place(x=3,y=3)
img = PhotoImage(file="ewlog.png")
canvas.create_image(1,1, anchor=NW, image=img)

#body 
body=Label(root,text='Rant anytime without',font=('Sans-serif','32'),bg='#050A30',fg='white').place(x=100,y=150)
body1=Label(root,text='feeling insecure',font=('Helvetica','32'),bg='#050A30',fg='white').place(x=100,y=200)
body2=Label(root,text='“Ranting” has been scientifically proven',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=250)
body2=Label(root,text='to improve your mood and even improve',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=280)
body2=Label(root,text='efficiency. Music has been known,time',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=310)
body2=Label(root,text='time again,to improve our mood and ',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=340)
body2=Label(root,text='help us stay happy.Keeping in that',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=370)
body2=Label(root,text='same theme,we combined these two and',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=400)
body2=Label(root,text='created Rantify.',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=430)
body2=Label(root,text='“Ranting” has been scientifically proven',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=250)

#side graphic
canvas1 = Canvas(root, width = 500, height = 500,bd=7,relief=RAISED)
canvas1.place(x=700,y=90)
img1 = PhotoImage(file="sidegraphic.png")
canvas1.create_image(0,0,anchor=NW, image=img1)

#buttons
#login button
logb = Button(root, text='Log in',font=('Helvetica',20,'bold') ,width=10,bg='#748EFF')
logb.place(x=100,y=500)

#signin button 
signinb = Button(root, text='Sign in',font=('Helvetica',20,'bold') ,width=10,bg='white' )
signinb.place(x=350,y=500)


root.mainloop()