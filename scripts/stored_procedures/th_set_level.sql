CREATE PROCEDURE `th_set_level` (
    th_id CHAR(10),
    lvl TINYINT UNSIGNED
)
BEGIN
    SET @max_level = (SELECT MAX(level) FROM TownHall WHERE townhall_id LIKE 'validth%');
    IF lvl<1 OR lvl > @max_level THEN
        SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'INVALID townhall level';
    END IF;
    UPDATE TownHall
    SET level = lvl
    WHERE townhall_id = th_id;
END