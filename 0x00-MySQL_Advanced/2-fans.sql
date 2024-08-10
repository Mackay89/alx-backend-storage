-- Script to rank country origins of bands by the number of non-unique fans
-- The result will list countries and their total number of fans in descending order

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

