-- Show all sales from Manila OR Cebu City.
-- Result: 18 rows returned
SELECT *
FROM sales
WHERE city IN ('Manila', 'Cebu City');