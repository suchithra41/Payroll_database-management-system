CREATE TABLE users(
user_id INT NOT NULL UNIQUE,
username VARCHAR(30) NOT NULL, password VARCHAR(30),
email_id VARCHAR(60) UNIQUE,
user_type VARCHAR(30) DEFAULT 'ADMIN',
CONSTRAINT PK_users PRIMARY KEY(user_id) );
CREATE TABLE company(
comp_id INT NOT NULL UNIQUE,
comp_addr VARCHAR(50) NOT NULL, comp_name VARCHAR(50) NOT NULL unique, comp_number INT,
CONSTRAINT PK_company PRIMARY KEY(comp_id) );
CREATE TABLE department(
dept_id INT NOT NULL UNIQUE,
dept_name VARCHAR(30) NOT NULL UNIQUE, comp_name varchar(30) not null,
dept_size int not null,
dept_roomno int not null,
dept_head varchar(30) not null,
CONSTRAINT PK_department PRIMARY KEY(dept_id), CONSTRAINT FK_comp_name FOREIGN KEY(comp_name) references company(comp_name)
);
CREATE TABLE project(
project_id INT NOT NULL UNIQUE, project_title VARCHAR NOT NULL UNIQUE, due_date date,
CONSTRAINT PK_project PRIMARY KEY(project_id) );
CREATE TABLE employee(
employee_id INT NOT NULL UNIQUE, fname VARCHAR(30) NOT NULL, mname VARCHAR(30) NOT NULL, lname VARCHAR(30) NOT NULL, gender char(1) NOT NULL,
dob DATE CHECK ( DOB > '1975-01-01' and dob < '2000-01-01'), doj DATE CHECK ( DOJ > DOB),
Age INT,
comp_name varchar(30),
dept_name VARCHAR(30), job_title VARCHAR(30),

ph_no INT NOT NULL UNIQUE, project_title VARCHAR(30), address VARCHAR(50),
pincode INT,
CONSTRAINT PK_employee PRIMARY KEY(employee_id), FOREIGN KEY(comp_name) references company(comp_name), FOREIGN KEY(dept_name) references department(dept_name), FOREIGN KEY(project_title) references project(project_title)
);
CREATE TABLE bank_account(
account_number INT NOT NULL UNIQUE, beneficiary_name VARCHAR(30) NOT NULL, remitter_name VARCHAR(30) NOT NULL, employee_id INT NOT NULL,
transaction_id INT NOT NULL UNIQUE, date_of_transaction DATE NOT NULL, amount_transferred INT NOT NULL,
CONSTRAINT PK_bank_account PRIMARY KEY(account_number), FOREIGN KEY(employee_id) references employee(employee_id)
);
CREATE TABLE paygrade(
paygrade_id INT NOT NULL UNIQUE, employee_id INT NOT NULL,
job_title VARCHAR(30) NOT NULL, job_grade VARCHAR(10) NOT NULL, basic_salary INT CHECK ( basic_salary > 0), bonus INT,
taxes INT,

penalties INT,
final_salary INT,
allowances INT,
total_amount INT NOT NULL,
CONSTRAINT PK_paygrade PRIMARY KEY(paygrade_id), FOREIGN KEY(employee_id) references employee(employee_id) );
CREATE TABLE payroll(
payroll_id INT NOT NULL UNIQUE, employee_id INT NOT NULL UNIQUE, transaction_id INT NOT NULL, account_number INT NOT NULL, date_of_transaction DATE NOT NULL, payroll_report VARCHAR(100) NOT NULL, total_amount INT NOT NULL,
CONSTRAINT PK_payroll PRIMARY KEY (payroll_id),
FOREIGN KEY(employee_id) references employee(employee_id), FOREIGN KEY(transaction_id) references bank_account(transaction_id), FOREIGN KEY(account_number) references bank_account(account_number)
);

#using INSERT statement to fill the database state

