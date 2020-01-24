CREATE DATABASE IF NOT EXISTS purbeurre DEFAULT CHARACTER SET 'utf8';
USE purbeurre;
CREATE TABLE IF NOT EXISTS Categories (id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL UNIQUE,
                    PRIMARY KEY (id)
                    )
                    ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS Products (id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL UNIQUE,
                    description VARCHAR(250),
                    category_id INT UNSIGNED NOT NULL,
                    store VARCHAR(200),
                    nova_groups VARCHAR(1) NOT NULL,
					barcode VARCHAR(30) NOT NULL,
                    url VARCHAR(200) NOT NULL UNIQUE,
                    PRIMARY KEY (id),
                    CONSTRAINT FK_product_category FOREIGN KEY (category_id) REFERENCES Categories (id)
                    )
                    ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS Favorites (id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    substitute_id INT UNSIGNED NOT NULL,
                    original_product_id INT UNSIGNED NOT NULL,
                    PRIMARY KEY (id),
                    CONSTRAINT FK_substitute_product FOREIGN KEY (substitute_id) REFERENCES Products (id) ON DELETE CASCADE,
                    CONSTRAINT FK_original_product FOREIGN KEY (original_product_id) REFERENCES Products (id) ON DELETE CASCADE
                    )
                    ENGINE = InnoDB;