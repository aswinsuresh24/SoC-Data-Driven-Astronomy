SELECT Star.radius, COUNT(Planet.koi_name)
FROM Star
JOIN Planet ON Planet.kepler_id=Star.kepler_id
WHERE Star.radius>1 AND Planet.kepler_id=Star.kepler_id
GROUP BY Star.kepler_id
HAVING COUNT(Planet.koi_name)>1 
ORDER BY Star.radius DESC