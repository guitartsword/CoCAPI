CREATE VIEW `new_view` AS
SELECT
    th.level AS 'th_level',
    b.building_id, b.name,
    bd.max_level,
    bd.max_available
FROM building_detail bd
INNER JOIN building b ON bd.building_id=b.building_id
INNER JOIN townhall th ON th.townhall_id=bd.townhall_id
WHERE th.townhall_id LIKE 'validth%' ORDER BY th.level;