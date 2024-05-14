with G1 as (
    select *
    from ECOLI_DATA
    where PARENT_ID is null
    ),
    G2 as (
    select *
    from ECOLI_DATA
    where PARENT_ID in (select ID from G1)
    ),
    G3 as (
    select *
    from ECOLI_DATA
    where PARENT_ID in (select ID from G2)
    )

select ID
from G3
order by 1