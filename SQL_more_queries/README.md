SQL Query Basics

Table of Contents
How to create a new MySQL user
How to manage privileges for a user to a database or table
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve data from multiple tables in one request
What are subqueries
What are JOIN and UNION

How to create a new MySQL user
To create a new MySQL user, use the CREATE USER statement. Replace 'newuser' with the desired username and 'localhost' with the appropriate host.

sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
How to manage privileges for a user to a database or table
Grant privileges to a user using the GRANT statement. Below is an example of granting all privileges on a specific database to the 'newuser'.

sql
GRANT ALL PRIVILEGES ON mydatabase.* TO 'newuser'@'localhost';
To revoke privileges, use the REVOKE statement.

sql
REVOKE ALL PRIVILEGES ON mydatabase.* FROM 'newuser'@'localhost';
What’s a PRIMARY KEY
A PRIMARY KEY is a unique identifier for a record in a table. It must contain unique values, and by default, it cannot have NULL values.

Example:

sql
  name VARCHAR(50),
  salary DECIMAL(10,2)
);
What’s a FOREIGN KEY
A FOREIGN KEY is a field that refers to the PRIMARY KEY in another table. It establishes a link between the two tables, enforcing referential integrity.

Example:

sql
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  product_id INT,
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);
How to use NOT NULL and UNIQUE constraints
Use NOT NULL to ensure a column cannot have NULL values and UNIQUE to ensure all values in a column are distinct.

Example:

sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(50) NOT NULL
);
How to retrieve data from multiple tables in one request
Use JOIN to retrieve data from multiple tables based on a common column. Example using INNER JOIN:

sql
SELECT employees.id, employees.name, departments.department_name
FROM employees
JOIN departments ON employees.department_id = departments.id;
What are subqueries
Subqueries are queries embedded within other queries. They allow for operations on the result set of one query and using that result in another query.

Example:

sql
SELECT id, name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
What are JOIN and UNION
JOIN is used to combine rows from two or more tables based on a related column. Example using INNER JOIN:

sql
SELECT sales.order_id, sales.product, customers.customer_name
FROM sales
JOIN customers ON sales.customer_id = customers.customer_id;
UNION is used to combine the result sets of two or more SELECT statements.

Example:

sql
SELECT column1 FROM table1
UNION
SELECT column1 FROM table2;

