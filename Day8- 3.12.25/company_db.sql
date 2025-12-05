create database company_db;
use company_db;

create table employees(
	emp_id INT PRIMARY KEY,
    emp_name varchar(50),
    email varchar(50),
    salary int,
    dept_id int null
);

create table departments(
	dept_id int primary key,
    dept_name varchar(50),
    location varchar(50)
);

INSERT INTO departments (dept_id, dept_name, location)
VALUES
(10, 'HR', 'Mumbai'),
(20, 'Finance', 'Delhi'),
(30, 'IT', 'Bangalore'),
(40, 'Marketing', 'Chennai'),
(50, 'Admin', 'Hyderabad');   -- no employees for dept 50
 
 
INSERT INTO employees (emp_id, emp_name, email, salary, dept_id)
VALUES
(101, 'Aisha Khan', 'aisha@company.com', 60000, 10),
(102, 'Rahul Sharma', 'rahul@company.com', 72000, 20),
(103, 'Meera Iyer', 'meera@company.com', 50000, 30),
(104, 'Imran Ali', 'imran@company.com', 65000, NULL),  -- no department
(105, 'Sanjay Patel', 'sanjay@company.com', 45000, NULL), -- no department
(106, 'David John', 'david@company.com', 90000, 40);


select e.emp_id, e.emp_name, d.dept_name, d.location
from employees e
Inner join departments d
on e.dept_id = d.dept_id;

select e.emp_id, e.emp_name, d.dept_name
from employees e
Left join departments d
on e.dept_id = d.dept_id;

select e.emp_id, e.emp_name, d.dept_name
from employees e
Right join departments d
on e.dept_id = d.dept_id;


##FULL JOIN
select e.emp_id, e.emp_name, d.dept_name
from employees e
Left join departments d
on e.dept_id = d.dept_id

UNION

select e.emp_id, e.emp_name, d.dept_name
from employees e
Right join departments d
on e.dept_id = d.dept_id;


select e.emp_name , d.dept_name
from employees e 
Cross join departments d;
