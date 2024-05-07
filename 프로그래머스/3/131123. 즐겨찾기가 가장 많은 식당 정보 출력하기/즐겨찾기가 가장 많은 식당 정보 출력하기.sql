select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from (
SELECT *, DENSE_RANK() over(PARTITION BY FOOD_TYPE order by FAVORITES desc) `RANK`
from REST_INFO
    ) base
where `RANK` = 1
order by FOOD_TYPE desc 