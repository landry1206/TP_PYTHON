use classicmodels;
select * from payments;
SELECT customerName, count(customers.customerNumber) as nbreAchat, amount  FROM customers
inner join payments on customers.customerNumber = payments.customerNumber
GROUP BY payments.customerNumber
ORDER BY nbreAchat DESC;