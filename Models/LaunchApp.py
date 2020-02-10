#! /usr/bin/env python3
# coding: utf-8
'''Import sample from random to pick a few products and subs to make easier the reading on screen'''
from random import sample

from Models.APIRequest import APIRequest
from Models.Database import Database
from Models.Interface import Interface
from Controllers.KeyboardController import KeyboardController


class LaunchApp:
    '''Define what happens when someone is using the app'''
    def __init__(self):
        self.api = APIRequest()
        self.db = Database(self.api)
        self.ctrl = KeyboardController()
        self.running = False
        self.answer = 0

    def regular_start(self):
        '''Start and close the app when the database is already created'''
        print('====PUR BEURRE, l\'application====')
        print()
        self.db.database_connexion() #Checking if there's a matching database
        if self.db.database_selection() == False:
            self.db.database_creation() #If not we create it
            self.db.database_selection()
        
        if self.db.database_check_in() is None: #Checking if the database is filled with products
            self.first_start() # If not we fill it with the API datas
        
        self.running = True
        while self.running:
            self.menu()
            menu_choice = self.ctrl.binary_choice()
            
            if menu_choice == 1: #All the process from choosing a categorie to save or not a substitute into the database
                self.app_cat_query()
                cat_nb = self.db.select_categories()
                cat_choice = self.ctrl.cat_choice(cat_nb)
                self.db.select_products(cat_choice)
                self.app_prod_query()
                prod_nb = self.db.select_products(cat_choice)
                prod_choice = self.ctrl.prod_choice(prod_nb)
                self.db.select_substitutes(cat_choice, prod_choice)
                self.app_sub_query()
                sub = self.ctrl.sub_choice(prod_nb)
                self.db.show_substitute(sub)
                self.subs_details()
                self.sub_saving()
                save_choice = self.ctrl.binary_choice()

                if save_choice == 1: #if the user choses to save his query
                    self.db.save_favorites(sub, prod_choice)
                    print('========ENREGISTREMENT EFFECTUÉ========')
                    self.app_closing()
                    end_choice = self.ctrl.binary_choice()
                    if end_choice == 1:
                        self.running = True
                else: #if the user choses to not save his query, he can end the app or start over
                    self.app_closing()
                    end_choice = self.ctrl.binary_choice()
                    if end_choice == 1:
                        self.running = True
                    else:
                        self.db.database_closing()
                        self.running = False

            
            else: #Only deals with the action of consulting the saved favorites
                self.app_fav_query()
                fav_nb = self.db.select_favorites()
                fav = self.ctrl.fav_choice(fav_nb)
                self.db.show_favorite(fav)
                self.favorite_details()
                self.app_closing()
                end_choice = self.ctrl.binary_choice()
                if end_choice == 1: #the user goes back to the starting menu
                    self.running = True
                else: #disconnect the database and close the app
                    self.db.database_closing()
                    self.running = False

    def first_start(self):
        '''When datas are missing or first use of the app'''
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
        print()
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
        for product in self.products:
            self.prod_choices = '\n{} -> {} / NOVA Groupe : {}'.format(product.id, product.name, product.nova_group)
            self.text = self.text + self.prod_choices
        print(self.text)    

    def app_sub_query(self):
        """Call the database to show an certain amount of substitutes regarding its grade"""
        print('''=======PRODUIT À REMPLACER=======''')
        self.text = '''=======BETTER, HEALTHIER, TASTIER======='''
        self.substitutes = sample(self.db.substitute, 10)
        for original, substitute in zip(self.db.original_prod, self.substitutes):
            self.recall = '\nVoici les substituts pour {}, Nova GROUPE : {}'.format(original.name, original.nova_group)
            self.sub_choices = '\n{} -> {}, {}, Groupe NOVA : {}'.format(substitute.id, substitute.name, substitute.description, substitute.nova_group)
            self.text = self.text + self.sub_choices
        print(self.recall)
        print()
        print(self.text)

    def subs_details(self):
        """Show to the user the details of the selected substitute"""
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

    def sub_saving(self):
        '''Give the user the choice to save or not the printed substitute'''
        print()
        print('Que souhaitez-vous faire ?\
        \nPour conserver ce substitut dans votre base de données -> Tapez 1\
        \nPour clôturer la recherche -> Tapez 2')

    def app_fav_query(self):
        '''If the user wants to take a look at his previous queries'''
        self.db.select_favorites()
        self.text = ('=======HALL OF FAME=======')
        for id, favorite, original in zip(self.db.id, self.db.favorite, self.db.original):
            self.saves = '\n{} -> {}, comme substitut à {}'.format(id.id, favorite.name, original.name)
            self.text = self.text + self.saves
        print(self.text)

    def favorite_details(self):
        """Show to the user the details of the selected substitute"""
        self.text = '''=======SUBSTITUT SÉLECTIONNÉ======='''
        for favorite in self.db.selected_favorite:
            self.favorite_card = """\nNom : {}
                \nDescription : {} 
                \nGroupe Nova : {}
                \nDisponible chez : {}
                \nCode-barre : {}
                \nEn savoir plus : {}""".format(favorite.name, favorite.description, favorite.nova_group, 
                                                favorite.stores, favorite.code, favorite.url)
            self.text = self.text + self.favorite_card
        print(self.text)
        