from tkinter import*
from PIL import ImageTk, Image
import tkinter.font

#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('icon.ico')
root.geometry('500x450')

'''#background of the landing page 
bg=PhotoImage(file = "D:\Github\Rantify-front\gradnew.png")
bg1=Label(root,image=bg)
bg1.place(x=0,y=0,relwidth=1,relheight=1)
root.config(bg='#050A30')'''


'''#header
head=Label(root,text='Rantify',font=("Kollektif", 30),bg='#050A30',fg='white').place(x=75,y=3)


#sub-header
sub_head=Label(root,text='Music That You Like',font=("Roboto", 15, "italic")).place(x=200,y=1)'''


'''#logo
canvas = Canvas(root, width = 39, height = 39)
canvas.place(x=3,y=3)
img = PhotoImage(file="D:\Github\Rantify-front\ewlog.png")
canvas.create_image(1,1, anchor=NW, image=img)'''

'''#body 
canvas(root,text='Rant anytime without',font=('Sans-serif','32'),bg='#050A30',fg='white').place(x=100,y=150)
body1=Label(root,text='feeling insecure',font=('Helvetica','32'),bg='#050A30',fg='white').place(x=100,y=200)
body2=Label(root,text='“Ranting” has been scientifically proven',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=250)
body2=Label(root,text='to improve your mood and even improve',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=280)
body2=Label(root,text='efficiency. Music has been known,time',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=310)
body2=Label(root,text='time again,to improve our mood and ',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=340)
body2=Label(root,text='help us stay happy.Keeping in that',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=370)
body2=Label(root,text='same theme,we combined these two and',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=400)
body2=Label(root,text='created Rantify.',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=430)
body2=Label(root,text='“Ranting” has been scientifically proven',font=('Helvetica','18'),bg='#050A30',fg='white').place(x=100,y=250)'''

#bg 
canvas1 = Canvas(root, width = 1920, height = 1080)
canvas1.place(x=0,y=0)
mg = PhotoImage(file="GRADNEW2.png")
canvas1.create_image(1,1, anchor=NW, image=mg)

#logo
canvas = Canvas(root, width = 39, height = 39)
canvas.place(x=3,y=3)
img = PhotoImage(file="ewlog.png")
canvas.create_image(1,1, anchor=NW, image=img)

#Rantify
canvas1.create_text(130,27,text='Rantify',font=("Kollektif", 30),fill='black')

canvas1.create_text(900,180,text='RANT',fill='#FFD00A',font=('Bungee Shade',45))
canvas1.create_text(950,250,text='YOUR',fill='#FFD00A',font=('Bungee Shade',35))
canvas1.create_text(900,320,text='HEART',fill='#FFD00A',font=('Bungee Shade',45))
canvas1.create_text(950,390,text='OUT',fill='#FFD00A',font=('Bungee Shade',35))

def nextPage():
    root.destroy()
    import ques_login

#buttons
#login button
logb = Button(root, text='Log in',font=('Helvetica',20,'bold') ,width=10,bg='#748EFF',command=nextPage)
logb.place(x=100,y=500)

#signin button 
signinb = Button(root, text='Sign up',font=('Helvetica',20,'bold') ,width=10,bg='white' )
signinb.place(x=350,y=500)

canvas1.create_text(310,150,text='Rant anytime without',font=('Sans-serif','32'),fill='white')
canvas1.create_text(266,200,text='feeling insecure.',font=('Sans-serif','32'),fill='white')
canvas1.create_text(318,250,text='“Ranting” has been scientifically proven',font=('Sans-serif','18'),fill='white')
canvas1.create_text(327,280,text='to improve your mood and even improve',font=('Sans-serif','18'),fill='white')
canvas1.create_text(320,310,text='efficiency. Music has been known, time',font=('Sans-serif','18'),fill='white')
canvas1.create_text(305,340,text='and time again,to improve our mood',font=('Sans-serif','18'),fill='white')
canvas1.create_text(322,370,text='and help us stay happy.Keeping in that',font=('Sans-serif','18'),fill='white')
canvas1.create_text(305,400,text='same theme,we combined these two',font=('Sans-serif','18'),fill='white')
canvas1.create_text(193,430,text='created Rantify.',font=('Sans-serif','18'),fill='white')



root.mainloop()    



