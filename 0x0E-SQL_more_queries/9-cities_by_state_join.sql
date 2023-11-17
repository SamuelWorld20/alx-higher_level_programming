-- This script lists all cities contained in a database
SELECT cities.id, cities.name, states.name AS name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
