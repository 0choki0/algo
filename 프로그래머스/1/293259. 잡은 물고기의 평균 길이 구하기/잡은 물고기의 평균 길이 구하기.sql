-- 코드를 작성해주세요
select ROUND(avg(LENGTH), 2) AVERAGE_LENGTH
from (select ID, IFNULL(LENGTH, 10) LENGTH
from FISH_INFO 
) base