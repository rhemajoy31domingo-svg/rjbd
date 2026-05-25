-- A customer called asking about keyboard products. 
-- Search the inventory table for all items where
-- item_name contains the word 'Keyboard' (use LIKE). 
-- Show the item_name, warehouse,
-- quantity_on_hand, and unit_cost.

-- Table to be called is "inventory"
-- Field to be queried is "item_name"
-- Operation is LIKE because we are looking for a specific pattern in the item_name field.

SELECT item_name, warehouse, quantity_on_hand, unit_cost
FROM inventory
WHERE item_name LIKE '%Keyboard%';

