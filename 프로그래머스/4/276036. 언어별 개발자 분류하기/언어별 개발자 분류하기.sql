with FRONT_END as (
    select SUM(`CODE`) `CODE`
    from SKILLCODES
    where CATEGORY = 'Front End'
    )
    
    , BACK_END as (
    select NAME, `CODE`
    from SKILLCODES
    where NAME in ('Python','C#')
    )
    
select case
    when SKILL_CODE & (select `CODE` from FRONT_END) and SKILL_CODE & (select `CODE` from BACK_END where NAME = 'Python') then 'A'
    when SKILL_CODE & (select `CODE` from BACK_END where NAME = 'C#') then 'B'
    when SKILL_CODE & (select `CODE` from FRONT_END) then 'C'
    end GRADE,
    ID, EMAIL
from DEVELOPERS
HAVING GRADE is not null
order by 1, 2
