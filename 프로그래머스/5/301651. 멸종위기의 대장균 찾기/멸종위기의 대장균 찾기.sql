with RECURSIVE GEN as(
    select ID, PARENT_ID, 1 AS GEN
    from ECOLI_DATA
    where PARENT_ID is NULL
    
    UNION ALL
    
    select CHILD.ID, CHILD.PARENT_ID, GEN.GEN + 1
    from ECOLI_DATA CHILD
    inner join GEN
        on CHILD.PARENT_ID = GEN.ID
    )

    , HAVE_CHILD as (
    select A.GEN, A.ID, B.ID as CHILD_ID
    from GEN as A, GEN as B
    where A.ID = B.PARENT_ID
    )
    
select COUNT(ID) as `COUNT`, GEN as GENERATION
from  GEN
where ID not in (select ID from HAVE_CHILD)
group by 2
order by 2
