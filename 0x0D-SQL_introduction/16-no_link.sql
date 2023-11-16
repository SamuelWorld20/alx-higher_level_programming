-- This script list all records of the table
-- Only if it has a name
-- Records in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
