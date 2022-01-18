from tkinter import*
from PIL import ImageTk, Image
import tkinter.font


#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('D:\Github\Rantify-front\icon.ico')
root.geometry('1920x1080')

img=PhotoImage(file ="D:\Github\Rantify-front\log.png")
label = Label(root, image = img)
label.pack(side='right')



#background of the landing page 
'''bg=PhotoImage(file = "D:\Github\Rantify-front\Background_landingpage.png")
bg1=Label(root,image=bg)
bg1.place(x=0,y=0,relwidth=1,relheight=1)'''

#header
head=Label(root,text='Rantify',font=("Lovelo", 20, "bold")).pack()
'''bg='#97D5FA'''

#sub-header
sub_head=Label(root,text='Music That You Like',font=("Roboto", 15, "italic")).pack()
'''bg='#97D5FA'''

'''#logo resize
pic=Image.open('"D:\Github\Rantify-front\logo.png"')
resized=pic.resize((100,100),Image.ANTIALIAS)
newlogo=ImageTk.PhotoImage(resized)'''


#logo
'''canvas = Canvas(root, width = 100, height = 100)
canvas.pack()'''
img = PhotoImage(file="D:\Github\Rantify-front\log.png")
Button(root,  image = img).place()
'''canvas.create_image(5,5, anchor=NW, image=img)'''


'''#About rantify 
about=Label(root,text='About Rantify')
about.place(x=100, y= 100)
Desired_font = tkinter.font.Font( family = "Secular One", size = 25, weight = 'bold')
about.configure(font = Desired_font)'''

#body 
body=Label(root,text='Lorem ipsum dolor sit amet, consectetur adipiscing elit, ',font=(25)).place(x=100,y=200)
body1=Label(root,text='sed do eiusmod tempor incididunt ut labore et',font=(24)).place(x=100,y=250)
body2=Label(root,text='sed do eiusmod tempor incididunt ut labore et',font=(23)).place(x=100,y=300)
body2=Label(root,text='sed do eiusmod tempor incididunt ut labore et',font=(23)).place(x=100,y=350)






#buttons
#login button
logb = Button(root, text='Log in',font=('Helvetica',20) ,width=10)
logb.place(x=100,y=500)

#signin button 
signinb = Button(root, text='Sign in',font=('Helvetica',20) ,width=10 )
signinb.place(x=350,y=500)





root.mainloop()