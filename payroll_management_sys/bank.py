import tkinter as tk
from tkinter.constants import END

class Addbank(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')

        ACC_NO = tk.IntVar()
        BENF_NAME = tk.StringVar()
        REM_NAME = tk.StringVar()
        EMP_ID = tk.IntVar()
        TRANS_ID = tk.IntVar()
        DOT = tk.StringVar()
        AMT_TRANS = tk.IntVar()

        back_button = tk.Button(self,text="Back",command=lambda:controller.show_frame("Adminpanel"))
        back_button.grid(row=0,column=1,pady=10,padx=10)

        bank_page = tk.Label(self,text="ADD BANK DETAILS",foreground="red",background='light green',font=('',15,'bold'))
        bank_page.grid(row = 0,column=3,pady=10)

        acc_no = tk.Label(self,text="account No")
        benf_name  = tk.Label(self,text="beneficiary Name")
        rem_name = tk.Label(self,text="remitter Name") 
        emp_id = tk.Label(self,text="employee ID")
        trans_id  = tk.Label(self,text="transaction ID")
        dot  = tk.Label(self,text="Date of Transaction")
        amt_trans  = tk.Label(self,text="amount Transferred")


        acc_no.grid(row=3,column=2,pady=10)
        benf_name.grid(row=4,column=2,pady=10)
        rem_name.grid(row=5,column=2,pady=10)
        emp_id.grid(row=6,column=2,pady=10)
        trans_id.grid(row=7,column=2,pady=10)
        dot.grid(row=8,column=2,pady=10)
        amt_trans.grid(row=9,column=2,pady=10)

        acc_no1 = tk.Entry(self,textvariable=ACC_NO)
        benf_name1 = tk.Entry(self,textvariable=BENF_NAME)
        rem_name1 = tk.Entry(self,textvariable=REM_NAME)
        emp_id1 = tk.Entry(self,textvariable=EMP_ID)
        trans_id1 = tk.Entry(self,textvariable=TRANS_ID)
        dot1 = tk.Entry(self,textvariable=DOT)
        amt_trans1 = tk.Entry(self,textvariable=AMT_TRANS)



        acc_no1.grid(row=3,column=3,pady=10)
        benf_name1.grid(row=4,column=3,pady=10)
        rem_name1.grid(row=5,column=3,pady=10)
        emp_id1.grid(row=6,column=3,pady=10)
        trans_id1.grid(row=7,column=3,pady=10)
        dot1.grid(row=8,column=3,pady=10)
        amt_trans1.grid(row=9,column=3,pady=10)

        acc_no1.delete(0,END)
        emp_id1.delete(0,END)
        trans_id1.delete(0,END)
        amt_trans1.delete(0,END)

        acc_no1.focus_set()

        bank_add = tk.Button(self,text="ADD BANK",command= lambda: add_bank(ACC_NO,BENF_NAME,REM_NAME,EMP_ID,TRANS_ID,DOT,AMT_TRANS))
        bank_add.grid(row=11,column=2,columnspan=10)

        def add_bank(a,b,r,e,t,d,am):
            if(len(b.get()) == 0 or len(r.get()) == 0 or len(str(a.get())) == 0  or 
            len(d.get()) == 0  or len(str(e.get())) == 0 or 
            len(str(am.get())) == 0 or len(str(t.get())) == 0):
                empty_label = tk.Label(self,text="PLEASE FILL ALL THE DETAILS",foreground="Black",background="light green",font=("",10,'italic'))
                empty_label.grid(row = 13,column=2,columnspan=10)


            else:
                controller.show_frame("Adminpanel")
                acc_no1.delete(0,END)
                emp_id1.delete(0,END)
                trans_id1.delete(0,END)
                amt_trans1.delete(0,END)
                benf_name1.delete(0,END)
                rem_name1.delete(0,END)
                dot1.delete(0,END)






