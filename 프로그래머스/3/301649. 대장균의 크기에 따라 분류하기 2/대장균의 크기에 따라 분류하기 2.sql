with num as (
    select COUNT(*) N
    from ECOLI_DATA
    ),
    TIER as (
    select *,
        NTILE(4) OVER (ORDER BY SIZE_OF_COLONY desc) AS TIER
    from ECOLI_DATA
    )

select ID,
    case 
        when TIER = 1 then 'CRITICAL'
        when TIER = 2 then 'HIGH' 
        when TIER = 3 then 'MEDIUM' 
        when TIER = 4 then 'LOW'
    end COLONY_NAME
from TIER
order by 1
