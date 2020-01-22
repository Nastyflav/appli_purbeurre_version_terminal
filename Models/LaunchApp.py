#! /usr/bin/env python3
# coding: utf-8

from Models.APIRequest import APIRequest
from Models.Database import Database
from Models.Interface import Interface
from Settings.constants import *


class LaunchApp(self):
    '''Define what happens when someone is using the app'''
    def __init__(self):
        pass

    def regular_start(self):
        '''Start and close the app when the database is already created'''
        pass

    def first_start(self):
        '''When database is missing or first use of the app'''
        pass

    def app_closing(self):
        '''To close properly the app'''
        pass

    def app_query(self):
        '''Call every searching methods from Database() to find substitutes products'''
        pass

    def favorites_query(self):
        '''If the user wants to take a look at his previous queries'''
        pass