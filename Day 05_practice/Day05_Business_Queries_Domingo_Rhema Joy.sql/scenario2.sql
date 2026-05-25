-- The marketing team wants to see all high-value sales (₱10,000 and above) from the NCR region. 
-- Show the customer_name, product_name, city, and total_amount. Sort by total_amount from highest to
-- lowest.

-- sales (10,000 and above) from the NCR region.
-- Logical [AND and OR]
-- false AND true = false
-- true AND false = false
-- true AND true = true
-- false AND false = false
-- false OR true = true
-- true OR false = true
-- true OR true = true
-- false OR false = false

SELECT customer_name, product_name, city, total_amount
FROM sales
WHERE region = 'NCR' AND total_amount >= 10000
ORDER BY total_amount DESC;