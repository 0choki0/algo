-- 코드를 입력하세요
SELECT A.PRODUCT_CODE, sum(A.PRICE * B.SALES_AMOUNT) SALES
from PRODUCT A inner join OFFLINE_SALE B on A.PRODUCT_ID = B.PRODUCT_ID
group by 1
order by 2 desc, 1