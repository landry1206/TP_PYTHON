use classicmodels;
SELECT lastName, firstName, count(employees.employeeNumber)
FROM employees
INNER JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
GROUP BY employees.employeeNumber
ORDER BY count(employees.employeeNumber) DESC
LIMIT 3;