UPDATE Planet
SET kepler_name=NULL
WHERE NOT(Status='CONFIRMED');

DELETE FROM Planet
WHERE Radius<0;