with L_MAX as (
    select FISH_TYPE, MAX(LENGTH) LENGTH
    from FISH_INFO 
    group by FISH_TYPE
    ),
    FISH_MAX as (
    select A.FISH_TYPE, FISH_NAME, LENGTH
    from FISH_NAME_INFO A inner join L_MAX B on A.FISH_TYPE = B.FISH_TYPE
    )
    

select A.ID, B.FISH_NAME, B.LENGTH 
from FISH_INFO A
inner join FISH_MAX B on A.FISH_TYPE = B.FISH_TYPE
where A.LENGTH = B.LENGTH and A.FISH_TYPE = B.FISH_TYPE
order by 1

