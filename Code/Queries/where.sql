Select Star.radius AS sun_radius, Planet.radius AS planet_radius
From Star, Planet
Where (Star.kepler_id=Planet.kepler_id) AND (Star.radius/Planet.radius>1)
ORDER BY sun_radius DESC;