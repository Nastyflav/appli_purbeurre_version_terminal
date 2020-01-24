#! /usr/bin/env python3
# coding: utf-8
'''We import requests to load all the targeted datas from the OFF API'''
import requests as rq

from Settings.constants import API_PAGE_SIZE, API_PAGES_NUMBER, API_CATEGORIES, API_URL_SOURCE, \
                                DB_PRODUCTS_INSERT, DB_CATEGORIES_INSERT


class APIRequest:
    '''Class to load a data list from the OFF API products into the database'''
    def __init__(self):
        '''Define the category products we want'''
        self.categories = API_CATEGORIES
        self.products_list = []

    def data_loading(self):
        '''Make a request to the API and fill the products list'''
        for category in self.categories:
            pages = API_PAGES_NUMBER
            for x in pages:
                payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',  \
                        'tag_0': self.categories, 'page_size': API_PAGE_SIZE, 'page': x, 'json': 1}
                request = rq.get(API_URL_SOURCE, params=payload)
                datas = request.json() # json decoder, raises an exception in case of json decoding fails#
                self.products_list.append(datas)
