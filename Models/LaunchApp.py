#! /usr/bin/env python3
# coding: utf-8

from Models.APIRequest import APIRequest
from Models.Database import Database
from Models.Interface import Interface
from Controllers.KeyboardController import KeyboardController
from Settings.constants import *


class LaunchApp:
    '''Define what happens when someone is using the app'''
    def __init__(self):
        self.api = APIRequest()
        self.db = Database(self.api)
        self.ctrl = KeyboardController()

    def regular_start(self):
        '''Start and close the app when the database is already created'''
        print('====PUR BEURRE, l\'application====')
        print()
        self.db.database_connexion()
        if self.db.database_selection() == False:
            self.db.database_creation()
            self.db.database_selection()
        
        if self.db.database_check_in() is None:
            self.first_start()
    
        self.menu()
        menu_choice = self.ctrl.binary_choice()
        if menu_choice == 1 :
            self.app_cat_query()
        else:
            self.app_fav_query()
                # If category choice is choosen
                    # self.app_query()
                # if favorites is choosen
                    # self.favorites_query()
            # Do you still want to use the app ?
                # If not:
                    # self.app_closing()
                # Else:
                    #continue = True

    def first_start(self):
        '''When database is missing or first use of the app'''
        print('=====Les stocks sont au plus bas !====')
        print('=====Téléchargement des données====')
        self.api.data_loading()
        print('=====Reconstitution des stocks en cours====')
        self.db.products_recording(self.api)
        print('====Votre magasin est désormais opérationnel !====')

    def app_closing(self):
        '''To close properly the app'''
        # self.db.database_closing()

    def menu(self):
        """First interaction with the user, who has to chose 
        between the favorites or the categories menu"""
        print('Que souhaitez-vous faire ?\
        \nPour consulter les catégories d\'aliments disponibles -> Tapez 1\
        \nPour consulter vos aliments favoris -> Tapez 2')

    def app_cat_query(self):
        """Call the database to show all the available category"""
        self.db.select_categories()
        self.text = '''========CATEGORIES========\
        \nChoisissez un type d'aliment en tapant son numéro :'''
        for category in self.db.selected_cat:
            self.cat_choices = '\n{} -> {}'.format(category.name, category.id)
            self.text = self.text + self.cat_choices
        print(self.text)

    def app_prod_query(self):
        """Call the database to show an certain amount of products regarding its category"""
        self.db.select_products()
        self.text = '''=======ALIMENTS=======\
        \nChoisissez un produit à substituer en tapant son numéro :'''
        for product in self.db.selected_products:
            self.prod_choices = '\n{} / NOVA Groupe : {} -> {}'.format(product.name, product.nova_group, product.id)
            self.text = self.text + self.prod_choices
        print(self.text)    

    def app_sub_query(self):
        """Call the database to show an certain amount of substitutes regarding its grade"""
        self.db.select_substitutes(1, 1, 13)
        self.text = '''=======BETTER, HEALTHIER, TASTIER======='''
        for product in self.db.original_prod:
            self.recall = '\nVoici les substituts pour {}, Nova GROUPE : {}'.format(product.name, product.nova_group)
        for sub in self.db.substitute:
            self.sub_choices = '\n{}, {}, Groupe NOVA : {}, disponible chez : {}, en savoir plus : {}'\
                                .format(product.name, product.description, product.nova_group, product.stores, product.url) 
            self.text = self.text + self.recall + self.sub_choices
        print(self.text)

    def app_fav_query(self):
        '''If the user wants to take a look at his previous queries'''
        print('=======HALL OF FAME=======')
        # self.db.favorites_from_db()