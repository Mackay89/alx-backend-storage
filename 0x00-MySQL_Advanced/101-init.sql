DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;

    -- Cursor to iterate over all user IDs
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open cursor
    OPEN user_cursor;

    -- Loop through each user
    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Call the existing procedure to compute the average weighted score for each user
        CALL ComputeAverageWeightedScoreForUser(user_id);

    END LOOP user_loop;

    -- Close cursor
    CLOSE user_cursor;
END$$

DELIMITER ;

