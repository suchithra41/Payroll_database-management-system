import tkinter as tk
from tkinter.constants import END

class Addepartment(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')

        DEP_ID = tk.IntVar()
        DEP_NAME = tk.StringVar()
        COMP_NAME = tk.StringVar()
        DEP_SIZE = tk.IntVar()
        DEP_ROOMNO = tk.IntVar()
        DEP_HEAD = tk.StringVar()

        back_button = tk.Button(self,text="Back",command=lambda:controller.show_frame("Adminpanel"))
        back_button.grid(row=0,column=1,pady=10,padx=10)


        department_page = tk.Label(self,text="ADD DEPARTMENT DETAILS",foreground="red",background='light green',font=('',15,'bold'))
        department_page.grid(row = 0,column=3,pady=10)


        dep_id = tk.Label(self,text=" department ID")
        dep_name = tk.Label(self,text=" department Name")
        comp_name = tk.Label(self,text=" company Name")
        dep_size = tk.Label(self,text=" department Size")
        dep_roomno = tk.Label(self,text="department Room No")
        dep_head = tk.Label(self,text="HOD")


        dep_id.grid(row=3,column=2,pady=10)
        dep_name.grid(row=4,column=2,pady=10)
        comp_name.grid(row=5,column=2,pady=10)
        dep_size.grid(row=6,column=2,pady=10)
        dep_roomno.grid(row=7,column=2,pady=10)
        dep_head.grid(row=8,column=2,pady=10)


        dep_id1 = tk.Entry(self,textvariable=DEP_ID)
        dep_name1 = tk.Entry(self,textvariable=DEP_NAME)
        comp_name1 = tk.Entry(self,textvariable=COMP_NAME)
        dep_size1 = tk.Entry(self,textvariable=DEP_SIZE)
        dep_roomno1 = tk.Entry(self,textvariable=DEP_ROOMNO)
        dep_head1 = tk.Entry(self,textvariable=DEP_HEAD)

        dep_id1.delete(0,END)
        dep_size1.delete(0,END)
        dep_roomno1.delete(0,END)

        dep_id1.grid(row=3,column=3,pady=10)
        dep_name1.grid(row=4,column=3,pady=10)
        comp_name1.grid(row=5,column=3,pady=10)
        dep_size1.grid(row=6,column=3,pady=10)
        dep_roomno1.grid(row=7,column=3,pady=10)
        dep_head1.grid(row=8,column=3,pady=10)
                 

        dep_id1.focus_set()

        dep_add = tk.Button(self,text="ADD DEPARTMENT",command= lambda: add_dep(DEP_ID,DEP_NAME,COMP_NAME,DEP_SIZE,DEP_ROOMNO,DEP_HEAD))
        dep_add.grid(row=10,column=2,columnspan=10)

        def add_dep(i,n,cn,s,r,h):
            if(len(cn.get()) == 0 or len(n.get()) == 0 or len(str(i.get())) == 0 or len(str(s.get())) == 0 or len(str(r.get())) == 0 or len(h.get()) == 0):
                empty_label = tk.Label(self,text="PLEASE FILL ALL THE DETAILS",foreground="Black",background="light green",font=("",10,'italic'))
                empty_label.grid(row = 12,column=2,columnspan=10)

            else:
                controller.show_frame("Adminpanel")
                dep_id1.delete(0,END)
                dep_name1.delete(0,END)
                dep_size1.delete(0,END)
                dep_roomno1.delete(0,END)
                dep_head1.delete(0,END)
                comp_name1.delete(0,END)