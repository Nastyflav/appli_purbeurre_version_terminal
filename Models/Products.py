#! /usr/bin/env python3
# coding: utf-8


class Products:
    """A very small class to define what a product is, and to be properly used by the Interface"""
    def __init__(self, id = None, name = None, description = None, category_id = None,
                 stores = None, nova_group = None, code = None, url = None):
        self.id = id
        self.name = name
        self.description = description
        self.category_id = category_id
        self.stores = stores
        self.nova_group = nova_group
        self.code = code
        self.url =url
