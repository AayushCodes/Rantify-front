
from tkinter import*
from PIL import ImageTk, Image
import tkinter.font

root=Tk()
root.title('Rantify-Music That You Like')
root.iconbitmap('icon.ico')
root.geometry('1920x1080')

frame = Frame(root)                                                          
frame.place(x = 467, y = 150, width = 340, height = 450)
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    
  
# TextBox Creation
inputtxt = Text(frame,
                   height = 5,
                   width = 50)
  
inputtxt.pack()
  
# Button Creation
printButton = Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = Label(frame, text = "")
lbl.pack()
frame.mainloop()