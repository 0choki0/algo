with RECORD_NOVEMBER as (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE LIKE '2022-11%' OR START_DATE LIKE '2022-11%' 
            OR(START_DATE < '2022-11-01' AND END_DATE > '2022-11-30')
    ),
    
    RENTAL_CAR as (
    select C.CAR_ID CAR_ID, R.CAR_ID RECORD_NOVEMBER, C.CAR_TYPE, C.DAILY_FEE
    from CAR_RENTAL_COMPANY_CAR as C left join RECORD_NOVEMBER as R
        on C.CAR_ID = R.CAR_ID
    where CAR_TYPE in ('세단', 'SUV')
    HAVING RECORD_NOVEMBER is null
    ),
    
    DISCOUNT as (
    select CAR_TYPE, DISCOUNT_RATE
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where DURATION_TYPE = '30일 이상'
    )
    
select CAR_ID, R.CAR_TYPE, ROUND(DAILY_FEE*30*(100-DISCOUNT_RATE)*0.01) FEE
from RENTAL_CAR R inner join DISCOUNT D
    on R.CAR_TYPE = D.CAR_TYPE
HAVING FEE between 500000 and 2000000
order by 3 desc, 2, 1 desc