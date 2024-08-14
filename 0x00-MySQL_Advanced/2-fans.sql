-- Rank band origins (styles) by the number of non-unique fans

SELECT
    style AS origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    style
ORDER BY
    nb_fans DESC;

