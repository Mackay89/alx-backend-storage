-- Show current data
SELECT * FROM users;
SELECT * FROM corrections;

-- Call the procedure to compute and update the average score for Jeanne
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

-- Show updated data
SELECT "--";
SELECT * FROM users;

