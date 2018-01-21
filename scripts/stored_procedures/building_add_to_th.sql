CREATE PROCEDURE `building_add_to_th` (
    th_id CHAR(10),
    building_id CHAR(10),
    lvl TINYINT UNSIGNED
)
BEGIN
    DECLARE
        th_level,
        max_level,
        max_available,
        b_count,
        building_exists
    INT DEFAULT 0;
    DECLARE building_level CHAR(10) DEFAULT concat(building_id, lvl);
    DECLARE building_name VARCHAR(20);

    SELECT level INTO th_level FROM townhall WHERE townhall_id = th_id;
    SELECT b.name INTO building_name FROM building b WHERE b.building_id = building_id;

    SELECT SUM(building_count) INTO b_count
    FROM building_detail bd INNER JOIN building b ON b.building_id=bd.building_id
    WHERE townhall_id=th_id AND b.name = building_name;

    SELECT b.level INTO building_exists 
    FROM building b
    WHERE b.building_id = building_level;

    SET building_exists = building_exists IS NOT NULL OR building_exists = 0;

    IF b_count IS NULL THEN
        SET b_count = 0;
    END IF;
    
    SELECT max_level, max_available INTO max_level, max_available
    FROM valid_buildings vb
    WHERE vb.th_level=th_level AND vb.building_id=building_id;

    IF NOT building_exists THEN
        SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'INVALID building id';
    END IF;

    IF b_count + 1 > max_available THEN
        SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'building limit reached';
    END IF;

    INSERT INTO building_detail VALUES(building_level, th_id, max_level, max_available, 1)
    ON DUPLICATE KEY UPDATE building_count = building_count + 1;
END
