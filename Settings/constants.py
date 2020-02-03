#! /usr/bin/env python3
# coding: utf-8
'''File which contains all parameters the user can change in order to \
extract datas from the API and to instruct the database'''

#MySQL connexion parameters#

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Flying14!'

#API search parameters#

API_PAGE_SIZE = 100
API_PAGES_NUMBER = 1
API_CATEGORIES = ['Pâte à tartiner', 'Thés en sachet', 'Fromages blancs', 'Jus de fruits', 'Confitures de fruits']
API_URL_SOURCE = 'https://fr.openfoodfacts.org/cgi/search.pl?'

#Database recording parameters#

FILENAME = 'db_init.sql'
DB_PRODUCTS_INSERT = """INSERT IGNORE INTO Products (name, description, category_id, store, nova_groups, barcode, url)
                        VALUES ({0}, {1}, (SELECT id FROM Categories WHERE name = {2}), {3}, {4}, {5}, {6})"""
DB_CATEGORIES_INSERT = """ INSERT IGNORE INTO Categories (name) VALUES ({0})"""
DB_FAVORITES_INSERT = """INSERT IGNORE INTO favorites (substitute_id, original_product_id) VALUES (%s, %s)"""
DB_PRODUCTS_SELECTION = """SELECT id, name, nova_groups FROM Products WHERE category_id = {} AND nova_groups = 4"""
DB_CATEGORIES_SELECTION = """SELECT id, name FROM Categories ORDER BY id"""
DB_FAVORITES_SELECTION = """SELECT id, name, description, nova_groups FROM Products 
                            WHERE category_id = {} AND nova_groups < 4 
                            ORDER BY nova_groups"""
