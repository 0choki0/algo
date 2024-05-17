with FRONT as (
    select SUM(`CODE`) `CODE`
    from SKILLCODES
    where CATEGORY = 'Front End'
    )
    
select D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
from DEVELOPERS as D, FRONT as F
where F.CODE & D.SKILL_CODE
order by 1