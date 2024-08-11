-- Set the delimiter to avoid conflicts with the semicolon used within the function
DELIMITER //

-- Drop the function if it exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the function
CREATE FUNCTION SafeDiv(numerator FLOAT, denominator FLOAT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN CASE 
        WHEN denominator = 0 THEN NULL 
        ELSE numerator / denominator 
    END;
END//

-- Reset the delimiter to the default
DELIMITER ;

