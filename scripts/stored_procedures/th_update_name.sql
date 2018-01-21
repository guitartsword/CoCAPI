CREATE PROCEDURE `th_update_name` (
    th_id CHAR(10),
    username VARCHAR(16)
)
BEGIN
    UPDATE townhall
    SET username = username
    WHERE townhall_id = th_id;
END
