#! /usr/bin/env python3
# coding: utf-8

from Models.APIRequest import APIRequest
from Models.Database import Database
from Settings.constants import *


class Interface:
    '''A class to centralize the user's interactions with the terminal'''
    def __init__(self):
        pass

    def products_display(self):
        '''How every product is displayed into the terminal'''
        pass

    def category_choice(self):
        '''Method to make a first selection level by category from the DB'''
        pass

    def food_choice(self):
        '''Method to achieve the selection among all products from a category'''
        pass

    def substitutes_proposal(self):
        '''Select from the DB a list of similar products, with higher grades'''
        pass

    def substitutes_saving(self):
        '''The user can save his query result'''
        pass

    def favorites_from_db(self):
        '''The user can directly look at his previous saves'''
        pass

