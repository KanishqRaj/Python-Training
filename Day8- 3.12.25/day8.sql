create table students (
	student_id INT auto_increment primary key,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100),
    age INT,
    city varchar(50)
    );
    
    Insert into students (first_name , last_name, email, age, city)
    Values
    ('Kanishq','Raj','kanishq@gmail.com',22,'Coimbatore'),
    ('Synthia','Evangeline','synthia@example.com',23,'Kuniyamuthur'),
    ('Anto','Samson','anto@late.com',23,'ooty');
    
    SELECT * From students
    
    
    Select first_name, last_name, city
    from students;
    
    select * from students where city = 'Delhi';
    
    Select * from students Order By age desc;
    
delete from students where student_id = 2;

delete from students where city = 'Ooty';

drop table students;

drop database college_db;

    