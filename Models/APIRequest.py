#! /usr/bin/env python3
# coding: utf-8
'''We import requests to load all the targeted datas from the OFF API\
and mysql.connector to fill the database'''
import requests as rq
import mysql.connector as con

from Settings.constants import API_PAGE_SIZE, API_PAGES_NUMBER, API_CATEGORIES, API_URL_SOURCE


class APIRequest:
    '''Class to load a data list from the OFF API products into the database'''
    def __init__(self):
        '''Define the category products we want'''
        self.categories = API_CATEGORIES
        self.products_list = []

    def data_loading(self):
        '''Make a request to the API and fill the products list'''
        for element in self.categories:
            pages = API_PAGES_NUMBER
            for x in pages:
                payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
                       'tag_0': element, 'sort_by': 'unique_scans', 'page_size': API_PAGE_SIZE, 'page': x,
                       'json': '1'}
                request = rq.get(API_URL_SOURCE, params=payload)
                datas = request.json()#json decoder, raises an exception in case of json decoding fails#
                self.products_list.append(datas)

    def data_recording(self):
        '''Pick precisely each chosen data and record it into the database'''
        self.mydb = con.connect(host="localhost",user="root",password="Flying14!", database="essai1")
        self.curseur = self.mydb.cursor()
        self.insert = 'INSERT INTO products (name, description, barcode, store, nova_groups, url)\
                                 VALUES (%s, %s, %s, %s, %s, %s)'

        for result in self.products_list:
            for element in result['products']:
                # print(element)
                # exit(0)
                self.data = (element['product_name'], element['generic_name_fr'], element['unique_scans_n'], \
                             element['stores'], element['nutrition_grade_fr'], element['url'])
                self.curseur.execute(self.insert, self.data)
                
            self.mydb.commit()
        self.mydb.close()