CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(256) UNIQUE NOT NULL,
    first_name VARCHAR(256),
    last_name VARCHAR(256),
    email VARCHAR(256),
    INDEX (login)
);

CREATE TABLE IF NOT EXISTS services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    description TEXT,
    cost DECIMAL(10, 2),
    INDEX (name)
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    INDEX (user_id)
);

CREATE TABLE IF NOT EXISTS order_service (
    order_id INT,
    service_id INT,
    PRIMARY KEY (order_id, service_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

INSERT INTO users (login, first_name, last_name, email)
VALUES ('john123', 'John', 'Doe', 'john@example.com');

INSERT INTO users (login, first_name, last_name, email)
VALUES ('jane567', 'Jane', 'Smith', 'jane@example.com');

INSERT INTO users (login, first_name, last_name, email)
VALUES ('mike789', 'Mike', 'Johnson', 'mike@example.com');


INSERT INTO services (name, description, cost)
VALUES ('Web Development', 'Professional website development services', 250.00);

INSERT INTO services (name, description, cost)
VALUES ('Graphic Design', 'Creative graphic design services', 150.00);

INSERT INTO services (name, description, cost)
VALUES ('Digital Marketing', 'Effective online marketing strategies', 300.00);

INSERT INTO orders (user_id, date_created)
VALUES (1, '2023-10-10'), (2, '2023-11-15'), (3, '2023-09-20');

INSERT INTO order_service (order_id, service_id)
VALUES (1, 1), (2, 2), (3, 3);

SELECT * FROM users;
SELECT * FROM orders;
SELECT * FROM services;
SELECT * FROM order_service;
