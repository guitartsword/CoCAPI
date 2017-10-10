CREATE PROCEDURE `building_add_to_th` (
	th_id CHAR(10),
    building_id CHAR(10)    
)
BEGIN
	SET @th_level = (SELECT level from TownHall where townhall_id = th_id);
    SET @max_level=0;
    SET @max_available=0;
	SELECT max_level, max_available INTO @max_level, @max_available
	FROM TownHall th INNER JOIN building_detail bui_det ON th.townhall_id = bui_det.townhall_id
	WHERE th.townhall_id = concat('validth',@th_level);
	INSERT INTO building_detail VALUES(building_id, th_id, @max_level, @max_available);
END
