use classicmodels;
SELECT year(paymentDate) as Year, sum(amount) as gain
FROM payments
GROUP BY year(paymentDate)
ORDER BY Year;