-- Show all products that are NOT in the Accessories category
-- results: 8 rows
SELECT *FROM products
WHERE category != 'Accessories';