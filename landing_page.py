from tkinter import*
from PIL import ImageTk, Image
import tkinter.font
#-----------------------------------------------------------------------------------------------------------

#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('icon.ico')
root.geometry('1920x1080')

#-----------------------------------------------------------------------------------------------------------

#bg 
canvas1 = Canvas(root, width = 1920, height = 1080)
canvas1.pack()
mg = ImageTk.PhotoImage(file="landing_bg.png")
canvas1.create_image( 0,0,anchor=NW,image=mg)
#-----------------------------------------------------------------------------------------------------------

#logo and header
canvas = Canvas(root, width = 39, height = 39)
canvas.place(x=5,y=3)
img = PhotoImage(file="logo.png")
canvas.create_image(0,0, anchor=NW, image=img)

canvas1.create_text(130,27,text='Rantify',font=("Kollektif", 30),fill='black')

#-----------------------------------------------------------------------------------------------------------

#graphic text
canvas1.create_text(900,180,text='RANT',fill='#FFD00A',font=('Bungee Shade',45))
canvas1.create_text(950,250,text='YOUR',fill='#FFD00A',font=('Bungee Shade',35))
canvas1.create_text(900,320,text='HEART',fill='#FFD00A',font=('Bungee Shade',45))
canvas1.create_text(950,390,text='OUT',fill='#FFD00A',font=('Bungee Shade',35))

#-----------------------------------------------------------------------------------------------------------

#Function to move to next page
def nextPage():
    root.destroy()
    from login import main
    main()

#-----------------------------------------------------------------------------------------------------------

#login button
logb = Button(root, text='Register',font=('Helvetica',20,'bold') ,width=10,bg='#F1E510',command=nextPage)
logb.place(x=160,y=500)

#-----------------------------------------------------------------------------------------------------------

#text
canvas1.create_text(310,150,text='Rant anytime without',font=('Sans-serif','32'),fill='white')
canvas1.create_text(266,200,text='feeling insecure.',font=('Sans-serif','32'),fill='white')
canvas1.create_text(318,250,text='“Ranting” has been scientifically proven',font=('Sans-serif','18'),fill='white')
canvas1.create_text(327,280,text='to improve your mood and even improve',font=('Sans-serif','18'),fill='white')
canvas1.create_text(320,310,text='efficiency. Music has been known, time',font=('Sans-serif','18'),fill='white')
canvas1.create_text(305,340,text='and time again,to improve our mood',font=('Sans-serif','18'),fill='white')
canvas1.create_text(322,370,text='and help us stay happy.Keeping in that',font=('Sans-serif','18'),fill='white')
canvas1.create_text(305,400,text='same theme,we combined these two',font=('Sans-serif','18'),fill='white')
canvas1.create_text(193,430,text='created Rantify.',font=('Sans-serif','18'),fill='white')

#-----------------------------------------------------------------------------------------------------------



root.mainloop()    



