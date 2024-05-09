select A.ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO A inner join ITEM_TREE B on A.ITEM_ID = B.ITEM_ID
where B.PARENT_ITEM_ID in (
                            select ITEM_ID
                            from ITEM_INFO
                            where RARITY = 'RARE'
                          )
order by 1 desc 


