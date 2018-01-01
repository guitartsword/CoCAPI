CREATE PROCEDURE `th_add` (
	th_id CHAR(10),
    username VARCHAR(15),
    lvl TINYINT UNSIGNED
)
BEGIN
	SET @max_level = (SELECT MAX(level) FROM TownHall WHERE townhall_id LIKE 'validth%');
    
	IF lvl<1 OR lvl > @max_level THEN
		SIGNAL SQLSTATE '45000' 
			SET MESSAGE_TEXT = 'INVALID townhall level';
	END IF;
	INSERT INTO TownHall(townhall_id, username, level) VALUES (th_id,username,lvl)
    ON DUPLICATE KEY UPDATE
    username = username,
    level = lvl;
END
