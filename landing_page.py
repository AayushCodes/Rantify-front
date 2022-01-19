from tkinter import*
from PIL import ImageTk, Image
import tkinter.font


#window 
root=Tk()
root.title('Rantify-Music That You Like')
<<<<<<< HEAD
root.iconbitmap('icon.ico')
root.geometry('1920x1080')

img=PhotoImage(file ="log.png")
label = Label(root, image = img)
label.pack(side='right')


=======
root.iconbitmap('D:\Github\Rantify-front\icon.ico')
root.geometry('500x450')
>>>>>>> 39fbe8b33c7c7715954bf93dd158d0f7594ad7ea

#background of the landing page 
bg=PhotoImage(file = "D:\Github\Rantify-front\Background_landingpage.png")
bg1=Label(root,image=bg)
bg1.place(x=0,y=0,relwidth=1,relheight=1)

#header
head=Label(root,text='Rantify',font=("Lovelo", 25, "bold"),bg='#97D5FA').pack()
'''bg='#97D5FA'''

#sub-header
sub_head=Label(root,text='Music That You Like',font=("Roboto", 15, "italic"),bg='#97D5FA').pack()
'''bg='#97D5FA'''

<<<<<<< HEAD
'''#logo resize
pic=Image.open('"D:/Github\Rantify-front\logo.png"')
resized=pic.resize((100,100),Image.ANTIALIAS)
newlogo=ImageTk.PhotoImage(resized)'''


#logo
'''canvas = Canvas(root, width = 100, height = 100)
canvas.pack()'''
img = PhotoImage(file="log.png")
=======
#logo
canvas = Canvas(root, width = 99, height = 99)
canvas.place(x=0,y=0)
img = PhotoImage(file="D:\Github\Rantify-front\log.png")
>>>>>>> 39fbe8b33c7c7715954bf93dd158d0f7594ad7ea
Button(root,  image = img).place()
canvas.create_image(1,1, anchor=NW, image=img)

#body 
body=Label(root,text='Lorem ipsum dolor sit amet, consectetur adipiscing',font=('Helvetica','26'),bg='#B3E1FB').place(x=100,y=200)
body1=Label(root,text='sed do eiusmod tempor incididunt ut labore et',font=('Helvetica','20'),bg='#B6E2FB').place(x=100,y=250)
body2=Label(root,text='sed do eiusmod tempor incididunt ut labore et',font=('Helvetica','18'),bg='#BDE3FD').place(x=100,y=300)
body2=Label(root,text='sed do eiusmod tempor incididunt ut labore et',font=('Helvetica','18'),bg='#C4E6FF').place(x=100,y=350)

#buttons
#login button
logb = Button(root, text='Log in',font=('Helvetica',20,'bold') ,width=10,bg='#748EFF')
logb.place(x=100,y=500)

#signin button 
signinb = Button(root, text='Sign in',font=('Helvetica',20,'bold') ,width=10,bg='white' )
signinb.place(x=350,y=500)





root.mainloop()