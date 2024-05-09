select ID, NAME, HOST_ID
from PLACES
where HOST_ID in (
    select HOST_ID
    from(
        select HOST_ID, COUNT(*) `COUNT`
        from PLACES
        group by 1
        HAVING `COUNT` >= 2
        ) BASE
    )
order by 1