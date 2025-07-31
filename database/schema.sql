-- Create database
CREATE DATABASE IF NOT EXISTS railway_db;
USE railway_db;

-- Users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    role ENUM('admin', 'passenger') DEFAULT 'passenger'
);

-- Trains table
CREATE TABLE trains (
    train_id INT AUTO_INCREMENT PRIMARY KEY,
    train_name VARCHAR(100) NOT NULL,
    source VARCHAR(50),
    destination VARCHAR(50),
    departure_time TIME,
    arrival_time TIME,
    total_seats INT NOT NULL
);

-- Bookings table
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    train_id INT,
    seat_number INT,
    booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('booked', 'cancelled') DEFAULT 'booked',
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (train_id) REFERENCES trains(train_id)
);
