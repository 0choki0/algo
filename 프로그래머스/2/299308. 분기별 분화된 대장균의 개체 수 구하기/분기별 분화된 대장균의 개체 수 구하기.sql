select QUARTER, COUNT(*) ECOLI_COUNT
from (
    select *, case when MONTH(DIFFERENTIATION_DATE) between 1 and 3 then '1Q'
                   when MONTH(DIFFERENTIATION_DATE) between 4 and 6 then '2Q'
                   when MONTH(DIFFERENTIATION_DATE) between 7 and 9 then '3Q'
                   when MONTH(DIFFERENTIATION_DATE) between 10 and 12 then '4Q'
              end QUARTER
    from ECOLI_DATA
    ) BASE
group by 1
order by 1
