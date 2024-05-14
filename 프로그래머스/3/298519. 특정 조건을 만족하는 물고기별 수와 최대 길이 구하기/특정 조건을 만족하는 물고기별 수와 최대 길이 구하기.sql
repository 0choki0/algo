select FISH_COUNT, MAX_LENGTH, FISH_TYPE
from(
    select FISH_TYPE, AVG(LENGTH) 'L_AVG', COUNT(ID) `FISH_COUNT`, MAX(LENGTH) `MAX_LENGTH`
    from (select ID, FISH_TYPE, case when LENGTH is null then 10 else LENGTH end LENGTH from FISH_INFO) BASE
    group by FISH_TYPE
    ) BASE
where L_AVG >= 33
order by 3 