#! /usr/bin/env python3
# coding: utf-8
'''One main method to run the entire program'''

from Models.LaunchApp import LaunchApp
from Models.Database import Database
from Models.APIRequest import APIRequest

def main():

    launch = LaunchApp()
    launch.regular_start()

if __name__ == "__main__":
    main()