from tkinter import *
from tkinter import ttk
import mysql.connector as msql

#---------------------------------------------------------------------------------------------------------
#mysqlconnection
mcon=msql.connect(host='localhost',user='root',passwd='parkhi',database='new_schema',port='3307')
curs=mcon.cursor()


#----------------------------------------------------------------------------------------------------------
#window
root = Tk()
root.title("Rantify-Music That You like")
root.iconbitmap('icon.ico')
root.geometry('1920x1080')

#---------------------------------------------------------------------------------------------------------
#bg
canvas1 = Canvas(root, width = 1920, height = 1080, bd=0, highlightthickness=0, relief='ridge')
canvas1.place(x=0,y=0)
mg = PhotoImage(file="ranting_bg.png")
canvas1.create_image(0,0, anchor=NW, image=mg)

#---------------------------------------------------------------------------------------------------------
#logo and header
canvas = Canvas(root, width = 39, height = 39)
canvas.place(x=3,y=3)
img = PhotoImage(file="logo.png")
canvas.create_image(1,1, anchor=NW, image=img)
canvas1.create_text(130,27,text='Rantify',font=("Kollektif", 30),fill='black')

#----------------------------------------------------------------------------------------------------------
canvas1.create_text(700,30, text="Rant Forum", font=("times", 40))
#----------------------------------------------------------------------------------------------------------
#function to fetch random rants from database
def query():
    query='select * from RANTS order by RAND() limit 3'
    curs.execute(query)
    data=curs.fetchall()
    
    for i in data:
       records=(data[0])
  
    text_box = Text(root,height=20,width=70)
    text_box.pack(expand=True)
    text_box.insert('end', records)
    text_box.config(state='disabled')
    
query()
#-----------------------------------------------------------------------------------------------------------

root.mainloop()


