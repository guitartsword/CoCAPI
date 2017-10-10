CREATE PROCEDURE `th_delete` (th_id CHAR(10))
BEGIN
	DELETE FROM TownHall where townhall_id = th_id;
END
