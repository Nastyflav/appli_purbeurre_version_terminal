#! /usr/bin/env python3
# coding: utf-8
'''File which contains all parameters the user can change in order to \
extract datas from the API and to instruct the database'''

#MySQL connexion parameters#

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Flying14!'

#API search parameters#

API_PAGE_SIZE = 20
API_PAGES_NUMBER = 1
API_CATEGORIES = ['Pâte à tartiner', 'Thés en sachet', 'Fromages blancs', 'Jus de fruits', 'Confitures de fruits']
API_URL_SOURCE = 'https://fr.openfoodfacts.org/cgi/search.pl?'

#Database recording parameters#

FILENAME = 'db_init.sql'
DB_PRODUCTS_INSERT = """INSERT IGNORE INTO products (name, description, store, nova_groups, barcode, url)\
                     VALUES (%(product_name)s, %(generic_name_fr)s, %(stores)s, %(nova_groups)s, %(code)s, %(url)s)"""
DB_CATEGORIES_INSERT = """INSERT INTO Categories (name)
                                VALUES
                                ('Pâtes à tartiner'),
                                ('Thés'),
                                ('Fromages blancs'),
                                ('Jus de fruits'),
                                ('Confitures de fruits')"""
DB_FAVORITES_INSERT = 'INSERT IGNORE INTO favorites (substitute_id, original_product_id) \
                    VALUES (%s, %s)'
