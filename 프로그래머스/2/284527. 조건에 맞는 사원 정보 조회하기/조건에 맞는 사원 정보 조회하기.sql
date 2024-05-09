select SUM(C.SCORE) SCORE, A.EMP_NO, A.EMP_NAME, A.POSITION, A.EMAIL
from HR_EMPLOYEES A inner join HR_DEPARTMENT B on A.DEPT_ID = B.DEPT_ID
    inner join HR_GRADE C on A.EMP_NO = C.EMP_NO
group by A.EMP_NO
order by 1 desc
limit 1