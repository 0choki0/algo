select COUNT(`TIME`) FISH_COUNT, `TIME` `MONTH`
from(
    select ID, MONTH(TIME) `TIME`
    from FISH_INFO 
    ) BASE
group by 2
order by 2