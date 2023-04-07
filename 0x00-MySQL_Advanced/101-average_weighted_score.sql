-- Write a SQL script that creates a stored procedure.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE avg_weighted_score FLOAT;

    SELECT SUM(score * weight) / SUM(weight) 
    INTO avg_weighted_score
    FROM users AS u 
    JOIN corrections AS c ON u.id = c.user_id 
    JOIN projects AS p ON c.project_id = p.id 
    WHERE u.id = user_id;

    UPDATE users 
    SET average_score = avg_weighted_score 
    WHERE id = user_id;
END$$

DELIMITER ;
