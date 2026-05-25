-- Show the top 5 most expensive sales (highest total_amount).
-- Result: 5 rows returned.
SELECT *
FROM sales
ORDER BY total_amount DESC
LIMIT 5;