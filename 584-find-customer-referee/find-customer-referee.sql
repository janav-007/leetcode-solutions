SELECT customer.name
FROM customer
WHERE customer.referee_id <> 2 OR customer.referee_id IS NULL;