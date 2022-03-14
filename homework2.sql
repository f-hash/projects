SHOW DATABASES;
Use employees; 
show tables; 
#4
select * from employees;
#5
select * from dept_manager; 
#6
select 
  *
from departments
limit 5; 
#8
select 
*
from employees natural join salaries 
where salary > 100000;
#9
select 
*
from salaries
where salary <= 30000
limit 5; #use semicolons to end the whole command 

 # 10 
 select emp_no, from_date, to_date from dept_emp #union must have the same column id similar to join 
 where dept_no = 'd002'
 union
 select 
   emp_no, from_date, to_date #no comma before the from statement 
 from salaries 
 where salary > 30000
 limit 5;

#11
select dept_manager.emp_no, employees.first_name, employees.last_name, salaries.salary from employees
inner join dept_manager on  employees.emp_no = dept_manager.emp_no 
inner join salaries on employees.emp_no = salaries.emp_no
where salary > 30000 and first_name = "John" and dept_no = "d002";

#12 
select emp_no, from_date, to_date from dept_manager #union must have the same column id similar to join 
 union
select 
  emp_no, from_date, to_date #no comma before the from statement 
 from salaries 
 where salary <= 30000
 limit 5;
 
 #13
select distinct salaries.emp_no , employees.first_name, employees.last_name #calling attributes this way makes it easier 
 from salaries
inner join employees on  salaries.emp_no = employees.emp_no
 inner join dept_manager on dept_manager.emp_no = employees.emp_no
 where salary > 50000 
 limit 5;

 
 
 #14
select distinct employees.emp_no, dept_manager.dept_no , employees.first_name, employees.last_name
 from dept_manager
 join salaries on  dept_manager.emp_no = salaries.emp_no #table 1
 join employees on dept_manager.emp_no = employees.emp_no #table2
 where dept_no = "d002"  and salary > 50000
 limit 5;


 
 
 
 
 #15
 select count(emp_no) from employees;
 
 #16
 select employees.first_name, employees.last_name, salaries.salary 
 from salaries 
 inner join employees on salaries.emp_no = employees.emp_no
 order by salary DESC
 limit 5; 
 
 #17
 
select departments.dept_name, dept_emp.emp_no, salaries.salary, employees.first_name, employees.last_name
from departments natural join dept_emp
natural join employees
natural join salaries
order by salary DESC;



#18 
select
 * 
from employees
order by hire_date DESC limit  1 ; 

#19 
 select
 *
from employees
order by hire_date ASC limit  1;
 
#20
select distinct title 
 
from titles; 
 
#21 
select 
count(gender)
from employees 
where gender = "M"; 

#22
select 
sum(case When gender = "M" then 1 else 0 end) / count(*) as male_gender, 
sum(case When gender = "F" then 1 else 0 end) / count(*) as female
from employees; 

#23 
select avg(salary) from salaries natural join employees where gender ="M";  #63838.1556
select avg(salary) from salaries natural join employees where gender ="F"; #63769.6032

#24
select 
*
from dept_manager natural join employees
order by from_date 
limit 1;

#25
select dept_no, emp_no, count(dept_no) 
from dept_manager 
group by dept_no 
having count(dept_no) > 1; #having greater than one

#tester group by
select dept_no, count(emp_no), count(dept_no) 
from dept_emp
group by emp_no
order by emp_no DESC; # you have to order based on count(emp_no) and desc is highest to low

#26
select * from dept_emp where dept_no is NULL;

#29
select dept_no, count(emp_no) 
from dept_emp where dept_no = "d002";

#30
select dept_name from departments;
#31
select * from employees 
order by birth_date DESC
limit 1; 

#32
select * from employees 
order by birth_date ASC
limit 1; 

#33
alter TABLE employees
  add column ssn int NOT NULL;
  select * from employees;

 

#34 
insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
values (‘777777’, ‘1980-01-01’, "Steve", "Smith", ‘M’, ‘2018-10-30’);

 
select * from employees where last_name = "Smith";

#35
select dept_no, count(emp_no)
from dept_emp
group by dept_no
order by count(emp_no) DESC; # you have to order based on count(emp_no) and desc is highest to low 

#36
select dept_no, count(emp_no)
from dept_emp
group by dept_no
order by count(emp_no) asc;

#37 

select 
* 
from dept_emp natural join salaries
where dept_no = "d001" 
order by salary desc;

delete from employees where emp_no = "66430";
select 
* 
from dept_emp natural join salaries
where dept_no = "d001" 
order by salary desc;
delete from employees where max(salary) = (select * from salaries inner join dept_emp.emp_no on salaries.emp_no = dept_emp.emp_no where dept_no = "d001" )
;#38 
select emp_no from salaries where salary = null;

#39
Create table dependents(
    dependent_id int, 
    first_name varchar(255),
    last_name varchar(255), 
    ssn int,
    relationship varchar(255) 
); 
select * from dependents;
 


