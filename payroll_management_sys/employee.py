import tkinter as tk
from tkinter.constants import END

class Addemployee(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='light green')
        self.controller = controller
        self.controller.state('zoomed')

        EMP_ID = tk.IntVar()
        EMP_FNAME = tk.StringVar()
        EMP_MNAME = tk.StringVar()
        EMP_LNAME = tk.StringVar()
        EMP_GENDER = tk.StringVar()
        DOB =tk.StringVar()
        DOJ = tk.StringVar()
        AGE = tk.IntVar()
        COMP_NAME = tk.StringVar()
        DEPT_NAME = tk.StringVar()
        JOB_TITLE = tk.StringVar()
        PH_NO = tk.IntVar()
        PROJECT_TITLE = tk.StringVar()
        ADDRESS = tk.StringVar()
        PIN_CODE = tk.IntVar()

        back_button = tk.Button(self,text="Back",command=lambda:controller.show_frame("Adminpanel"))
        back_button.grid(row=0,column=1,pady=10,padx=10)

        employee_page = tk.Label(self,text="ADD EMPLOYEE DETAILS",foreground="red",background='light green',font=('',15,'bold'))
        employee_page.grid(row = 0,column=3,pady=10)


        emp_id = tk.Label(self, text="employee ID")
        emp_fname = tk.Label(self, text="employee Fname")
        emp_mname = tk.Label(self, text="employee Mname")
        emp_lname = tk.Label(self, text="employee Lname")
        emp_gender = tk.Label(self, text ="employee Gender")
        emp_dob = tk.Label(self, text="employee DOB(yyyy-mm-dd)")
        emp_doj = tk.Label(self, text="employee DOJ(yyyy-mm-dd)")
        emp_age = tk.Label(self, text="employee Age")
        comp_name = tk.Label(self, text="company Name")
        dept_name = tk.Label(self, text="department Name")
        job_title = tk.Label(self, text="job Title")
        ph_no = tk.Label(self, text="phn No")
        project_title = tk.Label(self, text="project Title")
        address = tk.Label(self, text=" employee address")
        pin_code = tk.Label(self, text="pin Code")



        emp_id.grid(row=2,column=2,pady=10)
        emp_fname.grid(row=3,column=2,pady=10)
        emp_mname.grid(row=4,column=2,pady=10)
        emp_lname.grid(row=5,column=2,pady=10)
        emp_gender.grid(row=6,column=2,pady=10)
        emp_dob.grid(row=7,column=2,pady=10)
        emp_doj.grid(row=8,column=2,pady=10)
        emp_age.grid(row=9,column=2,pady=10)
        comp_name.grid(row=10,column=2,pady=10)
        dept_name.grid(row=11,column=2,pady=10)
        job_title.grid(row=12,column=2,pady=10)
        ph_no.grid(row=13,column=2,pady=10)
        project_title.grid(row=14,column=2,pady=10)
        address.grid(row=15,column=2,pady=10)
        pin_code.grid(row=16,column=2,pady=10)

        emp_id1 = tk.Entry(self,textvariable=EMP_ID)
        emp_fname1 = tk.Entry(self,textvariable=EMP_FNAME)
        emp_mname1 = tk.Entry(self,textvariable=EMP_MNAME)
        emp_lname1 = tk.Entry(self,textvariable=EMP_LNAME)
        emp_gender1 = tk.Entry(self,textvariable=EMP_GENDER)
        emp_dob1 = tk.Entry(self,textvariable=DOB)
        emp_doj1 = tk.Entry(self,textvariable=DOJ)
        emp_age1 = tk.Entry(self,textvariable=AGE)
        comp_name1 = tk.Entry(self,textvariable=COMP_NAME)
        dept_name1 = tk.Entry(self,textvariable=DEPT_NAME)
        job_title1 = tk.Entry(self,textvariable=JOB_TITLE)
        ph_no1 = tk.Entry(self,textvariable=PH_NO)
        project_title1 = tk.Entry(self,textvariable=PROJECT_TITLE)
        address1 = tk.Entry(self,textvariable=ADDRESS)
        pin_code1 = tk.Entry(self,textvariable=PIN_CODE)


        emp_id1.grid(row=2,column=3,pady=10)
        emp_fname1.grid(row=3,column=3,pady=10)
        emp_mname1.grid(row=4,column=3,pady=10)
        emp_lname1.grid(row=5,column=3,pady=10)
        emp_gender1.grid(row=6,column=3,pady=10)
        emp_dob1.grid(row=7,column=3,pady=10)
        emp_doj1.grid(row=8,column=3,pady=10)
        emp_age1.grid(row=9,column=3,pady=10)
        comp_name1.grid(row=10,column=3,pady=10)
        dept_name1.grid(row=11,column=3,pady=10)
        job_title1.grid(row=12,column=3,pady=10)
        ph_no1.grid(row=13,column=3,pady=10)
        project_title1.grid(row=14,column=3,pady=10)
        address1.grid(row=15,column=3,pady=10)
        pin_code1.grid(row=16,column=3,pady=10)

        emp_id1.delete(0,END)
        emp_age1.delete(0,END)
        ph_no1.delete(0,END)
        pin_code1.delete(0,END)

        emp_id.focus_set()

        emp_add = tk.Button(self,text="ADD EMPLOYEE",command= lambda: add_emp(EMP_ID,EMP_FNAME,EMP_MNAME,
        EMP_LNAME,EMP_GENDER,DOB,DOJ,AGE,COMP_NAME,DEPT_NAME,JOB_TITLE,PH_NO,PROJECT_TITLE,ADDRESS,PIN_CODE))
        emp_add.grid(row=18,column=2,columnspan=10)

        def add_emp(i,f,m,l,g,db,dj,a,cn,dn,j,ph,pt,ad,pc):
            if(len(f.get()) == 0 or len(m.get()) == 0 or len(str(a.get())) == 0 or
            len(l.get()) == 0 or len(g.get()) == 0 or len(str(ph.get())) == 0 or
            len(db.get()) == 0 or len(dj.get()) == 0 or len(str(i.get())) == 0 or
            len(cn.get()) == 0 or len(dn.get()) == 0 or len(str(pc.get())) == 0 or
            len(j.get()) == 0 or len(pt.get()) == 0 or len(ad.get()) == 0):
                empty_label = tk.Label(self,text="PLEASE FILL ALL THE DETAILS",foreground="Black",background="light green",font=("",10,'italic'))
                empty_label.grid(row = 20,column=2,columnspan=10)

            else:
                controller.show_frame("Adminpanel")
                emp_id1.delete(0,END)
                emp_age1.delete(0,END)
                ph_no1.delete(0,END)
                pin_code1.delete(0,END)
                emp_fname1.delete(0,END)
                emp_mname1.delete(0,END)
                emp_lname1.delete(0,END)
                emp_gender1.delete(0,END)
                emp_dob1.delete(0,END)
                emp_doj1.delete(0,END)
                comp_name1.delete(0,END)
                dept_name1.delete(0,END)
                job_title1.delete(0,END)
                project_title1.delete(0,END)
                address1.delete(0,END)


        

