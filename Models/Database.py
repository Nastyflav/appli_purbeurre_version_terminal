#! /usr/bin/env python3
# coding: utf-8
'''Manage the database in every ways, connexion, creation, insertion, error issues'''

import mysql.connector as con

from Models.APIRequest import APIRequest
from Settings.constants import *


class Database:
    '''Manage all the primary aspects regarding the database as connexion, error issues, data selection'''
    def __init__(self, api):
        self.filename = FILENAME
        self.api = api
        '''No connexion yet'''
        self.connexion = False
        self.curs = False

    def database_creation(self):
        '''Create a database in the user's system using instructions in an init MySQL file'''
        try:
            with open(self.filename, 'r') as cmd_file:
                sql_commands = cmd_file.read()
                sql_commands = sql_commands.split(';') # Split the file in a list by using ';' as a separator for each SQL command
            for command in sql_commands:
                self.curs.execute(command)
        except FileNotFoundError:
            print("Couldn't open commands file \"" + self.filename + "\"")

    def database_connexion(self):
        '''Use mysql.connector to allow access to the chosen database'''
        self.connexion = con.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database= DB_NAME)
        self.curs = self.connexion.cursor(buffered=True)

    def database_check_in(self):
        '''Check if the database already exists'''
        # if no database name as DB_NAME:
            # method = None

    def products_check_in(self):
        '''Check if the database is properly filled'''
        # if not enough products in the database:
            # self.database_connexion()
            # self.api.data_loading()
            # self.data_recording()
                
    def data_recording(self, api):
        '''Pick precisely each chosen data and record it into the database'''
        print('Enregistrement des produits...')
        self.cat_insert = DB_CATEGORIES_INSERT #first we record in the table Categories
        for result in api.products_list:
            for api.categories in result['products']:
                self.cat_data = (api.categories['categories'])
                print(self.cat_data)
        exit(0)
            #     self.curs.execute(self.cat_insert, self.cat_data)
            # self.connexion.commit()

        self.products_insert = DB_PRODUCTS_INSERT #Then we add all products
        for result in api.products_list:
            for element in result['products']:
                self.data = (element['product_name'], element['generic_name_fr'], element['unique_scans_n'], \
                             element['stores'], element['nutrition_grade_fr'], element['url'])
                self.curs.execute(self.products_insert, self.data)

    def products_select(self):
        '''Pick the product using its category and then its name'''
        pass

    def save_favorites(self):
        '''Allow the user to save his query into the database'''
        self.favorites_insert = DB_FAVORITES_INSERT
        self.fav_data =

    def database_closing(self):
        '''Closing the database'''
        self.curs.close()
        self.connexion.close()
