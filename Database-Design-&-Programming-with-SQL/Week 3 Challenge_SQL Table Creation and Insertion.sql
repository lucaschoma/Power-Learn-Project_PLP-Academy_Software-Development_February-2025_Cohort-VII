-- Create the student Table
CREATE TABLE student (
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

-- Insert 3 Unique Records
INSERT INTO student (name, age, gender) VALUES
('Alice Johnson', 20, 'Female'),
('Brian Lee', 22, 'Male'),
('Carmen Diaz', 19, 'Female');

-- View the Data
SELECT * FROM student;
