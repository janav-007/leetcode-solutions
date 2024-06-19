SELECT employee.name
FROM employee
WHERE employee.id IN(
    SELECT employee.managerId
    FROM employee
    GROUP BY managerId
    HAVING COUNT(*) >=5
);