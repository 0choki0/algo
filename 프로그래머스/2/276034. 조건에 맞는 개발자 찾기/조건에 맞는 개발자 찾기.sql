select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS
where SKILL_CODE & (select SUM(`CODE`) from SKILLCODES where NAME in ('Python', 'C#'))
order by 1


