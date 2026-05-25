-- Show all sales from NCR where the total_amount is greater than ₱10,000.
-- result: 8 rows returned

select *
from sales
where region = 'NCR' and total_amount > 10000;

