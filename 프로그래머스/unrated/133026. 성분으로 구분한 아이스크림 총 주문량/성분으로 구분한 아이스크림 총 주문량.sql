-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, sum(TOTAL_ORDER) total_order
FROM FIRST_HALF FH, ICECREAM_INFO II
WHERE FH.flavor = II.flavor
GROUP BY INGREDIENT_TYPE
ORDER BY total_order