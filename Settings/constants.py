#! /usr/bin/env python3
# coding: utf-8
'''File which contains all parameters the user can change in order to \
extract datas from the API and to instruct the database'''

#MySQL connexion parameters#

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Flying14!'
DB_NAME = 'purbeurre'
FILENAME = 'db_init.sql'

#API search parameters#

API_PAGE_SIZE = 10
API_PAGES_NUMBER = [1, 2, 3, 4, 5]
API_CATEGORIES = ['pâte à tartiner', 'thés', 'fromages blancs', 'jus de fruits', 'confitures de fruits']
API_URL_SOURCE = 'https://fr.openfoodfacts.org/cgi/search.pl?'

#Database recording parameters#

DB_PRODUCTS_INSERT = 'INSERT INTO products (name, description, barcode, store, nova_groups, url)\
                VALUES (%s, %s, %s, %s, %s, %s)'
