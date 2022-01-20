from tkinter import*
from PIL import ImageTk, Image
import tkinter.font
from tkinter.scrolledtext import ScrolledText

#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('D:\Github\Rantify-front\icon.ico')
root.geometry('500x450')

#background of the landing page 
'''bg=PhotoImage(file = "D:\Github\Rantify-front\Background_landingpage.png")
bg1=Label(root,image=bg)
bg1.place(x=0,y=0,relwidth=1,relheight=1)'''

#header
head=Label(root,text='Rantify',font=("Lovelo", 25, "bold"),bg='#97D5FA').pack()
'''bg='#97D5FA'''

#sub-header
sub_head=Label(root,text='Music That You Like',font=("Roboto", 15, "italic"),bg='#97D5FA').pack()
'''bg='#97D5FA'''

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

root.mainloop()