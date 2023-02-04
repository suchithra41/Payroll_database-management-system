import tkinter as tk
from tkinter.constants import END

class Addproject(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')

        PROJECT_ID = tk.IntVar()
        PROJECT_TITLE = tk.StringVar()
        DUE_DATE = tk.StringVar()

        back_button = tk.Button(self,text="Back",command=lambda:controller.show_frame("Adminpanel"))
        back_button.grid(row=0,column=1,pady=10,padx=10)

        project_page = tk.Label(self,text="ADD PROJECT DETAILS",foreground="red",background='light green',font=('',15,'bold'))
        project_page.grid(row = 0,column=3,pady=10)

        proj_id = tk.Label(self,text="projet ID")
        proj_title = tk.Label(self,text="project Name")
        due_date = tk.Label(self,text="due Date")

        proj_id.grid(row=3,column=2,pady=10)
        proj_title.grid(row=4,column=2,pady=10)
        due_date.grid(row=5,column=2,pady=10)

        proj_id1 = tk.Entry(self,textvariable=PROJECT_ID)
        proj_title1 = tk.Entry(self,textvariable= PROJECT_TITLE)
        due_date1 = tk.Entry(self,textvariable= DUE_DATE)

        proj_id1.grid(row=3,column=3,pady=10)
        proj_title1.grid(row=4,column=3,pady=10)
        due_date1.grid(row=5,column=3,pady=10)

        proj_id1.delete(0,END)

        proj_id1.focus_set()

        proj_add = tk.Button(self,text="ADD PROJECT",command= lambda: add_proj(PROJECT_ID,PROJECT_TITLE,DUE_DATE))
        proj_add.grid(row=7,column=2,columnspan=10)

        def add_proj(i,t,d):
            if(len(t.get()) == 0 or len(d.get()) == 0 or len(str(i.get())) == 0):
                empty_label = tk.Label(self,text="PLEASE FILL ALL THE DETAILS",foreground="Black",background="light green",font=("",10,'italic'))
                empty_label.grid(row = 9,column=2,columnspan=10)

            else:
                controller.show_frame("Adminpanel")
                proj_id1.delete(0,END)
                proj_title1.delete(0,END)
                due_date1.delete(0,END)










