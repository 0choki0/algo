-- 코드를 입력하세요
select USER_ID, NICKNAME, concat_WS(' ', CITY, STREET_ADDRESS1, STREET_ADDRESS2) '전체주소', 
concat(LEFT(TLNO, 3), '-', SUBSTRING(TLNO, 4, 4),  '-', RIGHT(TLNO, 4)) '전화번호'
from (
    SELECT B.USER_ID, B.NICKNAME, B.CITY, B.STREET_ADDRESS1, B.STREET_ADDRESS2, B.TLNO, count(*) `COUNT`
    from USED_GOODS_BOARD A inner join USED_GOODS_USER B on A.WRITER_ID = B.USER_ID
    group by B.USER_ID
    ) BASE
where `COUNT` >= 3
order by USER_ID desc