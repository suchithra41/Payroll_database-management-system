import tkinter as tk
from tkinter.constants import END

class Addcompany(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')

        COMP_ID = tk.IntVar()
        COMP_NAME = tk.StringVar()
        COMP_ADDR = tk.StringVar()
        COMP_PHNO = tk.IntVar()

        back_button = tk.Button(self,text="Back",command=lambda:controller.show_frame("Adminpanel"))
        back_button.grid(row=0,column=1,pady=10,padx=10)

        company_page = tk.Label(self,text="ADD COMPANY DETAILS",foreground="red",background='light green',font=('',15,'bold'))
        company_page.grid(row = 0,column=3,pady=10)


        comp_id = tk.Label(self,text="company ID")
        comp_name = tk.Label(self,text="company Name")
        comp_addr = tk.Label(self,text="company address")
        comp_phno = tk.Label(self,text="company Ph No")


        comp_id.grid(row=3,column=2,pady=10)
        comp_name.grid(row=4,column=2,pady=10)
        comp_addr.grid(row=5,column=2,pady=10)
        comp_phno.grid(row=6,column=2,pady=10)


        comp_id1 = tk.Entry(self,textvariable=COMP_ID)
        comp_name1 = tk.Entry(self,textvariable=COMP_NAME)
        comp_addr1 = tk.Entry(self,textvariable=COMP_ADDR)
        comp_phno1 = tk.Entry(self,textvariable=COMP_PHNO)

        comp_id1.grid(row=3,column=3,pady=10)
        comp_name1.grid(row=4,column=3,pady=10)
        comp_addr1.grid(row=5,column=3,pady=10)
        comp_phno1.grid(row=6,column=3,pady=10)

        comp_id1.delete(0,END)
        comp_phno1.delete(0,END)

        comp_id1.focus_set()

        comp_add = tk.Button(self,text="ADD COMAPNY",command= lambda: add_com(COMP_ID,COMP_ADDR,COMP_NAME,COMP_PHNO))
        comp_add.grid(row=8,column=2,columnspan=10)

        def add_com(i,a,n,p):
            empty_label = tk.Label(self,text="PLEASE FILL ALL THE DETAILS",foreground="Black",background="light green",font=("",10,'italic'))
            if(len(a.get()) == 0 or len(n.get()) == 0 or len(str(i.get())) == 0 or len(str(p.get())) == 0):
                empty_label.grid(row = 10,column=2,columnspan=10)

            else:
                empty_label.config(text="")
                comp_addr1.delete(0,END)
                comp_name1.delete(0,END)
                comp_phno1.delete(0,END)
                comp_id1.delete(0,END)
                controller.show_frame("Adminpanel")