# Write your MySQL query statement below
SELECT P2.Name AS Department,P3.Name AS Employee,P3.Salary AS Salary
FROM Employee AS P3
INNER JOIN Department AS P2
ON P2.Id = P3.DepartmentId
WHERE (
    SELECT COUNT(DISTINCT Salary)
    FROM Employee AS P4
    WHERE P3.DepartmentId = P4.DepartmentId
    AND P4.Salary >= P3.Salary
) <= 3
ORDER BY DepartmentId,Salary DESC