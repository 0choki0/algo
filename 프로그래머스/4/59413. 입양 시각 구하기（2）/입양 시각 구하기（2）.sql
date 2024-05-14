WITH recursive TIMES as(
    select 0 as HOUR 
    union 
    select HOUR+1 from TIMES 
    where HOUR < 23
)

select T.HOUR, COUNT(ANIMAL_ID)
from TIMES T left join ANIMAL_OUTS A on T.HOUR = HOUR(A.DATETIME)
group by 1
order by 1