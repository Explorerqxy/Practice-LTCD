# Write your MySQL query statement below
select w2.Id
from Weather w1, Weather w2
where
DATEDIFF(w2.RecordDate,w1.RecordDate)=1
and w1.Temperature<w2.Temperature;

#DATEDIFF是两个日期的天数差集