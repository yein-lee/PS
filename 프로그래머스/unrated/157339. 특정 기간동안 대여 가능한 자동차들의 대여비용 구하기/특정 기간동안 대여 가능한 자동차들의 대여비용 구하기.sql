WITH CAR_ID_CANDIDATE AS (
    SELECT CAR_ID 
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE CAR_TYPE IN ('세단', 'SUV')
), 
CAR_ID_NONE_CADIDATE AS (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-11-01' AND '2022-11-30'
        OR END_DATE BETWEEN '2022-11-01' AND '2022-11-30'
        OR START_DATE <= '2022-11-01' AND END_DATE >= '2022-11-30'
)

, FEE_CALCULATION AS (
    SELECT 
        car.CAR_ID,
        car.CAR_TYPE,
        FLOOR(car.DAILY_FEE * 30 * (1 - discount_plan.DISCOUNT_RATE * 0.01)) AS FEE -- 버림
    FROM CAR_RENTAL_COMPANY_CAR car
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN discount_plan 
        ON car.CAR_TYPE = discount_plan.CAR_TYPE
    WHERE car.CAR_ID IN (SELECT CAR_ID FROM CAR_ID_CANDIDATE)
        AND car.CAR_ID NOT IN (SELECT CAR_ID FROM CAR_ID_NONE_CADIDATE)
        AND discount_plan.DURATION_TYPE = '30일 이상'
)

SELECT CAR_ID, CAR_TYPE, FEE
FROM FEE_CALCULATION
WHERE FEE BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC;

