-- 코드를 입력하세요
SELECT PRODUCT_CODE, sum(price * sales_amount) as sales
FROM PRODUCT P, OFFLINE_SALE OS
WHERE P.PRODUCT_ID = OS.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY sales desc, PRODUCT_CODE