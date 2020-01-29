#! /usr/bin/env python3
# coding: utf-8
'''One main method to run the entire program'''

from Models.APIRequest import APIRequest
from Models.Database import Database
from Models.Interface import Interface
from Models.LaunchApp import LaunchApp

def main():

    api = APIRequest()
    db = Database(api)
    api.data_loading()
    db.database_connexion()
    db.database_selection()
    # db.database_check_in()
    db.products_recording(api)
    # db.database_creation()

    # launch = LaunchApp()
    # launch.regular_start()

if __name__ == "__main__":
    main()