# Write your MySQL query statement below
select Email from Person group by Email having count(Email)>1;

#Way 2
# Write your MySQL query statement below
select Email from person group by email having count(*)>1;

#W3
select
       a.email as Email
from
       person a
group by
       a.email
having
       count(a.email)>1;