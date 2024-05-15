with RENTAL_HISTORY as (
    select B.HISTORY_ID, A.CAR_ID, A.CAR_TYPE, DAILY_FEE, DATEDIFF(END_DATE,START_DATE)+1 as PERIOD,
    case 
        when DATEDIFF(END_DATE,START_DATE)+1 >= 90 then '90일 이상'
        when DATEDIFF(END_DATE,START_DATE)+1 >= 30 then '30일 이상'
        when DATEDIFF(END_DATE,START_DATE)+1 >= 7 then '7일 이상'
        else '7일 미만'
    end as DURATION_TYPE
    from CAR_RENTAL_COMPANY_CAR as A inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY as B
    on A.CAR_ID = B.CAR_ID
    )

select A.HISTORY_ID, 
    case 
        when A.DURATION_TYPE = '7일 미만' then A.PERIOD*A.DAILY_FEE
        else ROUND(A.PERIOD*A.DAILY_FEE*(100-B.DISCOUNT_RATE)*0.01)
    end FEE
from RENTAL_HISTORY as A left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as B
on A.CAR_TYPE  = B.CAR_TYPE 
and A.DURATION_TYPE  = B.DURATION_TYPE
where A.CAR_TYPE = '트럭'
order by 2 desc, 1 desc