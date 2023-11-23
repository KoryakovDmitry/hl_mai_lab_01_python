CREATE TABLE IF NOT EXISTS User (
    id INT NOT NULL AUTO_INCREMENT,
    login VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    first_name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    last_name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    email VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY unique_login (login)
);

CREATE TABLE IF NOT EXISTS Service (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    description TEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci,
    cost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS `Order` (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    service_id INT NOT NULL,
    date_created DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (service_id) REFERENCES Service(id)
);


INSERT INTO User (login, first_name, last_name, email)
VALUES ('john123',  'John', 'Doe', 'john@example.com');

INSERT INTO User (login, first_name, last_name, email)
VALUES ('jane567', 'Jane', 'Smith', 'jane@example.com');

INSERT INTO User (login, first_name, last_name, email)
VALUES ('mike789', 'Mike', 'Johnson', 'mike@example.com');

INSERT INTO Service (name, description, cost)
VALUES ('Web Development', 'Professional website development services', 250.00);

INSERT INTO Service (name, description, cost)
VALUES ('Graphic Design', 'Creative graphic design services', 150.00);

INSERT INTO Service (name, description, cost)
VALUES ('Digital Marketing', 'Effective online marketing strategies', 300.00);


INSERT INTO `Order` (user_id, service_id, date_created)
VALUES (1, 1, '2023-10-10');

INSERT INTO `Order` (user_id, service_id, date_created)
VALUES (2, 2, '2023-11-15');

INSERT INTO `Order` (user_id, service_id, date_created)
VALUES (3, 3, '2023-09-20');

SELECT * FROM User;
SELECT * FROM `Order`;
SELECT * FROM Service;