-- Create the MovieDB database
CREATE DATABASE MovieDB;-- use the database
USE MovieDB;

-- Create the Actors table
CREATE TABLE Actors (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

-- Create the Movies table
CREATE TABLE Movies (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    year INT
);

-- Insert actors
INSERT INTO Actors (id, name, age) VALUES
(1, 'Leonardo DiCaprio', 49),
(2, 'Scarlett Johansson', 39),
(3, 'Morgan Freeman', 86);

-- Insert movies
INSERT INTO Movies (id, title, year) VALUES
(1, 'Inception', 2010),
(2, 'Lucy', 2014),
(3, 'Shawshank Redemption', 1994);

-- Retrieve all actors
SELECT * FROM Actors;

-- Retrieve all movies released after 2000
SELECT * FROM Movies WHERE year > 2000;
