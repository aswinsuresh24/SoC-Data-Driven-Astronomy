Select kepler_name,radius
From Planet
Where (status='CONFIRMED') AND (radius BETWEEN 1 AND 3);