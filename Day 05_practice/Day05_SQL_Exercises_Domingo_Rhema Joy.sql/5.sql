-- Show all sales where the category is 'Electronics' AND the quantity is greater than 1.
-- Result: 1 rows returned
SELECT *
FROM sales
WHERE category = 'Electronics'
  AND quantity > 1;