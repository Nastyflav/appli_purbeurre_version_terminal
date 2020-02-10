#! /usr/bin/env python3
# coding: utf-8
from random import sample

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
        self.running = False

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
        
        self.running = True
        while self.running:
            self.menu()
            menu_choice = self.ctrl.binary_choice()
            
            if menu_choice == 1 :
                self.app_cat_query()
                cat_nb = self.db.select_categories()
                cat_choice = self.ctrl.cat_choice(cat_nb)
                self.db.select_products(cat_choice)
                self.app_prod_query()
                prod_nb = self.db.select_products(cat_choice)
                prod_choice = self.ctrl.prod_choice(prod_nb)
                self.db.select_substitutes(cat_choice, prod_choice)
                self.app_sub_query()
            
            else:
                self.app_fav_query()
                self.app_closing()
                end_choice = self.ctrl.binary_choice()
                if end_choice == 1:
                    self.running = True
                else:
                    self.db.database_closing()
                    self.running = False

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
        print('========RECHERCHE TERMINÉE========')
        print()
        print('Que souhaitez-vous faire ?\
        \nPour revenir à l\'accueil -> Tapez 1\
        \nPour quitter le programme -> Tapez 2')

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
        self.text = '''=======ALIMENTS=======\
        \nChoisissez un produit à substituer en tapant son numéro :'''
        self.products = sample(self.db.selected_products, 10)
        i = 0
        for product in self.products:
            i += 1
            self.prod_choices = '\n{} / NOVA Groupe : {} ->'.format(product.name, product.nova_group, product.id) + str(i)
            self.text = self.text + self.prod_choices
        print(self.text)    

    def app_sub_query(self):
        """Call the database to show an certain amount of substitutes regarding its grade"""
        print('''=======PRODUIT À REMPLACER=======''')
        self.text = '''=======BETTER, HEALTHIER, TASTIER======='''
        self.substitutes = sample(self.db.substitute, 10)
        for original, substitute in zip(self.db.original_prod, self.substitutes):
            self.recall = '\nVoici les substituts pour {}, Nova GROUPE : {}'.format(original.name, original.nova_group)
            self.sub_choices = '\n{}, {}, Groupe NOVA : {} ->{}'\
                                .format(substitute.name, substitute.description, substitute.nova_group, substitute.id) 
            self.text = self.text + self.sub_choices
        print(self.recall)
        print()
        print(self.text)

    def favorite_details(self):
        """Show to the user the details of the selected substitute"""
        self.db.show_substitut(847)
        self.text = '''=======SUBSTITUT SÉLECTIONNÉ======='''
        for product in self.db.selected_substitute:
            self.product_card = """\nNom : {}
                \nDescription : {} 
                \nGroupe Nova : {}
                \nDisponible chez : {}
                \nCode-barre : {}
                \nEn savoir plus : {}""".format(product.name, product.description, product.nova_group, 
                                                product.stores, product.code, product.url)
            self.text = self.text + self.product_card
        print(self.text)

    def app_fav_query(self):
        '''If the user wants to take a look at his previous queries'''
        print('=======HALL OF FAME=======')
        # self.db.favorites_from_db()