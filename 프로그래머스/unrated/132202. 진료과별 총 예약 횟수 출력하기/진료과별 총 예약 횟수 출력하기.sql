-- 코드를 입력하세요
SELECT MCDP_CD as "진료과코드", count(PT_NO) as "5월예약건수"
FROM APPOINTMENT
WHERE substr(to_char(APNT_YMD, 'yyyy-mm-dd'),7,1) = 5
GROUP BY MCDP_CD
ORDER BY count(PT_NO), MCDP_CD