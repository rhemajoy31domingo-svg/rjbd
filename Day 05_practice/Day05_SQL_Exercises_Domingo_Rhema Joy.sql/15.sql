-- Show all sales from the NCR region, sorted by category (A-Z), then by total_amount (highest first).
-- Result: 27 rows returned.

SELECT *
FROM sales
WHERE region = 'NCR'
ORDER BY category ASC, total_amount DESC;