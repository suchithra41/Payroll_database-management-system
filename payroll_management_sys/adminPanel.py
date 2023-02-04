import tkinter as tk

class Adminpanel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')

        back_button = tk.Button(self,text="Logout",command=lambda: controller.show_frame("StartPage"))
        back_button.grid(row=0,column=1,pady=10,padx=10)

        heading1 = tk.Label(self,text="ADMIN",foreground='red',background='lightgreen',font=("",20,'bold'))
        heading1.grid(row = 1,column = 2)

        heading2 = tk.Label(self,text="DASHBOARD",foreground='red',background='lightgreen',font=("",20,'bold'))
        heading2.grid(row = 1,column = 3)


        add_button = tk.Button(self,text = "ADD DETAILS",command= lambda: add_buttons(3))
        view_button = tk.Button(self,text= "VIEW DETAILS",command= lambda: view_buttons(3))

        add_button.grid(row=3,column=2,padx=20,pady=20)
        view_button.grid(row=3,column=3,padx=20,pady=20)

        def add_buttons(x):
            add_company = tk.Button(self,text = "ADD COMPANY",command= lambda :   controller.show_frame("Addcompany"))
            add_depatment = tk.Button(self,text = "ADD DEPARTMENT",command= lambda  :   controller.show_frame("Addepartment"))
            add_project = tk.Button(self,text = "ADD PROJECT",command= lambda  :   controller.show_frame("Addproject"))
            add_employee = tk.Button(self,text = "ADD EMPLOYEE",command= lambda  :   controller.show_frame("Addemployee"))
            add_bank = tk.Button(self,text = "ADD BANK",command= lambda  :   controller.show_frame("Addbank"))
            add_paygrade = tk.Button(self,text = "ADD PAYGRADE",command= lambda  :   controller.show_frame("Addpaygrade"))
            add_payroll = tk.Button(self,text = "ADD PAYROLL",command= lambda  :   controller.show_frame("Addpayroll"))


            add_company.grid(row = 5,column=1)
            add_depatment.grid(row = 5,column=2)
            add_project.grid(row = 5,column=3)
            add_employee.grid(row = 5,column=4)
            add_bank.grid(row = 5,column=5)
            add_paygrade.grid(row = 5,column=6)
            add_payroll.grid(row = 5,column=7)


        def view_buttons(e):
            
            view_company = tk.Button(self,text = "VIEW COMPANY",command= lambda  : add_buttons)
            view_depatment = tk.Button(self,text = "VIEW DEPARTMENT",command= lambda  : add_buttons)
            view_project = tk.Button(self,text = "VIEW PROJECT",command= lambda  : add_buttons)
            view_employee = tk.Button(self,text = "VIEW EMPLOYEE",command= lambda  : add_buttons)
            view_bank = tk.Button(self,text = "VIEW BANK",command= lambda  : add_buttons)
            view_paygrade = tk.Button(self,text = "VIEW PAYGRADE",command= lambda  : add_buttons)
            view_payroll = tk.Button(self,text = "VIEW PAYROLL",command= lambda  : add_buttons)


            view_company.grid(row = 5,column=1)
            view_depatment.grid(row = 5,column=2)
            view_project.grid(row = 5,column=3)
            view_employee.grid(row = 5,column=4)
            view_bank.grid(row=5,column=5)
            view_paygrade.grid(row = 5,column=6)
            view_payroll.grid(row = 5,column=7)
            


        





