-- Show the first_name, position, and salary of employees in the Sales department
-- result: 5 rows
select first_name, position, salary
from Employees
where department = 'Sales';