#! /usr/bin/env python3
# coding: utf-8

from Models.Categories import Categories
from Models.Products import Products
from Models.Favorites import Favorites
from Settings.constants import *


class Interface:
    '''A class to centralize the database interactions with the terminal'''
    @classmethod
    def get_categories(cls, sql_data):
        """ transform sql data (id and name of categories) to python object """
        object_list = []
        for element in sql_data:
            data = Categories(id_cat = element[0], name = element[1])
            object_list.append(data)
        return object_list

    @classmethod
    def transform_foods_to_object(cls, sql_data):
        """ transform sql data (id and name of foods) to python object """
        object_list = []

        for elt in sql_data:
            data = model.Food(foods_id=elt[0], name_food=elt[1])
            object_list.append(data)

        return object_list

    @classmethod
    def transform_substitute_to_object(cls, sql_data):
        """ transform sql data (name and nustriscore of food chooses
        and the substitute information) to python object """
        object_list_1 = []
        object_list_2 = []

        for elt in sql_data:
            data1 = model.Food(name_food=elt[0], nutriscore=elt[1])
            data2 = model.Food(name_food=elt[2], nutriscore=elt[3],
                               description=elt[4], store=elt[5], link=elt[6])
            object_list_1.append(data1)
            object_list_2.append(data2)

        return object_list_1, object_list_2

    @classmethod
    def transform_favorite_foods_to_object(cls, sql_data1, sql_data2):
        """ transform sql data (favorite food name
        and id, name of its substitute) to python object """
        object_list_1 = []
        object_list_2 = []
        object_list_3 = []

        for elt in sql_data1:
            data1 = model.Favorite(favorite_id=elt[0])
            data2 = model.Food(name_food=elt[1])
            object_list_1.append(data1)
            object_list_2.append(data2)

        for elt in sql_data2:
            data3 = model.Food(name_food=elt)
            object_list_3.append(data3)

        return object_list_1, object_list_2, object_list_3

    @classmethod
    def transform_detail_substitute_to_object(cls, sql_data):
        """ transform sql data (substitute information) to python object """
        object_list = []

        for elt in sql_data:
            data = model.Food(name_food=elt[0], nutriscore=elt[1],
                              description=elt[2], store=elt[3], link=elt[4])
            object_list.append(data)

        return object_list

# class Interface:
#     '''A class to centralize the database interactions with the terminal'''
#     def __init__(self):
#         self.database = Database(api)

#     def product_display(self):
#         '''How every product is displayed into the terminal'''
#         print('====Fiche produit====')
#         print(f'Nom : ')
#         print(f'Catégorie(s) : ')
#         print(f'Description : ')
#         print(f'Groupe Nova (traceur qualité): ')
#         print(f'Code-barre : ')
#         print(f'Lien : ')

#     def food_choice(self):
#         '''Method to achieve the selection among all products from a category'''
#         print('====Chargement des produits====')
#         self.database.select_products()
#         print('====Chargement terminé====')
#         print('====ALIMENTS====')
#         self.product_display()
#         print('Choisissez un produit à substituer en tapant son numéro :')

#     def substitutes_proposal(self):
#         '''Select from the DB a list of similar products, with higher grades'''
#         print('====Chargement des substituts====')
#         self.database.select_substitutes()
#         print('====Chargement terminé====')
#         print('BETTER, HEALTHIER, TASTIER')
#         print('Souhaitez vous placer ce produit dans vos favoris ? \
#         Oui - Tapez 1 \
#         Non - Tapez 2')

#     def substitutes_saving(self):
#         '''The user can save his query result'''
#         print('====Enregistrement dans vos favoris====')
#         self.database.save_products()
#         print('====Enregistrement terminé====')

#     def favorites_from_db(self):
#         '''The user can directly look at his previous saves'''
#         print('====Chargement de vos favoris====')
#         self.database.select_favorites()
#         print('====Chargement terminé====')
#         print('====HALL OF FAME====')

