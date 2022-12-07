-- Write a script that:
-- -creates a database hbnb_dev_db
-- -creates a user hbnb_dev(in localhost with password hbnb_dev_pwd)
-- -grants all privileges to hbnb_dev on hbnb_dev_db
-- -creates a database performace_schema
-- -hbnb_dev has SELECT privileges on performance_schema
-- if the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER 
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES
    ON `hbnb_dev_db`.*
    TO 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
