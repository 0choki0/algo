SELECT HOUR(DATETIME) HOUR, COUNT(DATETIME) `COUNT`
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19
GROUP BY 1 
ORDER BY 1;