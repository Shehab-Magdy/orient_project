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

-- insert into orient_advances_section(section_name) values('HR');
-- update user_management_account set is_admin = 1, is_superuser = 1, is_staff = 1 where email='cegres1@gmail.com';
-- update user_management_account set is_superuser = 1 where email='cegres1@gmail.com';
-- update user_management_account set is_staff = 1 where email='cegres1@gmail.com';
-- A123123a = 'pbkdf2_sha256$180000$LpvDMr6gOZ0A$0sfdue45qsIJbatLgTHAoFrs/2KDmoWmF2LyBWLdzag='
-- insert into user_management_account(password, email, username, employee_id, is_active, image, section_id) values('pbkdf2_sha256$180000$LpvDMr6gOZ0A$0sfdue45qsIJbatLgTHAoFrs/2KDmoWmF2LyBWLdzag=','bla@bla.com','blabla', '159632', 1,'default.png',1);