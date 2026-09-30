CREATE DATABASE IF NOT EXISTS smart_city;
USE smart_city;
CREATE TABLE IF NOT EXISTS problems (id INT AUTO_INCREMENT PRIMARY KEY, problem_type VARCHAR(100), location VARCHAR(100), severity VARCHAR(30), description TEXT, status VARCHAR(30), detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS predictions (id INT AUTO_INCREMENT PRIMARY KEY, problem_type VARCHAR(100), location VARCHAR(100), probability FLOAT, prediction_time DATETIME, recommendation TEXT);
CREATE TABLE IF NOT EXISTS citizen_reports (id INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(100), problem_type VARCHAR(100), priority VARCHAR(30), description TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
INSERT INTO problems(problem_type,location,severity,description,status) VALUES ('Traffic Congestion','Hanamkonda','High','Heavy traffic detected','Active'),('Air Pollution','Warangal','Critical','Air quality above safe threshold','Active'),('Waste Overflow','Kazipet','Medium','Waste level is high','Pending');
