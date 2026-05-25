-- Show all sales where the product_name contains 'USB' anywhere in the name.
-- Result: 6 rows returned.
SELECT *
FROM sales
WHERE product_name LIKE '%USB%';