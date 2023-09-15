-- Create the database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesnt exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush the privileges to apply them
FLUSH PRIVILEGES;