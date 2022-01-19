from tkinter import*
from PIL import ImageTk, Image
import tkinter.font


#window 
root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('D:\Github\Rantify-front\icon.ico')
root.geometry('500x450')

menubar=Menu(root)


filemenu = Menu(menubar,)
image=PhotoImage(file ='D:\Github\Rantify-front\log.png')
menubar.add_cascade(label=image,menu=filemenu)
root.config(menu=menubar)
root.mainloop()