-- Show the product_name, category, and stock_qty of products with stock less than 10
-- results: 4 rows
SELECT product_name, category, stock_qty
FROM products
WHERE stock_qty < 10;