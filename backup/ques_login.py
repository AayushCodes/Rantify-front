from tkinter import*
from PIL import ImageTk, Image
import tkinter.font
from tkinter.scrolledtext import ScrolledText

'''def loginques():'''

#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('icon.ico')
root.geometry('1920x1080')


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

def nextPage():
    
    root.destroy()
    import ranting_page


sub=Button(root,text='Submit',font=('Helvetica',15),width=12,height=1,command=nextPage).place(x=750,y=500)

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

