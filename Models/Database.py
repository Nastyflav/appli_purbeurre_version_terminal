#! /usr/bin/env python3
# coding: utf-8
'''Manage the database in every ways, connexion, creation, insertion, error issues'''

import mysql.connector as con

from Settings.constants import *


class Database:
    '''Manage all the primary aspects regarding the database as connexion, error issues, data selection'''
    def __init__(self):
        '''No connexion yet'''
        self.connexion = False
        self.curs = False

    def db_creation(self, file):
        '''Create a database in the user's system using instructions in an init MySQL file'''
        self.curs.execute(DB_CREATION.format(DB_NAME))

    def db_connexion(self):
        '''Use mysql.connector to allow access to the chosen database'''
        self.connexion = con.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        self.curs = self.connexion.cursor(buffered=True)

    def products_insert(self, insert, data):
        '''Method to insert the products from the API to the database'''
        self.curs.execute(insert, data)
        self.connexion.commit()

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
