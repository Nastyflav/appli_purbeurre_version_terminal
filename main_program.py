#! /usr/bin/env python3
# coding: utf-8
'''One main method to run the entire program'''

from Models.APIRequest import APIRequest
from Models.Database import Database
from Models.LaunchApp import LaunchApp

def main():

    api = APIRequest()
    db = Database(api)
    launch = LaunchApp()
    # db.database_connexion()
    # db.database_creation()
    # db.database_selection()
    # db.database_check_in()
    # api.data_loading()
    # db.products_recording(api)

    # launch.app_sub_query()
    launch.regular_start()

if __name__ == "__main__":
    main()