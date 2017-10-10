CREATE PROCEDURE `th_add` (
	th_id CHAR(10),
    username VARCHAR(15),
    lvl TINYINT UNSIGNED
)
BEGIN
	set @valid_lvl = (SELECT max_level from TownHall where townhall_id = 'validth1');
    
	IF lvl<1 OR lvl > @valid_lvl THEN
		SIGNAL SQLSTATE '45000' 
			SET MESSAGE_TEXT = 'INVALID townhall level';
	END IF;
	INSERT INTO TownHall VALUES (th_id,username,lvl)
    ON DUPLICATE KEY UPDATE
    username = username,
    level = lvl;
END
