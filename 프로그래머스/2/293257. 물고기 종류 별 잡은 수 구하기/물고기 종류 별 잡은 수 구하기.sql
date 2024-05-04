-- 코드를 작성해주세요
select count(*) FISH_COUNT, B.FISH_NAME
from FISH_INFO A left join FISH_NAME_INFO B
on A.FISH_TYPE = B.FISH_TYPE
group by A.FISH_TYPE, B.FISH_NAME
order by 1 desc