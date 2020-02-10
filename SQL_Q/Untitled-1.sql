-- SQLite
SELECT id, image, user_id, is_boss, employee_id
FROM `user_management_profile`;

SELECT *
FROM `user_management_account`;

-- SQLite
INSERT INTO 'orient_advances_section' (section_name) VALUES ('IT');

-- SQLite
SELECT id, section_name
FROM `orient_advances_section`;

SELECT id, section_name
FROM `orient_advances_other`;

DROP TABLE [IF EXISTS] orient_advances_other;

select * from `orient_advances_advance`;