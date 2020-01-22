#! /usr/bin/env python3
# coding: utf-8

from Models.APIRequest import APIRequest
from Models.Database import Database
from Models.Interface import Interface
from Settings.constants import *


class LaunchApp(self):
    '''Define what happens when someone is using the app'''
    def __init__(self):
        self.api = APIRequest()
        self.db = Database(api)
        self.inter = Interface()

    def regular_start(self):
        '''Start and close the app when the database is already created'''
        print('====PUR BEURRE, l\'application====')
        # self.db.database_check_in()
            # if method is None
                # self.first_start()
        # self.db.products_check_in()
        # self.db.database connexion() ???
        # continue = True
        # while continue:
            # Selection menu
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
        print('====Bienvenue sur Pur Beurre====')
        print('====Création de votre base de données en cours====')
        self.database_creation()
        print('=====Les stocks sont au plus bas !====')
        print('=====Téléchargement des données====')
        self.api.data_loading()
        print('=====Reconstitution des stocks en cours====')
        self.database_connexion()
        self.database_recording(api)
        print('====Votre magasin est désormais opérationnel !')

    def app_closing(self):
        '''To close properly the app'''
        # self.db.database_closing()

    def app_query(self):
        '''Call every searching methods from Database() to find substitutes products'''
        # self.db.category_choice()
        # self.db.food_choice()
        # self.db.substitutes_proposal()
        # self.db.substitutes_saving()

    def favorites_query(self):
        '''If the user wants to take a look at his previous queries'''
        print('====Voici vos produits sauvegardés====')
        self.db.favorites_from_db()