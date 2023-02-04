import tkinter as tk
from tkinter.constants import END

class Addpaygrade(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')


        PAYGRADE_ID = tk.IntVar()
        EMP_ID = tk.IntVar()
        JOB_TITLE = tk.StringVar()
        JOB_GRADE = tk.StringVar()
        BASIC_SAL = tk.IntVar()
        BONUS = tk.IntVar()
        TAXES = tk.IntVar()
        PENALTIES = tk.IntVar()
        FINAL_SAL = tk.IntVar()
        ALLOWANCES = tk.IntVar()
        TOTAL_AMT = tk.IntVar()

        back_button = tk.Button(self,text="Back",command=lambda:controller.show_frame("Adminpanel"))
        back_button.grid(row=0,column=1,pady=10,padx=10)

        paygrade_page = tk.Label(self,text="PAYGRADE PAGE",foreground="red",background='light green',font=('',15,'bold'))
        paygrade_page.grid(row = 0,column=3,pady=10)

        
        paygrade_id = tk.Label(self,text="paygrade ID")
        emp_id = tk.Label(self,text="employee ID")
        job_title = tk.Label(self,text="job Title")
        job_grade = tk.Label(self,text="job Grade")
        basic_sal = tk.Label(self,text="basic Salary")
        bonus = tk.Label(self,text="bonus")
        taxes = tk.Label(self,text="taxes")
        penalties = tk.Label(self,text="penalties")
        final_sal = tk.Label(self,text="final Salary")
        allowances = tk.Label(self,text="allowances")
        total_amt = tk.Label(self,text="total Amt")


        paygrade_id.grid(row=2,column=2,pady=10)
        emp_id.grid(row=3,column=2,pady=10)
        job_title.grid(row=4,column=2,pady=10)
        job_grade.grid(row=5,column=2,pady=10)
        basic_sal.grid(row=6,column=2,pady=10)
        bonus.grid(row=7,column=2,pady=10)
        taxes.grid(row=8,column=2,pady=10)
        penalties.grid(row=9,column=2,pady=10)
        final_sal.grid(row=10,column=2,pady=10)
        allowances.grid(row=11,column=2,pady=10)
        total_amt.grid(row=12,column=2,pady=10)


        paygrade_id1 = tk.Entry(self,textvariable=PAYGRADE_ID)
        emp_id1 = tk.Entry(self,textvariable=EMP_ID)
        job_title1 = tk.Entry(self,textvariable=JOB_TITLE)
        job_grade1 = tk.Entry(self,textvariable=JOB_GRADE)
        basic_sal1 = tk.Entry(self,textvariable=BASIC_SAL)
        bonus1 = tk.Entry(self,textvariable=BONUS)
        taxes1 = tk.Entry(self,textvariable=TAXES)
        penalties1 = tk.Entry(self,textvariable=PENALTIES)
        final_sal1 = tk.Entry(self,textvariable=FINAL_SAL)
        allowances1 = tk.Entry(self,textvariable=ALLOWANCES)
        total_amt1 = tk.Entry(self,textvariable=TOTAL_AMT)


        paygrade_id1.grid(row=2,column=3,pady=10)
        emp_id1.grid(row=3,column=3,pady=10)
        job_title1.grid(row=4,column=3,pady=10)
        job_grade1.grid(row=5,column=3,pady=10)
        basic_sal1.grid(row=6,column=3,pady=10)
        bonus1.grid(row=7,column=3,pady=10)
        taxes1.grid(row=8,column=3,pady=10)
        penalties1.grid(row=9,column=3,pady=10)
        final_sal1.grid(row=10,column=3,pady=10)
        allowances1.grid(row=11,column=3,pady=10)
        total_amt1.grid(row=12,column=3,pady=10)

        paygrade_id1.delete(0,END)
        emp_id1.delete(0,END)
        job_title1.delete(0,END)
        job_grade1.delete(0,END)
        basic_sal1.delete(0,END)
        bonus1.delete(0,END)
        taxes1.delete(0,END)
        penalties1.delete(0,END)
        final_sal1.delete(0,END)
        allowances1.delete(0,END)
        total_amt1.delete(0,END)


        paygrade_id1.focus_set()

        paygrade_add = tk.Button(self,text="ADD PAYGRADE",command= lambda: add_paygrade(PAYGRADE_ID,EMP_ID,JOB_TITLE,JOB_GRADE,BASIC_SAL,BONUS,TAXES,PENALTIES,FINAL_SAL,ALLOWANCES,TOTAL_AMT))
        paygrade_add.grid(row=14,column=2,columnspan=10)

        def add_paygrade(i,e,jt,jg,bs,b,t,p,fs,al,ta):
            if(len(jt.get()) == 0 or len(jg.get()) == 0 or len(str(i.get())) == 0 
            or len(str(e.get())) == 0 or len(str(bs.get())) == 0 or len(str(b.get())) == 0
             or len(str(t.get())) == 0 or len(str(p.get())) == 0 or len(str(fs.get())) == 0
             or len(str(al.get())) == 0 or len(str(ta.get())) == 0):
                empty_label = tk.Label(self,text="PLEASE FILL ALL THE DETAILS",foreground="Black",background="light green",font=("",10,'italic'))
                empty_label.grid(row = 16,column=2,columnspan=10)

            else:
                controller.show_frame("Adminpanel")
                paygrade_id1.delete(0,END)
                emp_id1.delete(0,END)
                job_title1.delete(0,END)
                job_grade1.delete(0,END)
                basic_sal1.delete(0,END)
                bonus1.delete(0,END)
                taxes1.delete(0,END)
                penalties1.delete(0,END)
                final_sal1.delete(0,END)
                allowances1.delete(0,END)
                total_amt1.delete(0,END)

