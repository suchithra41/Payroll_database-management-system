import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from admin import Login, Register
from adminPanel import Adminpanel
from company import Addcompany
from department import Addepartment
from project import Addproject
from employee import Addemployee
from paygrade import Addpaygrade
from payroll import Addpayroll
from bank import Addbank

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Register,Login,Adminpanel,Addbank,Addcompany,Addepartment,Addemployee,Addpaygrade,Addpayroll,Addproject):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller

        self.controller.title("payroll management system")
        self.controller.state('zoomed')
    
        heading1 = tk.Label(self,text="WELCOME TO",foreground='red',background='light green',font=('',20,'bold'))
        heading2 = tk.Label(self,text="PAYROLL MANAGEMENT SYSTEM",foreground='red',background='light green',font=('',20,'bold'))


        heading1.grid(row=1,column=3,columnspan=10)
        heading2.grid(row=2,column=3,columnspan=10)

        button1 = tk.Button(self,text='Register',command = lambda: controller.show_frame("Register"))
        button2 = tk.Button(self,text='Login',command= lambda: controller.show_frame("Login") )

        button1.grid(row=5,column=6)
        button2.grid(row=5,column=9)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()





