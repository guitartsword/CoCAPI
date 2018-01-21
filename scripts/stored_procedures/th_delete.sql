CREATE PROCEDURE `th_delete` (th_id CHAR(10))
BEGIN
    DELETE FROM townhall where townhall_id = th_id;
END
