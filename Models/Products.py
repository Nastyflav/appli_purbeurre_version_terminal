#! /usr/bin/env python3
# coding: utf-8


class Products:
    """A very small class to define what it is, and to be properly used by the Interface"""
    def __init__(self, id, name, description, category_id,
                 stores, nova_group, code, url):
        self.id = id
        self.name = name
        self.description = description
        self.category_id = category_id
        self.stores = stores
        self.nova_group = nova_group
        self.code = code
        self.url =url
