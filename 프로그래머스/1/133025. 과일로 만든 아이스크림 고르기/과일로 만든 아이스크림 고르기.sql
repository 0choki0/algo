-- 코드를 입력하세요
SELECT A.FLAVOR FLAVOR
from FIRST_HALF A left join ICECREAM_INFO B on A.FLAVOR = B.FLAVOR
where TOTAL_ORDER > 3000 and INGREDIENT_TYPE like 'fruit_based'
order by TOTAL_ORDER desc;