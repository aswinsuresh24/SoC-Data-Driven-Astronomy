SELECT Planet.koi_name, Planet.radius, Star.radius
FROM Planet
JOIN Star USING (kepler_id)
WHERE Star.radius IN(
  SELECT radius FROM Star
  ORDER BY radius DESC
  LIMIT 5)