create table employees (
    id int primary key,
    name varchar(50),
    datetime varchar(50),
    department_id int,
    job_id int null
);

create table departments (
    id int primary key,
    deparment varchar(50)
);

create table jobs (
    id int primary key,
    job varchar(50)
);