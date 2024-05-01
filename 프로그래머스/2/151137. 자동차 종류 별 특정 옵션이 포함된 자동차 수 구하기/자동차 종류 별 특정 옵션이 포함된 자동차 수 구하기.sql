-- 코드를 입력하세요
SELECT CAR_TYPE, count(CAR_ID) CARS
from CAR_RENTAL_COMPANY_CAR 
where OPTIONS like '%시트%'
group by 1
order by 1