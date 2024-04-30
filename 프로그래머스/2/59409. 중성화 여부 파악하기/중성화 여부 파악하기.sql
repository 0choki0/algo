-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, case when SEX_UPON_INTAKE like '%Neutered%' or SEX_UPON_INTAKE like '%Spayed%' then 'O' ELSE 'X' END '중성화'
from ANIMAL_INS 