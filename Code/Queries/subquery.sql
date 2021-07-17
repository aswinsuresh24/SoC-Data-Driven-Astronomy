SELECT ROUND(AVG(Planet.t_eq),1), MIN(Star.t_eff), MAX(Star.t_eff)
FROM Planet
JOIN Star USING (kepler_id)
WHERE Star.t_eff> (
  SELECT AVG(Star.t_eff) FROM Star)