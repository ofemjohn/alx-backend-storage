-- creating triggers to reset attributes in a field
DELIMITER $$ 

CREATE TRIGGER email_reset_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END
$$

DELIMITER ;

