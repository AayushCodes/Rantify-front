from tkinter import*
from PIL import ImageTk, Image,ImageFont,ImageDraw
import tkinter.font

#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('D:\Github\Rantify-front\icon.ico')
root.geometry('500x450')

#background of the landing page 
bg=PhotoImage(file = "D:\Github\Rantify-front\gradnew.png")
bg1=Label(root,image=bg)
bg1.place(x=0,y=0,relwidth=1,relheight=1)

image=Image.open("D:\Github\Rantify-front\gradnew.png")
text1=Label(root,text='aunty')
edit=ImageDraw.Draw(image)
edit.text((150,300),text1)
root.mainloop()