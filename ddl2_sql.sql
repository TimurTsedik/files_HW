CREATE TABLE IF NOT EXISTS employees (
    id serial PRIMARY KEY, 
    employee_name varchar(100) NOT NULL, 
    department integer NOT NULL
    upper_manager integer NOT NULL);
    
 CREATE TABLE IF NOT EXISTS managers (
    manager_self integer NOT NULL
    upper_manager_for integer NOT null
    CONSTRAINT managers_pk PRIMARY KEY (manager_self, upper_manager_for));

   CREATE TABLE IF NOT EXISTS departments (
    id serial PRIMARY KEY, 
    department_title varchar(100) NOT NULL, 
    description varchar(300));
