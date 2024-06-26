-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, TOTAL_SALES
from(
SELECT B.USER_ID, B.NICKNAME, SUM(A.PRICE) TOTAL_SALES
from USED_GOODS_BOARD A inner join USED_GOODS_USER  B
on A.WRITER_ID = B.USER_ID
where A.STATUS = 'DONE'
group by 1
    ) BASE
    where TOTAL_SALES >= 700000
order by 3