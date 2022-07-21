SELECT * FROM classicmodels.products;
SELECT products.productCode, products.productName, count(products.productCode) as sumProduct FROM products
join orderdetails on products.productCode = orderdetails.productCode
GROUP BY products.productCode
ORDER BY count(products.productCode) DESC;