USE railway_db;

-- Sample Users
INSERT INTO users (username, password, role) VALUES
('admin', 'admin123', 'admin'),
('rohit', 'rohitpass', 'passenger'),
('anita', 'anitapass', 'passenger');

-- Sample Trains
INSERT INTO trains (train_name, source, destination, departure_time, arrival_time, total_seats) VALUES
('Chennai Express', 'Chennai', 'Mumbai', '06:00:00', '18:30:00', 100),
('Rajdhani Express', 'Delhi', 'Kolkata', '08:00:00', '20:00:00', 120),
('Shatabdi Express', 'Bangalore', 'Hyderabad', '07:30:00', '13:00:00', 80);

-- Sample Bookings
INSERT INTO bookings (user_id, train_id, seat_number, status) VALUES
(2, 1, 10, 'booked'),
(3, 2, 15, 'booked'),
(2, 3, 5, 'cancelled');
