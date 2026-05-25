-- Show the 10 most recent sales (by sale_date, newest first).
-- Result: 10 rows returned.

SELECT *
FROM sales
ORDER BY sale_date DESC
LIMIT 10;