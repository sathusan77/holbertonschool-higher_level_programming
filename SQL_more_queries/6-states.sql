-- Create database and states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
