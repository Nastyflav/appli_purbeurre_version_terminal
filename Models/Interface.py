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
        """ Transform the cat datas into python objects """
        cat_list = []
        for element in sql_data:
            data = Categories(id_cat = element[0], name = element[1])
            cat_list.append(data)
        return cat_list

    @classmethod
    def get_products(cls, sql_data):
        """ Transform the product datas into python objects """
        prod_list = []
        for element in sql_data:
            data = Products(id = element[0], name = element[1], nova_group = element[2])
            prod_list.append(data)
        return prod_list

    @classmethod
    def get_substitutes(cls, sql_data):
        """ Transform the the substituted one and the substitute one datas into python objects """
        sub_list_1 = []
        sub_list_2 = []
        for element in sql_data:
            data1 = Products(name=element[0], nova_group=element[1])
            data2 = Products(id=element[2], name=element[3], description=element[4], nova_group=element[5])
            sub_list_1.append(data1)
            sub_list_2.append(data2)
        return sub_list_1, sub_list_2

    @classmethod
    def show_sub_details(cls, sql_data):
        """ Transform the product datas into python objects """
        sub_details_list = []
        for element in sql_data:
            data = Products(name = element[0], description = element[1], stores = element[2], 
                            nova_group = element[3], code = element[4], url = element[5])
            sub_details_list.append(data)
        return sub_details_list

    @classmethod
    def transform_favorite_foods_to_object(cls, sql_data1, sql_data2):
        """ transform sql data (favorite food name
        and id, name of its substitute) to python object """
        fav_list_1 = []
        fav_list_2 = []
        fav_list_3 = []
        for element in sql_data1:
            data1 = Favorite(id = element[0])
            data2 = Products(name = element[1])
            fav_list_1.append(data1)
            fav_list_2.append(data2)
        for element in sql_data2:
            data3 = Products(name = element)
            fav_list_3.append(data3)

        return fav_list_1, fav_list_2, fav_list_3
