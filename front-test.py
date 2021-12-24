from tkinter import *

window = Tk()
window.geometry('300x500')
window.title("GUI 1")
<<<<<<< HEAD
#bg = PhotoImage(file = "bg.png")
=======


x = Label(window, text="Rantify", font=("Lovelo", 20, "bold")).pack()
b = Button(window, text="Exit", bd='78', command=window.destroy).pack(side = 'bottom')

bg = PhotoImage(file = "bg.png")
>>>>>>> 57207e540e0fc8b1d282cfb61506f36e5f284a4e
c1 = Canvas(window, width=500, height=300)
c1.pack(fill = "both", expand=True)
<<<<<<< HEAD
#c1.create_image( 0, 0, image = bg, anchor = "nw")
=======
c1.create_image( 0, 0, image = bg, anchor = "nw")

>>>>>>> 57207e540e0fc8b1d282cfb61506f36e5f284a4e
name = Label(window, text = "Name").place(x = 30,y = 50)  
password = Label(window, text = "Rant").place(x = 30, y = 130)  
e1 = Entry(window).place(x = 85, y = 50)
inputtxt = Text(window, height = 10, width = 26).place(x = 85, y = 130)




window.mainloop()