select EMP_NO, EMP_NAME, GRADE, 
case when GRADE='S' then SAL*0.2 when GRADE='A' then SAL*0.15 when GRADE='B' then SAL*0.1 else 0 end BONUS
from (
    select EMP_NO, EMP_NAME, 
    case when SCORE>=96 then 'S' when SCORE>=90 then 'A' when SCORE>=80 then 'B' else 'C' end GRADE,
    SAL
    from (
        select A.EMP_NO, A.EMP_NAME, AVG(C.SCORE) SCORE, A.SAL
        from HR_EMPLOYEES A inner join HR_DEPARTMENT B on A.DEPT_ID = B.DEPT_ID
        inner join HR_GRADE C on A.EMP_NO = C.EMP_NO
        group by A.EMP_NO
        ) BASE
    ) BASE
order by 1

    