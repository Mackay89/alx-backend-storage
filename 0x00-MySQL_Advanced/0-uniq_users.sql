-- 0-uniq_users.sql
-- SQL script to create the table 'users'
-- The table contains an auto-incrementing 'id', a unique 'email', and a 'name'
-- This script will not fail if the table already exists

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

