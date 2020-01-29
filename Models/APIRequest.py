#! /usr/bin/env python3
# coding: utf-8
'''We import requests to load all the targeted datas from the OFF API'''
import requests as rq
import json

from Settings.constants import API_PAGE_SIZE, API_PAGES_NUMBER, API_CATEGORIES, API_URL_SOURCE, \
                                DB_PRODUCTS_INSERT, DB_CATEGORIES_INSERT


class APIRequest:
    '''Class to load a data list from the OFF API products into the database'''
    def __init__(self):
        '''Define the category products we want'''
        self.categories = API_CATEGORIES
        self.products_list = []
        self.keys = ['product_name', 'generic_name_fr', 'stores', 'nova_groups', 'code', 'url']

    def data_loading(self):
        '''Make a request to the API and sort all the datas'''
        
        for category in self.categories:
            pages = API_PAGES_NUMBER
            for page in range(pages):
                payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',  \
                        'tag_0': category, 'page_size': API_PAGE_SIZE, 'page': (page + 1), 'json': 1}
                self.request = rq.get(API_URL_SOURCE, params=payload)
                self.json_data = json.loads(self.request.text)
                with open('results.json', 'w') as f:
                    f.write(json.dumps(self.json_data, indent=4))

                for data in self.json_data['products']: # using the keys to select every product even if some keys are missing
                    self.temp_dict = {}
                    if self.keys[0] in data and self.keys[1] in data and self.keys[2] in data and self.keys[3] \
                     in data and self.keys[4] in data and self.keys[5] in data:
                        for key in self.keys:
                            self.temp_dict[key] = data[key]                 
                    self.products_list.append(self.temp_dict)
                
                while {} in self.products_list:
                    self.products_list.remove({})    
                print(self.products_list)