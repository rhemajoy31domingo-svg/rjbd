-- Show all products in the Accessories category with price less than ₱1,500
-- results: 4 rows  
SELECT *FROM products
WHERE category = 'Accessories' AND price < 1500;