from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image  




#creating a window
window=Tk()
window.option_add('*Font', 'Times')
window.geometry('500x500')
c1 = Canvas(window, width=500, height=300)
window.title('Rantify')

#header

head=Label(window, text='RANTIFY',).pack()
subtext=Label(window,text="The music you like").pack()


#toplevel PhotoImage
p1 = PhotoImage(file = 'logo.png')
window.iconphoto(False, p1)


#logo image
# img=Image.open('logo.png')
# img=img.resize('200x200')
# image=Label(window, image=img).grid(row=0, column=1)

#login button
logb = Button(window, text='Log in', width=10)
logb.place(x=1100,y=11)

#signin button 
signinb = Button(window, text='Sign in', width=10)
signinb.place(x=950,y=11)

'''bg = PhotoImage(file = "background.png")
backimg = Label( window, image = bg)
backimg.pack()'''




  
window.mainloop()



#creating a heading

