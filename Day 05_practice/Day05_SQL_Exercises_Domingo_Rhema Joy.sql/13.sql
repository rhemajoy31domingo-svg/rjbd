-- Show all sales in the Electronics category, sorted by sale_date (oldest first).
-- Result: 16 rows returned.
SELECT *
FROM sales
WHERE category = 'Electronics'