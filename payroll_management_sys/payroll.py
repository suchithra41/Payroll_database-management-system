import tkinter as tk
from tkinter.constants import END

class Addpayroll(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')

        PAYROLL_ID = tk.IntVar()
        EMP_ID = tk.IntVar()
        TRANS_ID = tk.IntVar()
        ACC_NUM =tk.IntVar()
        DOT = tk.StringVar()
        PAYROLL_REP = tk.StringVar()
        TOTAL_AMT =tk.IntVar()

        back_button = tk.Button(self,text="Back",command=lambda:controller.show_frame("Adminpanel"))
        back_button.grid(row=0,column=1,pady=10,padx=10)

        
        payroll_page = tk.Label(self,text="PAYROLL PAGE",foreground="red",background='light green',font=('',15,'bold'))
        payroll_page.grid(row = 0,column=3,pady=10)

        PAYROLL_ID,EMP_ID,TRANS_ID,ACC_NUM,DOT,PAYROLL_REP,TOTAL_AMT

        payroll_id = tk.Label(self,text="payroll ID")
        emp_id = tk.Label(self,text="employee ID")
        trans_id = tk.Label(self,text="transaction ID")
        acc_num = tk.Label(self,text="account Number")
        dot =  tk.Label(self,text="date of transaction")
        payroll_rep = tk.Label(self,text="payroll Report")
        total_amt = tk.Label(self,text="total Amount")

        payroll_id.grid(row=3,column=2,pady=10) 
        emp_id.grid(row=4,column=2,pady=10) 
        trans_id.grid(row=5,column=2,pady=10) 
        acc_num.grid(row=6,column=2,pady=10) 
        dot.grid(row=7,column=2,pady=10) 
        payroll_rep.grid(row=8,column=2,pady=10) 
        total_amt.grid(row=9,column=2,pady=10) 

        
        payroll_id1 = tk.Entry(self,textvariable=PAYROLL_ID)
        emp_id1 = tk.Entry(self,textvariable=EMP_ID)
        trans_id1 = tk.Entry(self,textvariable=TRANS_ID)
        acc_num1 = tk.Entry(self,textvariable=ACC_NUM)
        dot1 = tk.Entry(self,textvariable=DOT)
        payroll_rep1 = tk.Entry(self,textvariable=PAYROLL_REP)
        total_amt1 = tk.Entry(self,textvariable=TOTAL_AMT)
        
        payroll_id1.grid(row=3,column=3,pady=10)
        emp_id1.grid(row=4,column=3,pady=10)
        trans_id1.grid(row=5,column=3,pady=10)
        acc_num1.grid(row=6,column=3,pady=10)
        dot1.grid(row=7,column=3,pady=10)
        payroll_rep1.grid(row=8,column=3,pady=10)
        total_amt1.grid(row=9,column=3,pady=10)

        payroll_id1.delete(0,END)
        emp_id1.delete(0,END)
        trans_id1.delete(0,END)
        acc_num1.delete(0,END)
        dot1.delete(0,END)
        payroll_rep1.delete(0,END)
        total_amt1.delete(0,END)

        payroll_id1.focus_set()

        payroll_add = tk.Button(self,text="ADD PAYROLL",command= lambda: add_payroll(PAYROLL_ID,EMP_ID,TRANS_ID,ACC_NUM,DOT,PAYROLL_REP,TOTAL_AMT))
        payroll_add.grid(row=11,column=2,columnspan=10)

        def add_payroll(i,e,t,a,d,p,ta):
            if(len(d.get()) == 0 or len(p.get()) == 0 or len(str(a.get())) == 0   or len(str(e.get())) == 0 or 
            len(str(ta.get())) == 0 or len(str(t.get())) == 0 or len(str(i.get())) == 0):
                empty_label = tk.Label(self,text="PLEASE FILL ALL THE DETAILS",foreground="Black",background="light green",font=("",10,'italic'))
                empty_label.grid(row = 13,column=2,columnspan=10)

            else:
                controller.show_frame("Adminpanel")
                payroll_id1.delete(0,END)
                emp_id1.delete(0,END)
                trans_id1.delete(0,END)
                acc_num1.delete(0,END)
                dot1.delete(0,END)
                payroll_rep1.delete(0,END)
                total_amt1.delete(0,END)
                












