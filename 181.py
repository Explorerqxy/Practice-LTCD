# Write your MySQL query statement below
select name Employee from Employee as E
where Salary > (select
               salary
               from
                    Employee
               where
                    Id = E.Managerid)