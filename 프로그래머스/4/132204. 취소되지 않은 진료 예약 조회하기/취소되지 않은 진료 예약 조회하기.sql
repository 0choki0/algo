SELECT A.APNT_NO, B.PT_NAME, B.PT_NO, C.MCDP_CD, C.DR_NAME, A.APNT_YMD
from APPOINTMENT A inner join PATIENT B on A.PT_NO = B.PT_NO
inner join DOCTOR C on A.MDDR_ID = C.DR_ID
where C.MCDP_CD = 'CS' AND A.APNT_CNCL_YN = 'N' AND DATE(A.APNT_YMD) = '2022-04-13'
order by 6;