from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk    #pip install pillow
from tkinter import messagebox
import mysql.connector

#---------------------------------------------------------------------------------------------------------

f = open("password.txt","r")
data = f.read().strip()


#---------------------------------------------------------------------------------------------------------
def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=data)
    mycursor=mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS new_schema")
    mycursor.execute("USE new_schema")
    mycursor.execute("CREATE TABLE IF NOT EXISTS register(fname VARCHAR(45), lname VARCHAR(45), contact varchar(10), email VARCHAR(45) primary key, secques VARCHAR(45), secqans VARCHAR(45), password VARCHAR(45))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS rants (rants TEXT(65535))")

    mydb.commit()
#---------------------------------------------------------------------------------------------------------

class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title('Rantify-Music That You Like')
        self.root.iconbitmap('icon.ico')
        self.root.geometry("1920x1080")


        self.bg = ImageTk.PhotoImage(file = "login_bg.png") #Bg image of the whole page
        lbl_bg = Label(self.root, image = self.bg)
        lbl_bg.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        frame = Frame(self.root, bg = "black")                                                          #The black box 
        frame.place(x = 467, y = 150, width = 340, height = 450)

        userprofile = Image.open("userprofileimg.png")          #The user profile circle
        userprofile = userprofile.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(userprofile)
        labeling1 = Label(image = self.photoimage1, bg = "black", borderwidth = 0)                      #The profile pic is transparent and we use this func to fill the image bg with black
        labeling1.place(x = 582, y = 160, width = 100, height = 100)

        get_str = Label(frame, text = "Get Started", font = ("times new roman", 20, "bold"), fg = "white", bg = "black")
        get_str.place(x = 95, y = 100)

        #label of username and pass
        username = lbl = Label(frame, text = "Username/email", font = ("times new roman", 15, "bold"), fg = "white", bg = "black")
        username.place(x = 70, y = 155)

        self.txtuser = Entry(frame, font = ("times new roman", 13, "bold"))
        self.txtuser.place(x = 40, y = 180, width = 270)   

        password = lbl = Label(frame, text = "Password", font = ("times new roman", 13, "bold"), fg = "white", bg = "black")
        password.place(x = 70, y = 225)

        self.txtpass = Entry(frame, font = ("times new roman", 15, "bold"),show="*")
        self.txtpass.place(x = 40, y = 250, width = 270)

    # ==========ICON IMAGES================================================================================

        userfrontimage = Image.open("userprofileremovedbg.png")          #The user profile circle
        userfrontimage = userfrontimage.resize((50, 50), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(userfrontimage)
        labeling2 = Label(image = self.photoimage2, bg = "black", borderwidth = 0)
        labeling2.place(x = 512, y = 302, width = 25, height = 25)

        passfrontimage = Image.open("passfront.jpg")          #The user profile circle
        passfrontimage = passfrontimage.resize((50, 50), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(passfrontimage)
        labeling2 = Label(image = self.photoimage3, bg = "black", borderwidth = 0)
        labeling2.place(x = 512, y = 373, width = 25, height = 25)


    #===========login button==================================================================================================================
        
        loginbtn = Button(frame, text = "Login", command = self.login, font = ("Times New Roman", 15, "bold"), bd = 3, relief = RAISED, fg = "white", bg = "sky blue", activeforeground = "white", activebackground = "sky blue")  #loginbutton 
        loginbtn.place(x = 110, y = 300, width = 120, height=35)

        #register button
        registerbtn = Button(frame, text = "Sign Up", command = self.register_window, font = ("Helvetica", 10, "bold"), borderwidth = 0, fg = "white", bg = "black", activebackground="black", activeforeground= "white")  #signupbutton 
        registerbtn.place(x = 90, y = 370, width = 160)

    
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = newuser(self.new_window)

#==============backend connectivity==============================================================================================================================================================================================
    

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "PLACEHOLDER" and self.txtpass.get() == "PLACEHOLDER":
            messagebox.showinfo("Success", "Welcome to Rantify, rant your hearts out.")
        else:
            conn = mysql.connector.connect(host = "localhost", user = "root", password = data, database = "new_schema")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s", (
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()  
                                                                         ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password.")
            else:
                self.root.destroy()
                import ranting_page
            conn.commit()
            conn.close()

# ================== add main software code here =================================================================================================================================================================================                    
                    
                    #self.app = ""      remove the hash and attach code here

# ================== reset password ======================================================================================================================================================
    def reset_pass(self):
        if self.combo_secques.get() == "Select":
            messagebox.showerror("Error", "Select a Security Question")
        elif self.txt_secqans.get() == "":
            messagebox.showerror("Error", "Please enter the answer")
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter your new password")
        else:
            conn = mysql.connector.connect(host = "localhost", user = "root", password = data, database = "new_schema")
            my_cursor = conn.cursor()
            queryfrommysql = ("select * from register where email = %s and secques = %s and secqans = %s")
            valuefrommysql = (self.txtuser.get(), self.combo_secques.get(), self.txt_security)
            my_cursor.execute(queryfrommysql, valuefrommysql)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter correct Answer")
            else:
                updatedquery = ("Update register set password = %s where email = %s")
                updatedvalue = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(updatedquery, updatedvalue)



#=======================new user=====================================================================================================================================

class newuser:
    def __init__(self, root):
        self.root = root
        self.root.title('Rantify-Music That You Like')
        self.root.iconbitmap('icon.ico')
        self.root.geometry("1920x1080")

 #==================== variables ===========================================================================================================

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_secques = StringVar()
        self.var_secqans = StringVar()
        self.var_password = StringVar()
        self.var_confpass = StringVar()

# ================= bg image ============================================================================================
        self.bg = ImageTk.PhotoImage(file = "gradnew.png")
        bg_lbl = Label(self.root, image = self.bg)
        bg_lbl.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# ================= left image ===========================================================================================
        self.leftbg = ImageTk.PhotoImage(file = "MUSIC for your every rant.jpg")
        left_lbl = Label(self.root, image = self.leftbg)
        left_lbl.place(x = 25, y = 70, width = 389, height = 550)

        frame = Frame(self.root, bg = "white")
        frame.place(x = 390, y = 70, width = 700, height = 550)

        register_lbl = Label(frame,text="REGISTER HERE",font=("times new roman", 20, "bold"),fg = "#4682B4", bg = "white")
        register_lbl.place(x = 20, y = 20)

# ================ label and entry ============================================================================================
    #------------ row 1 ------------------------------------------------------------------------------------------------------

        fname = Label(frame, text = "First Name", font = ("times new roman", 15, "bold"), bg = "white")
        fname.place(x = 50, y = 100)

        fname_entry = ttk.Entry(frame, textvariable = self.var_fname, font = ("times new roman", 15, "bold"))
        fname_entry.place(x = 50, y = 132, width = 250)

        l_name = Label(frame, text = "Last Name", font = ("times new roman", 15, "bold"), bg = "white")
        l_name.place(x = 370, y = 100)

        lname_entry = ttk.Entry(frame, textvariable = self.var_lname, font = ("times new roman", 15, "bold"))
        lname_entry.place(x = 370, y = 130, width = 250)

    #------------ row 2 ------------------------------------------------------------------------------------------------------
         
        contact = Label(frame, text = "Contact No", font = ("times new roman", 15, "bold"), bg = "white")
        contact.place(x = 50, y = 170)

        contact = ttk.Entry(frame, textvariable = self.var_contact, font = ("times new roman", 15, "bold"))
        contact.place(x = 50, y = 200, width = 250) 

        email = Label(frame, text = "Email/Username", font = ("times new roman", 15, "bold"), bg = "white")
        email.place(x = 370, y = 170)

        email = ttk.Entry(frame, textvariable = self.var_email, font = ("times new roman", 15, "bold"))
        email.place(x = 370, y = 200, width = 250) 

    #------------ row 3 ------------------------------------------------------------------------------------------------------

        secques = Label(frame, text = "Select Security Question", font = ("times new roman", 15, "bold"), bg = "white")
        secques.place(x = 50, y = 240)

        self.combo_secques = ttk.Combobox(frame, textvariable = self.var_secques, font = ("times new roman", 15, "bold"), state = "readonly")
        self.combo_secques["values"] = ("Select", "Your Birth Place", "Name of a person you despise", "Your least favourite Superhero", "Your favourite song")
        self.combo_secques.place(x = 50, y = 270, width = 250)
        self.combo_secques.current(0)

        secqans = Label(frame, text = "Security Question answer", font = ("times new roman", 15, "bold"), bg = "white")
        secqans.place(x = 370, y = 240)

        secqans = ttk.Entry(frame, textvariable = self.var_secqans, font = ("times new roman", 15, "bold"))
        secqans.place(x = 370, y = 268, width = 250)
        
    #------------ row 4 ------------------------------------------------------------------------------------------------------

        password = Label(frame, text = "Password", font = ("times new roman", 15, "bold"), bg = "white")
        password.place(x = 50, y = 310)

        password = ttk.Entry(frame, textvariable =  self.var_password, font = ("times new roman", 15, "bold"),show="*")
        password.place(x = 50, y = 336, width = 250) 

        cpass = Label(frame, text = "Confirm Password", font = ("times new roman", 15, "bold"), bg = "white")
        cpass.place(x = 370, y = 310)

        cpass = ttk.Entry(frame, textvariable = self.var_confpass, font = ("times new roman", 15, "bold"),show="*")
        cpass.place(x = 370, y = 336, width = 250)


    # ========== buttons =============================================================
   
        '''regnowimg = Image.open(r"Loginform\regnowbutton.png")
        regnowimg = regnowimg.resize((200, 58))
        self.regnimg = ImageTk.PhotoImage(regnowimg)
        regnowbtn = Button(frame, image = self.regnimg, command = self.register_data, borderwidth=0, cursor = "hand2", fg="white")
        regnowbtn.place(x = 40, y = 405, width = 200)'''
        regnowbtn = Button(root, text='Register Now',font=('Helvetica',20,'bold') ,width=10,bg='#748EFF',command = self.register_data,cursor='hand2')
        regnowbtn.place(x = 440, y = 480, width = 200)


        '''lognowimg = Image.open("Loginform\sign-in-button-icon-isometric.jpg")
        lognowimg = lognowimg.resize((200, 140))
        self.loginimg = ImageTk.PhotoImage(lognowimg)
        lognowbtn = Button(frame, image = self.loginimg, borderwidth=0, cursor = "hand2", fg="white")
        lognowbtn.place(x = 400, y = 365, width = 200)
        lognowbtn = Button(root, text='Login',font=('Helvetica',20,'bold') ,width=10,bg='#748EFF',cursor='hand2')
        lognowbtn.place(x = 780, y = 480, width = 200)'''


    # ========= Backend 1 - Function Declaration ====================================================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_secqans.get() == "" or self.var_secques.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_password.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords aren't same")
        else:
            conn = mysql.connector.connect(host = "localhost", user = "root", password = data, database = "new_schema")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)",(
                                                                                              self.var_fname.get(),
                                                                                              self.var_lname.get(),
                                                                                              self.var_contact.get(),
                                                                                              self.var_email.get(),
                                                                                              self.var_secques.get(),
                                                                                              self.var_secqans.get(),
                                                                                              self.var_password.get(),


                                                                                            )) 
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")

#----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

