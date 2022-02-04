from tkinter import*
from PIL import ImageTk, Image
import tkinter.font
from tkinter.scrolledtext import ScrolledText

'''def loginques():'''

#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('icon.ico')
root.geometry('500x450')

#background of the landing page 
'''bg=PhotoImage(file = "D:\Github\Rantify-front\quesbg.png")
bg1=Label(root,image=bg)
bg1.place(x=0,y=0,relwidth=1,relheight=1)
#root.config(bg='#050A30')'''

'''#header
head=Label(root,text='Rantify',font=("Kollektif", 30),bg='#050A30',fg='white').place(x=75,y=3)

# heading
ques= Label(root,text='A Few Questions For You',font=('Times','40'),fg='black',border=0).place(x=40,y=200)

#Questions
q1=Label(root,text='1.How was Your Day?',font=('Comic Sans MS',20),bg='#050A30',fg='white').place(x=40,y=280)
e=Entry(root,width=40)
e.place(x=40,y=340)
q2=Label(root,text='1.How was Your Day?',font=('Comic Sans MS',20),bg='#050A30',fg='white').place(x=40,y=380)
e=Entry(root,width=40)
e.place(x=40,y=440)
q3=Label(root,text='1.How was Your Day?',font=('Comic Sans MS',20),bg='#050A30',fg='white').place(x=40,y=480)
e=Entry(root,width=40)
e.place(x=40,y=540)'''

canvas1 = Canvas(root, width = 1920, height = 1080)
canvas1.place(x=3,y=3)
mg = PhotoImage(file="quesbg.png")
canvas1.create_image(1,1, anchor=NW, image=mg)

#logo
canvas = Canvas(root, width = 39, height = 39)
canvas.place(x=3,y=3)
img = PhotoImage(file="ewlog.png")
canvas.create_image(1,1, anchor=NW, image=img)



canvas1.create_text(140, 25, text="Rantify", fill="black", font=('Kollektif 30 bold'))
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

root.mainloop()


#Radio buttons
'''v = StringVar(canvas1, "1")

# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1"}
values1 = {"RadioButton 2" : "1"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(root, text = text, variable = v,
        value = value).place(x=250, y=300)'''




'''def run():
    root=Tk()
    loginques(root)
    root.mainloop'''


