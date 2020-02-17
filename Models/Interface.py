#! /usr/bin/env python3
# coding: utf-8

from Models.Categories import Categories
from Models.Products import Products
from Models.Favorites import Favorites


class Interface:
    '''A class to centralize the database interactions with the terminal'''
    def get_categories(self, sql_data):
        """ Transform the cat datas into python objects """
        self.cat_list = []
        for element in sql_data:
            data = Categories(id_cat = element[0], name = element[1])
            self.cat_list.append(data)
        return self.cat_list

    def get_products(self, sql_data):
        """ Transform the products datas into python objects """
        self.prod_list = []
        for element in sql_data:
            data = Products(id = element[0], name = element[1], nova_group = element[2])
            self.prod_list.append(data)
        return self.prod_list

    def get_substitutes(self, sql_data):
        """ Transform the substituted one and the substitute one datas into python objects """
        self.sub_list_1 = [] #stores the substituted datas
        self.sub_list_2 = [] #stores the substitute datas
        for element in sql_data:
            data1 = Products(name=element[0], nova_group=element[1])
            data2 = Products(id=element[2], name=element[3], description=element[4], nova_group=element[5])
            self.sub_list_1.append(data1)
            self.sub_list_2.append(data2)
        return self.sub_list_1, self.sub_list_2

    def show_sub_details(self, sql_data):
        """ Transform the products datas into python objects, when the user wants to reveal details """
        self.sub_details_list = []
        for element in sql_data:
            data = Products(name = element[0], description = element[1], stores = element[2], 
                            nova_group = element[3], code = element[4], url = element[5])
            self.sub_details_list.append(data)
        return self.sub_details_list

    def get_favorites(self, sql_data1, sql_data2):
        """ Transform the favorites datas into python objects """
        self.fav_list_1 = [] #stores the id
        self.fav_list_2 = [] #stores the sub product name
        self.fav_list_3 = [] #stores the original product name
        for element in sql_data1:
            data1 = Favorites(id = element[0])
            data2 = Products(name = element[1])
            self.fav_list_1.append(data1)
            self.fav_list_2.append(data2)
        for element in sql_data2:
            data3 = Products(name = element[0])
            self.fav_list_3.append(data3)
        return self.fav_list_1, self.fav_list_2, self.fav_list_3
