-- 코드를 입력하세요
select count(NAME) `count`
from(
SELECT count(NAME) NAME
from ANIMAL_INS where NAME is not null
group by NAME
) base
    