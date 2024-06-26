-- 코드를 입력하세요
SELECT A.PRODUCT_ID, PRODUCT_NAME, SUM(A.PRICE*B.AMOUNT) TOTAL_SALES
from FOOD_PRODUCT A inner join FOOD_ORDER B
on A.PRODUCT_ID = B.PRODUCT_ID
where DATE_FORMAT(PRODUCE_DATE, '%Y-%m') = '2022-05'
group by PRODUCT_NAME
order by 3 desc, A.PRODUCT_ID