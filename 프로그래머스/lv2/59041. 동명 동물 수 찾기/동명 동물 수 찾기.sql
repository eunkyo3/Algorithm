-- 코드를 입력하세요
SELECT name, count(animal_id) as count
FROM animal_ins
WHERE name is not null
GROUP BY name
HAVING count(animal_id) >= 2
ORDER BY name