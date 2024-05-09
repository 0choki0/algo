select MONTH(START_DATE) MONTH, CAR_ID,
COUNT(*) RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where CAR_ID in (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where DATE_FORMAT(START_DATE, '%Y-%m') between '2022-08' and '2022-10'
    group by CAR_ID
    HAVING COUNT(*) >= 5
    ) and
    DATE_FORMAT(START_DATE, '%Y-%m') between '2022-08' and '2022-10'
group by 1, 2
HAVING RECORDS >0
order by 1, 2 desc
