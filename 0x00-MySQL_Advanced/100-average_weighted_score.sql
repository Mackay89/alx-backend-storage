-- Drop the existing procedure if it exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Create the new procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Procedure logic to compute and update the average weighted score
    UPDATE users
    SET average_weighted_score = (
        SELECT AVG(score * weight) / AVG(weight)
        FROM corrections
        WHERE corrections.user_id = user_id
    )
    WHERE id = user_id;
END //

DELIMITER ;

