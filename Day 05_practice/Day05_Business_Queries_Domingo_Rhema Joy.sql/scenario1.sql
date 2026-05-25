-- The warehouse manager needs to know which items are running low. 
-- Show all inventory items where
-- quantity_on_hand is LESS THAN or EQUAL TO the reorder_level. 
-- Sort by quantity_on_hand (lowest first).

-- TABLE to be called is "inventory"
-- FIELD to be queried "quantity_on_hand"
-- WHEN SORTING or arrangement is define in SQL that is ORDER BY

SELECT * FROM inventory
WHERE quantity_on_hand <= reorder_level
ORDER BY quantity_on_hand ASC;