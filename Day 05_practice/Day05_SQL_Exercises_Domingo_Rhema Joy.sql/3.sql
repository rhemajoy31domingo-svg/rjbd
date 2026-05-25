-- Show all sales that are NOT in the Accessories category.
-- Result: 26 rows returned.

SELECT *
FROM sales
WHERE category <> 'Accessories';