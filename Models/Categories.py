#! /usr/bin/env python3
# coding: utf-8

class Categories:
    """Category class used by 'Pur Beurre' application.
    Data come from Open Food Facts french database.
    """
    def __init__(self, id_cat, name):
        self.id = id_cat
        self.name = name
