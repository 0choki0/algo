select `YEAR`, ROUND(AVG(PM_VAL1), 2) `PM10`, ROUND(AVG(PM_VAL2), 2) `PM2.5`
from(
    select YEAR(YM) `YEAR`, PM_VAL1, PM_VAL2
    from AIR_POLLUTION 
    where LOCATION2 = '수원'
    ) BASE
group by 1
order by 1