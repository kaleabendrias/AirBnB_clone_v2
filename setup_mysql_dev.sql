-- Create a db if not exists
CREATE DATABASE IF NOT exists hbnb_dev_db;

-- Create a user if it doesnt exists and give it its passwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant the privilages needed by user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush the privileges
FLUSH PRIVILEGES;
