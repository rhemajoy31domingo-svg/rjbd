-- Show all sales where the city is IN ('Makati', 'Quezon City', 'Pasig').
-- Result: 19 rows returned.
SELECT *
FROM sales
WHERE city IN ('Makati', 'Quezon City', 'Pasig');