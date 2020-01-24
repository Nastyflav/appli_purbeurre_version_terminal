#! /usr/bin/env python3
# coding: utf-8

from Models.APIRequest import APIRequest
from Models.Database import Database
from Settings.constants import *


class Interface:
    '''A class to centralize the database interactions with the terminal'''
    def __init__(self):
        self.database = Database(api)

    def product_display(self):
        '''How every product is displayed into the terminal'''
        print('====Fiche produit====')
        print(f'Nom : ')
        print(f'Catégorie(s) : ')
        print(f'Description : ')
        print(f'Groupe Nova (traceur qualité): ')
        print(f'Code-barre : ')
        print(f'Lien : ')

    def category_choice(self):
        '''Method to make a first selection level by category from the DB'''
        print('====Chargement des catégories====')

    def food_choice(self):
        '''Method to achieve the selection among all products from a category'''
        print('====Chargement des produits====')
        self.database.select_products()
        print('====Chargement terminé====')
        self.product_display()

    def substitutes_proposal(self):
        '''Select from the DB a list of similar products, with higher grades'''
        print('====Chargement des substituts====')
        self.database.select_substitutes()
        print('====Chargement terminé====')

    def substitutes_saving(self):
        '''The user can save his query result'''
        print('====Enregistrement dans vos favoris====')
        self.database.save_products()
        print('====Enregistrement terminé====')

    def favorites_from_db(self):
        '''The user can directly look at his previous saves'''
        print('====Chargement de vos favoris====')
        self.database.select_favorites()
        print('====Chargement terminé====')

