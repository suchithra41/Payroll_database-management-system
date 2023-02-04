# Payroll_database-management-system
Problem statement
Payroll Management System is computer-operated system
designed to record monitor and manage employee’s payroll matters in any Organization. With an increase in the number of Employees and organizations, the financial management of the organization is becoming a complex issue. Payroll management system plays a key role in improving the organization’s productivity by computerizing some of its financial functions. It also helps to overcome the limitations of the current system and will play a key role in minimizing human strain and errors.
We create the database design for payroll management system considering following instances:-
* An ADMIN have access to payroll management system who
manages everything and has a unique id, username, password,
email id and a default user type.
* An EMPLOYEE with unique id, Fname, Mname, Lname,
gender, age, job title, date of birth, date of joining , mobile number, mail id,address, job department, project title working in
a COMPANY that has several DEPARTMENTS with a unique
company id, company name, address and phone number.
* The EMPLOYEE should be at least 20 years old and at most
60 years old.
* Each EMPLOYEE works in a certain DEPARTMENT. The
DEPARTMENT has a unique dept_id and name, job title.
* Each EMPLOYEE may or may not be working on a PROJECT.
The PROJECT has a project id, project title, due date.
* EMPLOYEE holds a BANK ACCOUNT which has details such
as account number, beneficiary name, remitter’s name,
employee id, transaction id, date of transaction,amount.
* There is a PAYGRADE system that determines the PAYROLL
of the EMPLOYEE, it has attributes namely paygrade_id, employee_id,job_title,job_grade,basic_salary,bonuses,taxes,pe nalties,final_salaray,allowances,total amount.
* EMPLOYEE’S PAYROLL has Payroll id,employee id, job id, salary id, leave id, transaction id, account number, total_amount, date of transaction, pay roll report.

ER Toll Usage
The ERD tool that we have used is an online ERD-making tool called ERDPlus.
ERDPlus is a web-based database modeling tool that lets you quickly and easily create

* Entity Relationship Diagrams (ERDs)
* Relational Schemas (Relational Diagrams)
* Star Schemas (Dimensional Models) More features
* Automatically convert ER Diagrams into Relational Schemas ● Export SQL
* Export diagrams as a PNG
* Save diagrams safely on our server
ERDPlus enables drawing standard ERD components.
* Entities
* Attributes
* Relationships
The notation supports drawing regular and weak entities, various types of attributes (regular, unique, multi-valued, derived, composite, and
optional), and all possible cardinality constraints of relationships (mandatory-many, optional-many, mandatory-one and optional-one).
ERDPlus enables drawing standard Relational Schema components
* Tables (Relations)
* Table Columns (including Primary and Foreign Keys)
* Referential Integrity Constraint Lines (pointing from a Foreign Key to the Primary Key it refers to)
The tool supports quick creation of foreign keys and referential integrity lines by simple click-point-connect actions. This simplifies and quickens the process of creating relational schemas.
Convert ER Diagrams
ERDPlus enables automatic conversion of ER Diagrams to Relational Schemas with one click of a button. This vastly speeds up the process of creating a Relational Schema based on an ER Diagram.
ERDPlus enables drawing Star Schema components: ● Fact Tables (Facts)
* Dimension Tables (Dimensions)
The notation distinguishes fact tables from dimension tables by using a thicker frame around fact tables. This makes star schema diagrams easier to interpret. As with relational schemas, the tool supports quick creation of foreign keys and referential integrity lines by simple click-point- connect actions. This simplifies and quickens the process of creating star schemas.
