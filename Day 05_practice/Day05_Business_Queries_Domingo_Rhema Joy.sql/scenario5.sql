-- The finance team needs a report of all sales from Q2 2025 
-- (April 1 to June 30) that were paid via GCash.
-- Show the sale_date, customer_name, product_name, total_amount, 
-- and payment_method. Sort by
-- sale_date.

-- Table to be called is "sales"
-- Fields to be queried are "sale_date", "customer_name", "product_name", "total_amount", and "payment_method"
-- Operation is AND because we are looking for sales that were paid via GCash AND occurred between April 1 and June 30, 2025.

SELECT sale_date, customer_name, product_name, total_amount, payment_method
FROM sales
WHERE payment_method = 'GCash' AND sale_date >= '2025-04-01' AND sale_date <= '2025-06-30'