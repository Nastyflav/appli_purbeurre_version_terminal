#! /usr/bin/env python3
# coding: utf-8
'''Manage the database in every ways, connexion, creation, insertion, error issues'''

import mysql.connector as con

from Settings.constants import *


class Database:
    '''Manage all the primary aspects regarding the database as connexion, error issues, data selection'''
    def __init__(self):
        self.filename = FILENAME
        '''No connexion yet'''
        self.connexion = False
        self.curs = False

    def db_creation(self):
        '''Create a database in the user's system using instructions in an init MySQL file'''
        try:
            with open(self.filename, 'r') as cmd_file:
                sql_commands = cmd_file.read()
                sql_commands = sql_commands.split(';') # Split the file in a list by using ';' as a separator for each SQL command
            for command in sql_commands:
                self.curs.execute(command)
        except FileNotFoundError:
            print("Couldn't open commands file \"" + self.filename + "\"")

    def db_connexion(self):
        '''Use mysql.connector to allow access to the chosen database'''
        self.connexion = con.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database= DB_NAME)
        self.curs = self.connexion.cursor(buffered=True)

    def db_check_in(self):
        '''Check if the database is already filled or not'''

    def data_recording(self):
        '''Pick precisely each chosen data and record it into the database'''
        print('Enregistrement des produits...')
        self.cat_insert = DB_CATEGORIES_INSERT #first we record in the table Categories
        for result in api.products_list:
            for api.categories in result['products']:
                self.cat_data = (api.categories['categories'])
                # print(self.cat_data)
                # exit(0)
                self.curs.execute(self.insert, self.data)
            self.connexion.commit()
        exit(0)

        self.products_insert = DB_PRODUCTS_INSERT #Then we add all products
        for result in api.products_list:
            for element in result['products']:
                self.data = (element['product_name'], element['generic_name_fr'], element['unique_scans_n'], \
                             element['stores'], element['nutrition_grade_fr'], element['url'])
                self.curs.execute(self.products_insert, self.data)

    def products_select(self):
        '''Pick the product using its category and then its name'''
        pass

    def substitutes_select(self):
        '''Show substitutes with higher nutritive grades than the original product'''
        pass

    def save_favorites(self):
        '''Allow the user to save his query into the database'''
        pass

    def favorites_select(self):
        '''Print all the previously saved favorites'''
        pass

    def db_closing(self):
        '''Closing the database'''
        self.curs.close()
        self.connexion.close()
