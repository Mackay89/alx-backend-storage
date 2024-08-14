-- Check if the table exists and drop it if it does
DROP TABLE IF EXISTS need_meeting;

-- Create the table
CREATE TABLE need_meeting (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    meeting_date DATE NOT NULL
);

-- Insert sample data (optional)
INSERT INTO need_meeting (name, meeting_date) VALUES ('Alice', '2024-08-10');
INSERT INTO need_meeting (name, meeting_date) VALUES ('Bob', '2024-08-11');

