# Write your MySQL query statement below
SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id;

# use aliases for more readability
-- SELECT eu.unique_id, e.name
-- FROM Employees e
-- LEFT JOIN EmployeeUNI eu ON e.id = eu.id;
