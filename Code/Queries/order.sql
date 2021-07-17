Select kepler_id, COUNT(kepler_name)
From Planet
GROUP BY kepler_id
HAVING COUNT(kepler_name)>1
ORDER BY COUNT(kepler_name) DESC