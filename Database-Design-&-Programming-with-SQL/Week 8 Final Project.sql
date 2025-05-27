
-- Create the database
CREATE DATABASE IF NOT EXISTS ClinicDB;
USE ClinicDB;

-- Table: Patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    BirthDate DATE,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: Doctors
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    SpecialtyID INT,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(20),
    FOREIGN KEY (SpecialtyID) REFERENCES Specialties(SpecialtyID)
);

-- Table: Specialties
CREATE TABLE Specialties (
    SpecialtyID INT AUTO_INCREMENT PRIMARY KEY,
    SpecialtyName VARCHAR(100) NOT NULL UNIQUE
);

-- Table: Appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    AppointmentDate DATETIME NOT NULL,
    Reason TEXT,
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- Table: Treatments
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY,
    AppointmentID INT NOT NULL,
    Description TEXT NOT NULL,
    TreatmentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);

-- Table: DoctorSpecialty (for M-M in case doctors can have multiple specialties)
CREATE TABLE DoctorSpecialty (
    DoctorID INT,
    SpecialtyID INT,
    PRIMARY KEY (DoctorID, SpecialtyID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (SpecialtyID) REFERENCES Specialties(SpecialtyID)
);
