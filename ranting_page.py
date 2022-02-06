from curses.textpad import Textbox
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
from ranting import*
import webbrowser
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="parkhi",port='3307',database='new_schema')
mycursor=mydb.cursor()

def printInput():
   inp = inputtxt.get(1.0, "end-1c")
   global prediction
   prediction=rant_check(inp)
   query=mycursor.execute("INSERT INTO rants VALUES('{}')".format(inp))
   mydb.commit()
   
   
  
   
def output ():
      if prediction==1:
            win.destroy()
            import happy
      else:
            win.destroy()
            import sad
    
#----------------------------------------------------------------------------------------------------------
#window
win = Tk()
win.title("Rantify-Music That You like")
win.iconbitmap('icon.ico')
win.geometry('1920x1080')

#-----------------------------------------------------------------------------------------------------------
#bg 
canvas1 = Canvas(win, width = 1920, height = 1080, bd=0, highlightthickness=0, relief='ridge')
canvas1.place(x=0,y=0)
mg = PhotoImage(file="ranting_bg.png")
canvas1.create_image(0,0, anchor=NW, image=mg)

#------------------------------------------------------------------------------------------------------------
#logo
canvas = Canvas(win, width = 39, height = 39)
canvas.place(x=3,y=3)
img = PhotoImage(file="logo.png")
canvas.create_image(1,1, anchor=NW, image=img)
canvas1.create_text(130,27,text='Rantify',font=("Kollektif", 30),fill='black')

#-----------------------------------------------------------------------------------------------------------
#title
canvas1.create_text(130, 180, text="Title:", fill='white', font=("Fredoka One", 40))
e1 = Entry(win, font=('',20)).place(x = 230, y = 165, width=500, height=37)

#----------------------------------------------------------------------------------------------------------
canvas1.create_text(132, 275, text="Rant:", fill='white', font=("Fredoka One", 40))
canvas1.create_text(350, 275, text="(Don't hold it back)", fill='black', font=("Fredoka One", 20,'italic'))

frame = Frame(win)                                                          
frame.place(x = 70, y = 320, width = 850, height = 200)
# TextBox Creation
inputtxt = Text(frame,height = 200,width = 850,font=('helvetica',20))
inputtxt.pack()





#-----------------------------------------------------------------------------------------------------------
#page functionality


#-----------------------------------------------------------------------------------------------------------
#button
lezgo = Button(win, text="Lezz Go",font=("", 20),command=output,bg='#748EFF').place(x = 720, y = 530)
submit=Button(win,text='Submit',font=("", 20),command=printInput,bg='#748EFF').place(x = 450, y = 530)
#-----------------------------------------------------------------------------------------------------------

win.mainloop()