INSERT INTO USERS(user_id,username,password,email_id) VALUES
(9902,'steve01','324steg','steve01@gmail.com');
INSERT INTO USERS(user_id,username,password,email_id) VALUES
(001,???Tejas???,???1fttt2???, 'tejas11@gmail.com???);
INSERT INTO USERS(user_id,username,password,email_id) VALUES (002,???Arjun???,???4vf4w???,???arjun09@gmail.com???);
INSERT INTO USERS(user_id,username,password,email_id) VALUES (003,???Karan???,???gt5ef???,???karan55@gmail.com???);
INSERT INTO USERS(user_id,username,password,email_id) VALUES (004,???Ram???,???fgt42???,???ram65@gmail.com???);
INSERT INTO USERS(user_id,username,password,email_id) VALUES (005,???Jacob ???,???14gtt???,???jacob76@gmail.com???);
INSERT INTO USERS(user_id,username,password,email_id) VALUES (006,???Sudeep???,???1fr6d???,???sudeep@gmail.com???);
INSERT INTOUSERS(user_id,username,password,email_id) VALUES (007,???Suhan???,???1tr5t???,???suhan@gmail.com???);
INSERT INTO USERS(user_id,username,password,email_id) VALUES
(008,???Nancy???,???1gyu7???,???nancy@gmail.com???);
    
COMPANY
INSERT INTO COMPANY(comp_id,comp_addr,comp_name,comp_number) VALUES (0123,'texas USA','TESLA',990021);
INSERT INTO COMPANY(comp_id,comp_addr,comp_name,comp_number) VALUES (13555,???Amritsar???,???Jio???,45634745);
INSERT INTO COMPANY(comp_id,comp_addr,comp_name,comp_number) VALUES (74184,???TexasUSA???,???Google???,45637547);
INSERT INTO COMPANY(comp_id,comp_addr,comp_name,comp_number) VALUES (13455,???Germany???,???Spacex???,53464763);
INSERT INTO COMPANY(comp_id,comp_addr,comp_name,comp_number) VALUES (83455,???Maharastra???,???Relaince???,45363464);
INSERT INTO COMPANY(comp_id,comp_addr,comp_name,comp_number) VALUES (74884,???Banglore???,???swiggy???,43636633);
INSERT INTO COMPANY(comp_id,comp_addr,comp_name,comp_number) VALUES (93455,???France???,???Microsoft???,36773346);
INSERT INTO COMPANY(comp_id,comp_addr,comp_name,comp_number) VALUES (17455,???Chennai???,???Zomato???,364477344);
INSERT INTO COMPANY(comp_id,comp_addr,comp_name,comp_number) VALUES (76884,???Kolkata???,???Amazon???,346737344);
 
DEPARTMENT
INSERT INTO DEPARTMENT(dept_id,dept_name,comp_name,dept_size,dept_roomno, dept_head) VALUES (0767,'Management','TESLA',20,34,'manak S agarwal');
INSERT INTO DEPARTMENT(dept_id,dept_name,comp_name,dept_size,dept_roomno,de pt_head) VALUES (00012,???delivery???,???swiggy???,20,30,???Mayank s agarwal???);
INSERT INTO DEPARTMENT(dept_id,dept_name,comp_name,dept_size,dept_roomno,de pt_head) VALUES (00022,???development???,???Jio???,25,34,???Andrew???);
INSERT INTO DEPARTMENT(dept_id,dept_name,comp_name,dept_size,dept_roomno,de pt_head) VALUES (00032,???research???,???Spacex???,18,28,???Mattew???);
INSERT INTO DEPARTMENT(dept_id,dept_name,comp_name,dept_size,dept_roomno,de pt_head) VALUES (00012,???sales???,???zomato???,40,44,???Sundar pichai???);
INSERT INTO DEPARTMENT(dept_id,dept_name,comp_name,dept_size,dept_roomno,de pt_head) VALUES (00234,???testing???,???Microsoft???,25,10,???Amith yadav???);
INSERT INTO DEPARTMENT(dept_id,dept_name,comp_name,dept_size,dept_roomno,de pt_head) VALUES (03565,???inquiry???,???Goolge???,50,21,???Mohan r???);
INSERT INTO DEPARTMENT(dept_id,dept_name,comp_name,dept_size,dept_roomno,de pt_head) VALUES (23425,???production???,???Amazon???,15,05,???Akshay r???);
INSERT INTO DEPARTMENT(dept_id,dept_name,comp_name,dept_size,dept_roomno,de pt_head) VALUES (00893,???accounting???,???Reliance???,23,43,???Anirudh b mitta???);

 PROJECT
INSERT INTO PROJECT(project_id,project_title,due_date) VALUES
(435,'Website management','2019-10-19');
INSERT INTO PROJECT(project_id,project_title,due_date) VALUES (2501,???app development???,"2020-12-10);
INSERT INTO PROJECT(project_id,project_title,due_date) VALUES (422,???food delivery???,"2021-02-08");
INSERT INTO PROJECT(project_id,project_title,due_date) VALUES (7124,???graphic designing???,"2023-12-23");
INSERT INTO PROJECT(project_id,project_title,due_date) VALUES (599,???system testing???,"2024-10-09");
INSERT INTO PROJECT(project_id,project_title,due_date) VALUES (244,???online marketing???,"2022-01-21");
INSERT INTO PROJECT(project_id,project_title,due_date) VALUES (753,???data entry???,"2021-10-05");
INSERT INTO PROJECT(project_id,project_title,due_date) VALUES (555,???client meetings???,"2023-10-04");
INSERT INTO PROJECT(project_id,project_title,due_date) VALUES (381,???documentation???,"2020-03-23");
EMPLOYEE
INSERT INTO EMPLOYEE(employee_id,fname,mname,lname,gender,dob,doj,age,comp _name,dept_name,job_title,ph_no,project_title,address,pincode) values (0104,'Manak','s','agarwal','M','1985-03-05','2003-05- 12',36,'TESLA','Management','Manager',3534657,'Website management','attibele benagluru',345753);
INSERT INTO EMPLOYEE(employee_id,fname,mname,lname,gender,dob,doj,age,comp_n
ame,dept_name,job_title,ph_no,project_title,address,pincode) values (2345,???Mohan???,???R ???,???nayak ???,???M ???,"1989-05-25","2010-11- 12",32,???swiggy???,???delivery???,???vice president???,3534657,???food delivery???,???kormangla???,945753);
INSERT INTO EMPLOYEE(employee_id,fname,mname,lname,gender,dob,doj,age,comp_n
ame,dept_name,job_title,ph_no,project_title,address,pincode) values (3484,??? Shankar???,???G???,???singh???,???M ???,"1989-03-05","2010-11- 12",32,???Jio???,???development???,???developer???,3534367,???app development???,???mount olympus???,325853);
INSERT INTO EMPLOYEE(employee_id,fname,mname,lname,gender,dob,doj,age,comp_n
ame,dept_name,job_title,ph_no,project_title,address,pincode) values (3548,??? Sudeep???,???n ???,???k ???,???F ???,"1998-03-05","2021-09- 12",23,???Relaince???,???accounting???,???ceo???,8554657,???data entry???,???washington dc???,340753);
INSERT INTO EMPLOYEE(employee_id,fname,mname,lname,gender,dob,doj,age,comp_n

ame,dept_name,job_title,ph_no,project_title,address,pincode) values (3847,??? Yang???,??? su ???,???woo ???,???F ???,"1985-03-05","2007-05- 12",36,???Zomato???,???sales???,???supervisor???,42783557,???online marketing???,???beijing???,849223);
INSERT INTO EMPLOYEE(employee_id,fname,mname,lname,gender,dob,doj,age,comp_n
ame,dept_name,job_title,ph_no,project_title,address,pincode) values (3871,??? Siri???,???S ???,???nayak ???,???F ???,"1995-06-16","2019-04- 12",26,???Google???,???inquiry???,???manager???,3467357,???client meetings???,???delhi???,245753);
INSERT INTO
EMPLOYEE(employee_id,fname,mname,lname,gender,dob,doj,age,comp_n ame,dept_name,job_title,ph_no,project_title,address,pincode) values (4534,??? Elon???,???musk???,???S ???,???M???,"1985-04-27","2006-05- 18",36,???Amazon???,???production???,???employee???,7774657,???online marketing???,???electronic city???,345753);
INSERT INTO EMPLOYEE(employee_id,fname,mname,lname,gender,dob,doj,age,comp_n
ame,dept_name,job_title,ph_no,project_title,address,pincode) values (7364,??? Jeff???,???X ???,???bezoz ???,???M ???,"1994-09-05","2018-08- 21",25,???Spacex???,???research???,???managing director???,3537087,???documentation???,???elctronic city???,399553);
INSERT INTO EMPLOYEE(employee_id,fname,mname,lname,gender,dob,doj,age,comp_n
ame,dept_name,job_title,ph_no,project_title,address,pincode) values (7556,??? Chandana???,???h ???,??? b???,???F ???,"1996-03-12","2021-06- 11",25,???Microsoft???,???testing???,???manager???,355565,???system testing???,???bombay???,378753);
 
BANK_ACCOUNT
INSERT INTO bank_account(account_number,beneficiary_name,remitter_name,employee _id,transaction_id,date_of_transaction,amount_transferred) VALUES (123123123,'Manak S agarwal','TESLA',0104,26378,'2021-10-29',35000);
INSERT INTO BANK ACCOUNT(account_number,beneficiary_name,remitter_name,employee_i
d,transaction_id,date_of_transaction,amount_transferred) VALUES (423546565,"mohan r nayak","harry",3548,6968745,"2021-10-29",95000);
INSERT INTO BANK ACCOUNT(account_number,beneficiary_name,remitter_name,employee_i
d,transaction_id,date_of_transaction,amount_transferred) VALUES
(436543766,"shankar g singh","lily ",7556,5685767,"2021-04-09",67000);
INSERT INTO BANK ACCOUNT(account_number,beneficiary_name,remitter_name,employee_i
d,transaction_id,date_of_transaction,amount_transferred) VALUES (465768954,"sudeep n k","julie",2345,1341546,"2021-08-02",100000);
INSERT INTO BANK ACCOUNT(account_number,beneficiary_name,remitter_name,employee_i
d,transaction_id,date_of_transaction,amount_transferred) VALUES (546576234,"yang su woo","kelvin",7364,2837656,"2021-09-12",26000);
INSERT INTO BANK ACCOUNT(account_number,beneficiary_name,remitter_name,employee_i
d,transaction_id,date_of_transaction,amount_transferred) VALUES (687546546,"siri s nayak","maria",3871,3564376,"2021-06-23",74000);
INSERT INTO BANK ACCOUNT(account_number,beneficiary_name,remitter_name,employee_i
d,transaction_id,date_of_transaction,amount_transferred) VALUES (726123453,"elon musk s","susan",3484,4826778,"2021-10-07",75000);

INSERT INTO BANK ACCOUNT(account_number,beneficiary_name,remitter_name,employee_i
d,transaction_id,date_of_transaction,amount_transferred) VALUES (745643651,"jeff x bezoz","eva",4534,3245746,"2021-10-22",45000);
INSERT INTO BANK ACCOUNT(account_number,beneficiary_name,remitter_name,employee_i
d,transaction_id,date_of_transaction,amount_transferred) VALUES (983756313,"chandana h b","olivia",3847,3786535,"2021-10-29",33000);
PAYGRADE
INSERT INTO PAYGRADE(paygrade_id,employee_id,job_title,job_grade,basic_salary,b onus,taxes,penalties,final_salary,allowances,total_amount) VALUES (6537,0104,'Manager','A',32000,3000,1000,1000,33000,2000,35000);
INSERT INTO PAYGRADE(paygrade_id,employee_id,job_title,job_grade,basic_salary,bo
nus,taxes,penalties,final_salary,allowances,total_amount) VALUES (2200,2345,"vice-president","B",45000,3000,7000,800,40200,600,40800);
INSERT INTO PAYGRADE(paygrade_id,employee_id,job_title,job_grade,basic_salary,bo
nus,taxes,penalties,final_salary,allowances,total_amount) VALUES (2205,3484,"developer","S",80000,10000,11000,200,78800,600,79400);
INSERT INTO PAYGRADE(paygrade_id,employee_id,job_title,job_grade,basic_salary,bo
nus,taxes,penalties,final_salary,allowances,total_amount) VALUES (2564,3847,"supervisor","A",50000,6000,9000,500,46500,600,471000);
INSERT INTO PAYGRADE(paygrade_id,employee_id,job_title,job_grade,basic_salary,bo
 
nus,taxes,penalties,final_salary,allowances,total_amount) VALUES (6065,3871,"manager","A",55000,10000,10000,800,54500,800,55500);
INSERT INTO PAYGRADE(paygrade_id,employee_id,job_title,job_grade,basic_salary,bo
nus,taxes,penalties,final_salary,allowances,total_amount) VALUES (6537,4534,"employee","A",32000,3000,1000,1000,33000,2000,35000);
INSERT INTO PAYGRADE(paygrade_id,employee_id,job_title,job_grade,basic_salary,bo
nus,taxes,penalties,final_salary,allowances,total_amount) VALUES (6789,7364,"managing director","d",10000,600,300,200,10100,600,10700);
INSERT INTO PAYGRADE(paygrade_id,employee_id,job_title,job_grade,basic_salary,bo
nus,taxes,penalties,final_salary,allowances,total_amount) VALUES (7045,7556,"manager","A",50000,15000,9000,500,55500,600,56100
);
INSERT INTO PAYGRADE(paygrade_id,employee_id,job_title,job_grade,basic_salary,bo
nus,taxes,penalties,final_salary,allowances,total_amount) VALUES (2056,3548,"ceo","A",30000,8000,4000,100,34900,600,35500);
PAYROLL
INSERT INTO PAYROLL(payroll_id,employee_id,transaction_id,account_number,date_ of_transaction,payroll_report,total_amount) VALUES (3267,0104,26378,123123123,'2021-10-29','employee has done a great job!!',35000);
INSERT INTO

PAYROLL(payroll_id,employee_id,transaction_id,account_number,date_of _transaction,payroll_report,total_amount) VALUES (23,3548,6968745,423546565,"2021-10-29","Success",35500);
INSERT INTO PAYROLL(payroll_id,employee_id,transaction_id,account_number,date_of
_transaction,payroll_report,total_amount) VALUES (34,1347,1983475,346524354,"2021-04-03","Success",47100);
INSERT INTO PAYROLL(payroll_id,employee_id,transaction_id,account_number,date_of
_transaction,payroll_report,total_amount) VALUES (35,3847,3786535,983756313,"2021-10-29","Success",56100);
INSERT INTO PAYROLL(payroll_id,employee_id,transaction_id,account_number,date_of
_transaction,payroll_report,total_amount) VALUES (43,7556,5685767,436543766,"2021-04-09","Success",40800);
INSERT INTO PAYROLL(payroll_id,employee_id,transaction_id,account_number,date_of
_transaction,payroll_report,total_amount) VALUES (45,4534,3245746,745643651,"2021-10-22","Success",10700);
INSERT INTO PAYROLL(payroll_id,employee_id,transaction_id,account_number,date_of
_transaction,payroll_report,total_amount) VALUES (54,3871,3564376,687546546,"2021-06-23","Success",55500);
INSERT INTO PAYROLL(payroll_id,employee_id,transaction_id,account_number,date_of
_transaction,payroll_report,total_amount) VALUES (63,2345,1341546,465768954,"2021-08-02","Success",79400);
INSERT INTO PAYROLL(payroll_id,employee_id,transaction_id,account_number,date_of
_transaction,payroll_report,total_amount) VALUES (87,3484,4826778,726123453,"2021-10-07","Success",35000);
