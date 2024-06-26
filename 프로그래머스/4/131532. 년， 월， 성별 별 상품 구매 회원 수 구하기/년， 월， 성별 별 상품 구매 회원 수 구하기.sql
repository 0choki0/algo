select YEAR(B.SALES_DATE) `YEAR`, MONTH(B.SALES_DATE), GENDER, COUNT(DISTINCT A.USER_ID) USERS
from USER_INFO A inner join ONLINE_SALE B on A.USER_ID=B.USER_ID
where A.GENDER is not null
group by 1, 2, 3
order by 1, 2, 3