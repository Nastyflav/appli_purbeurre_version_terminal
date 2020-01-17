#! /usr/bin/env python3
# coding: utf-8
'''File which contains all parameters the user can change in order to \
extract datas from the API and to instruct the database'''

#MySQL connexion parameters#

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Flying14!'
DB_NAME = 'purbeurre'

#API search parameters#

API_PAGE_SIZE = 10
API_PAGES_NUMBER = [1, 2, 3, 4, 5]
API_CATEGORIES = ['pâte à tartiner', 'thés', 'fromages blancs', 'jus de fruits', 'confitures de fruits']
API_URL_SOURCE = 'https://fr.openfoodfacts.org/cgi/search.pl?'

#Database recording parameters#

DB_CREATION = "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'"
DB_PRODUCTS_TABLE = "CREATE TABLE IF NOT EXISTS Products (id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
                    name VARCHAR(50) NOT NULL UNIQUE, \
                    description VARCHAR(250), \
                    category_id INT UNSIGNED NOT NULL, \
                    barcode VARCHAR(30) NOT NULL, \
                    store VARCHAR(200), \
                    nova_groups VARCHAR(1) NOT NULL, \
                    url VARCHAR(200) NOT NULL UNIQUE, \
                    PRIMARY KEY (id) \
                    CONSTRAINT FK_product_category FOREIGN KEY (category_id) REFERENCES Category (id) \
                    )ENGINE = InnoDB;"
DB_CATEGORY_TABLE = "CREATE TABLE IF NOT EXISTS Products (id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
                    name VARCHAR(50) NOT NULL UNIQUE, \
                    )ENGINE = InnoDB;"
DB_FAVORITES_TABLE = "CREATE TABLE IF NOT EXISTS Products (id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
                    substitute_id INT UNSIGNED NOT NULL,\
                    original_product_id INT UNSIGNED NOT NULL, \
                    CONSTRAINT FK_substitute_product FOREIGN KEY (substitute_id) REFERENCES Products (id) \
                    CONSTRAINT FK_original_product FOREIGN KEY (original_product_id) REFERENCES Products (id) \
                    )ENGINE = InnoDB;"
DB_PRODUCTS_INSERTION = 'INSERT INTO products (name, description, barcode, store, nova_groups, url)\
                VALUES (%s, %s, %s, %s, %s, %s)'
