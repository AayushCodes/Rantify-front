from tkinter import *


#creating a window
window=Tk()
window.geometry('500x500')
c1 = Canvas(window, width=500, height=300)
window.title('Rantify')
head=Label(window, text='RANTIFY').pack()

#toplevel PhotoImage
p1 = PhotoImage(file = 'logo.png')
window.iconphoto(False, p1)

#logo image
# img=Image.open('logo.png')
# img=img.resize('200x200')
# image=Label(window, image=img).grid(row=0, column=1)

#login button
logb = Button(window, text='Log in', width=25)
logb.place(relx = 1.0, rely = 0.0,anchor='ne')
logb.pack(pady = 10)


  
window.mainloop()



#creating a heading

