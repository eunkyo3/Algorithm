-- 코드를 입력하세요
SELECT round(avg(DAILY_FEE)) as average_fee
from CAR_RENTAL_COMPANY_CAR
where car_type = 'SUV'