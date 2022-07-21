use classicmodels;
SELECT year(shippedDate) as year, month(shippedDate) as month, count(quantityOrdered) as quantity
FROM orders
inner join orderdetails on orders.orderNumber = orderdetails.orderNumber
WHERE (shippedDate  like "2003-%") and status = "Shipped"
GROUP BY month(shippedDate)
ORDER BY Month;