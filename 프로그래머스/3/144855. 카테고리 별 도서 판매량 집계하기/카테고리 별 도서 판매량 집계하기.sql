-- 코드를 입력하세요 
SELECT CATEGORY, sum(B.SALES) TOTAL_SALES
from BOOK A inner join BOOK_SALES B on A.BOOK_ID = B.BOOK_ID
where YEAR(SALES_DATE) = '2022' and MONTH(SALES_DATE) = '01'
group by 1
order by 1

