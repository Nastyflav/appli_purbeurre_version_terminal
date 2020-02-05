CREATE DATABASE IF NOT EXISTS purbeurre DEFAULT CHARACTER SET 'utf8';
USE purbeurre;
CREATE TABLE IF NOT EXISTS Categories (id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    PRIMARY KEY (id),
                    UNIQUE INDEX ind_cat_name(name)
                    )
                    ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS Products (id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    name VARCHAR(100) NOT NULL,
                    description VARCHAR(200),
                    category_id INT UNSIGNED NOT NULL,
                    stores VARCHAR(200),
                    nova_group CHAR(1) NOT NULL,
					barcode BIGINT UNSIGNED NOT NULL,
                    url VARCHAR(200) NOT NULL,
                    PRIMARY KEY (id),
                    UNIQUE INDEX ind_barcode_name(barcode, name),
                    CONSTRAINT FK_product_category FOREIGN KEY (category_id) REFERENCES Categories (id) ON DELETE CASCADE
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