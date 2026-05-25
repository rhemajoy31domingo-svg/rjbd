-- Show all sales where the product_name starts with 'Laptop' (use LIKE).
-- Result: 7 rows returned.
SELECT *
FROM sales
WHERE product_name LIKE 'Laptop%';