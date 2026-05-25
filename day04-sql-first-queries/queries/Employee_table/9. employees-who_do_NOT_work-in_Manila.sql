-- Show the first_name, last_name, and city of employees who do NOT work in Manila
-- result: 15 rows
Select first_name, last_name, city
From Employees
Where city != 'Manila';