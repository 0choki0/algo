SELECT CATEGORY, PRICE, PRODUCT_NAME
from FOOD_PRODUCT where PRICE in (
    select max(price)
    from FOOD_PRODUCT
    group by CATEGORY) 
AND CATEGORY in ( '과자', '국', '김치', '식용유')
group by 1
order by 2 desc