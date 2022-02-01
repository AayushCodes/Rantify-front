from tkinter import*
from PIL import ImageTk, Image
import tkinter.font
from tkinter.scrolledtext import ScrolledText

#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('icon.ico')
root.geometry('500x450')

#background of the landing page 
'''bg=PhotoImage(file = "D:\Github\Rantify-front\Background_landingpage.png")
bg1=Label(root,image=bg)
bg1.place(x=0,y=0,relwidth=1,relheight=1)'''



'''#header
head=Label(root,text='Rantify',font=("Lovelo", 25, "bold"),bg='#97D5FA').pack()


#sub-header
sub_head=Label(root,text='Music That You Like',font=("Roboto", 15, "italic"),bg='#97D5FA').pack()


#logo
canvas = Canvas(root, width = 99, height = 99)
canvas.place(x=0,y=0)
img = PhotoImage(file="D:\Github\Rantify-front\log.png")
Button(root,  image = img).place()
canvas.create_image(1,1, anchor=NW, image=img)

# heading
ques= Label(root,text='A Few Questions For You',font=('Times','25')).place(x=40,y=200)

#Questions
q1=Label(root,text='1.What kind of music do you like?',font=('Comic Sans MS',20)).place(x=40,y=280)
e=Entry(root,width=40)
e.place(x=40,y=340)
q2=Label(root,text='1.Who is your favourite artist?',font=('Comic Sans MS',20)).place(x=40,y=380)
e=Entry(root,width=40)
e.place(x=40,y=440)
q3=Label(root,text='1.What genre do you like the most ?',font=('Comic Sans MS',20)).place(x=40,y=480)
e=Entry(root,width=40)
e.place(x=40,y=540)

canvas1 = Canvas(root, width = 1920, height = 1080)
canvas1.place(x=3,y=3)
mg = PhotoImage(file="D:\Github\Rantify-front\quesbg.png")
canvas1.create_image(1,1, anchor=NW, image=mg)'''

canvas1 = Canvas(root, width = 1920, height = 1080)
canvas1.place(x=3,y=3)
mg = PhotoImage(file="quesbg.png")
canvas1.create_image(1,1, anchor=NW, image=mg)


#logo
canvas = Canvas(root, width = 39, height = 39)
canvas.place(x=3,y=3)
img = PhotoImage(file="ewlog.png")
canvas.create_image(1,1, anchor=NW, image=img)



canvas1.create_text(140,25, text="Rantify", fill="black", font=('Kollektif 30 bold'))
canvas1.pack()

canvas1.create_text(600, 130, text="A Few Questions For You",font=('Helvetica','40'))
canvas1.pack()

canvas1.create_text(480, 210, text='1.How was Your Day?',font=('Helvetica','28'))
canvas1.pack()

e=Entry(root,width=100)
e.place(x=310,y=250)


canvas1.create_text(480, 310, text='1.How was Your Day?',font=('Helvetica','28'))
canvas1.pack()

e=Entry(root,width=100)
e.place(x=310,y=350)

canvas1.create_text(480, 410, text='1.How was Your Day?',font=('Helvetica','28'))
canvas1.pack()
e=Entry(root,width=100)
e.place(x=310,y=450)

#submit button 
sub=Button(root,text='Submit',font=('Helvetica',15),width=12,height=1).place(x=750,y=500)

root.mainloop()