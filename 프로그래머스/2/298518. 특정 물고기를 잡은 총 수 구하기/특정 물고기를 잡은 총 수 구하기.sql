select COUNT(*) FISH_COUNT
from FISH_INFO A inner join FISH_NAME_INFO B on A.FISH_TYPE = B.FISH_TYPE
where FISH_NAME in ('BASS', 'SNAPPER')