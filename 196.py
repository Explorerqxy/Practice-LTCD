# Write your MySQL query statement below
DELETE FROM Person WHERE Id Not IN (SELECT * FROM (SELECT MIN(Id) FROM Person GROUP BY Email) AS p)

