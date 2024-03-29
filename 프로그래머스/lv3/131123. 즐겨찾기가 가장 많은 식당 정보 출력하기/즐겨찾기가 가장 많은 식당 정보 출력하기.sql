-- 코드를 입력하세요
SELECT info.FOOD_TYPE, info.REST_ID, info.REST_NAME, info.FAVORITES
FROM REST_INFO info
WHERE (info.FOOD_TYPE, info.FAVORITES) IN (
    SELECT FOOD_TYPE, MAX(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)
ORDER BY info.FOOD_TYPE DESC;
