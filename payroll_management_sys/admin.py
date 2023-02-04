import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import ITALIC 
from tkinter.ttk import *
from adminPanel import Adminpanel


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')

        USERNAME = StringVar()
        EMAILID = StringVar()
        PASSWORD = StringVar()

        back_button = tk.Button(self,text="Back",command=lambda:controller.show_frame("StartPage"))
        back_button.grid(row=0,column=1,pady=10,padx=10)

        register_page = tk.Label(self,text="REGISTER PAGE",foreground="red",background='light green',font=('',15,'bold'))
        register_page.grid(row = 0,column=3,pady=10)

        username = tk.Label(self,text="username")
        emailid = tk.Label(self,text='Emailid')
        password = tk.Label(self,text='password')

        username.grid(row=2,column=2,pady=10)
        emailid.grid(row=3,column=2,pady=10)
        password.grid(row=4,column=2,pady=10)

        username_var = tk.Entry(self,textvariable= USERNAME)
        emailid_var = tk.Entry(self,textvariable= EMAILID)
        password_var = tk.Entry(self,textvariable= PASSWORD)

        username_var.focus_set()

        username_var.grid(row=2,column=3,pady=10)
        emailid_var.grid(row=3,column=3,pady=10)
        password_var.grid(row=4,column=3,pady=10)


        register_button = Button(self,text="Register",command = lambda: register_submit(USERNAME,EMAILID,PASSWORD))
        register_button.grid(row=5,column=2,columnspan=10)        
       

        def register_submit(u,e,p):
            if(len(u.get()) == 0 or len(e.get()) == 0 or len(p.get()) == 0):
                empty_label = tk.Label(self,text="PLEASE FILL ALL THE DETAILS",foreground="Black",background="light green",font=("",10,ITALIC))
                empty_label.grid(row = 8,column=1,columnspan=10)
            else:
                controller.show_frame("StartPage")
                username_var.delete(0,END)
                password_var.delete(0,END)
                emailid_var.delete(0,END)


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')

        USERNAME = StringVar()
        PASSWORD = StringVar()

        back_button = tk.Button(self,text="Back",command=lambda:controller.show_frame("StartPage"))
        back_button.grid(row=0,column=1,pady=10,padx=10)


        login_page = tk.Label(self,text="LOGIN PAGE",foreground="red",background='light green',font=('',15,'bold'))
        login_page.grid(row = 0,column=3,pady=10)

        username = tk.Label(self,text="username")
        password = tk.Label(self,text='password')

        username.grid(row=1,column=2,pady=10)
        password.grid(row=3,column=2,pady=10)

        username_var = tk.Entry(self,textvariable= USERNAME)
        password_var = tk.Entry(self,textvariable= PASSWORD)

        username_var.focus_set()

        username_var.grid(row=1,column=3,pady=10)
        password_var.grid(row=3,column=3,pady=10)


        register_button = tk.Button(self,text="Login",command = lambda: login_submit(USERNAME,PASSWORD))
        register_button.grid(row=5,column=1,columnspan=10)

        def login_submit(u,p):
            if(len(u.get()) == 0 or len(p.get()) == 0):
                empty_label = tk.Label(self,text="PLEASE FILL ALL THE DETAILS",foreground="Black",background="light green",font=("",10,ITALIC))
                empty_label.grid(row = 8,column=1,columnspan=10)
            else:
                controller.show_frame("Adminpanel")
                username_var.delete(0,END)
                password_var.delete(0,END)



        

    