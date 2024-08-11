-- Check if the procedure exists and drop it if it does
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Create the new procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Your procedure logic here
    -- Example:
    UPDATE users
    SET average_weighted_score = (
        SELECT AVG(score * weight) / AVG(weight)
        FROM corrections
        WHERE corrections.user_id = users.id
    );
END //

DELIMITER ;

