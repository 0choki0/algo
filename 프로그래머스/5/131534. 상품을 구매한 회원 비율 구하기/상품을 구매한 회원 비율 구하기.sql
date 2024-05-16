with JOINED as (
    select USER_ID, (select COUNT(USER_ID) from USER_INFO where YEAR(JOINED) = '2021') as USERS
    from USER_INFO
    where YEAR(JOINED) = '2021'
    )
    
    ,SALES as (
    select YEAR(S.SALES_DATE) as YEAR, MONTH(S.SALES_DATE) as MONTH, COUNT(DISTINCT J.USER_ID) PUCHASED_USERS, USERS
    from ONLINE_SALE as S inner join JOINED as J
        on S.USER_ID = J.USER_ID
    group by 1, 2
    )

select YEAR, MONTH, PUCHASED_USERS, ROUND(PUCHASED_USERS/USERS, 1) as PUCHASED_RATIO
from SALES
order by 1, 2



    

