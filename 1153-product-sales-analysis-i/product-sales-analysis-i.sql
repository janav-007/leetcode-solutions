SELECT product.product_name, sales.year, sales.price
FROM sales
JOIN product
ON sales.product_id WHERE sales.product_id = product.product_id
ORDER BY sales.year;