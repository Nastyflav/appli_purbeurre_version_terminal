#! /usr/bin/env python3
# coding: utf-8
'''File which contains all parameters the user can change in order to \
extract datas from the API and to instruct the database'''

#MySQL connexion parameters#

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Flying14!'

#API search parameters#

API_PAGE_SIZE = 150
API_PAGES_NUMBER = 1
API_CATEGORIES = ['Pâte à tartiner', 'Thés en sachet', 'Fromages blancs', 'Jus de fruits', 'Confitures de fruits',
                 'Céréales pour petit-déjeuner', 'Cafés', 'Pâtes alimentaires', 'Epices', 'Légumes surgelés',
                 'Sauces tomates', 'Surimi', 'Légumineuses', 'Frites', 'Galettes de céréales soufflées']
API_URL_SOURCE = 'https://fr.openfoodfacts.org/cgi/search.pl?'

#Database recording parameters

FILENAME = 'db_init.sql'
DB_PRODUCTS_INSERT = """INSERT IGNORE INTO Products (name, description, category_id, stores, nova_group, barcode, url)
                        VALUES ({0}, {1}, (SELECT id FROM Categories WHERE name = {2}), {3}, {4}, {5}, {6})"""
DB_CATEGORIES_INSERT = """ INSERT IGNORE INTO Categories (name) VALUES ({0})"""
DB_FAVORITES_INSERT = """INSERT IGNORE INTO Favorites (substitute_id, original_product_id) VALUES ({0}, {1})"""

#Database selection parameters

DB_PRODUCTS_SELECTION = """SELECT id, name, nova_group FROM Products WHERE category_id = {} AND nova_group = 4"""
DB_CATEGORIES_SELECTION = """SELECT * FROM Categories ORDER BY id"""
DB_SUBS_SELECTION = """SELECT (SELECT name FROM Products WHERE id = {1}),
                    (SELECT nova_group FROM Products WHERE id = {1}), 
                    id, name, description, nova_group FROM Products
                    WHERE category_id = {0} AND nova_group < 4 
                    ORDER BY nova_group"""
DB_SUB_DETAILS = """SELECT name, description, stores, nova_group, barcode, url FROM Products WHERE id = {}"""
DB_FAVORITES_SELECTION = """SELECT Favorites.id, Products.name FROM Products
                            JOIN Favorites ON Products.id = Favorites.substitute_id
                            WHERE Products.id = Favorites.substitute_id
                            ORDER BY Favorites.id"""
DB_ORIGINAL_PRODUCTS_SELECTION = """SELECT Products.name FROM Products
                            JOIN Favorites ON Products.id = Favorites.original_product_id
                            WHERE Products.id = Favorites.original_product_id
                            ORDER BY Favorites.id"""
DB_FAV_DETAILS = """SELECT name, description, stores, nova_group, barcode, url FROM Products
                            WHERE id = (SELECT substitute_id FROM Favorites WHERE id = {})"""
