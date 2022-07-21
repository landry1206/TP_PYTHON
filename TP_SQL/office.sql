use classicmodels;
SELECT city, offices.officeCode, count(offices.officeCode) as sumEmployees FROM offices
inner join employees on offices.officeCode = employees.officeCode
GROUP BY offices.officeCode
ORDER BY offices.officeCode 
limit 1;