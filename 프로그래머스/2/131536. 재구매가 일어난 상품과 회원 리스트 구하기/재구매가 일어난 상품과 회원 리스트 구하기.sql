-- 코드를 입력하세요
select USER_ID, PRODUCT_ID
from(
    SELECT *, count(*) `COUNT`
    from ONLINE_SALE 
    group by USER_ID, PRODUCT_ID
    ) BASE
where `COUNT` >= 2
order by 1, 2 desc