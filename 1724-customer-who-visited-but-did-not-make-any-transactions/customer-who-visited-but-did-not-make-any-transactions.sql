SELECT visits.customer_id, COUNT(visits.visit_id) AS count_no_trans
FROM visits
WHERE visits.visit_id NOT IN (
    SELECT transactions.visit_id
    FROM transactions
)
GROUP BY customer_id;