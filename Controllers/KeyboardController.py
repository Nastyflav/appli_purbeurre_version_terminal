#! /usr/bin/env python3
# coding: utf-8


class KeyboardController:
    '''Deals with every user / terminal interactions, only by pressing keys on keyboard'''
    def __init__(self):
        pass

    def binary_choice(self):
        '''When the user have to chose between two entries'''
        print()
        user_answer = input('Validez votre choix avec Entrée : ')
        if user_answer not in ['1', '2']:
            print('Cette option n\'existe pas, veuillez choisir entre les numéros proposés')
            user_answer = self.binary_choice()
        return int(user_answer)

    def cat_choice(self, cat_nb):
        '''When the user choses a category to explore'''
        print()
        user_answer = input('Validez votre choix avec Entrée : ')
        if not (1 <= int(user_answer) <= len(cat_nb)):
            print('Cette option n\'existe pas, veuillez choisir entre les numéros proposés')
            user_answer = self.cat_choice(cat_nb)
        return int(user_answer)

    def prod_choice(self, prod_nb):
        '''When the user choses a product to substitute'''
        print()
        user_answer = input('Validez votre choix avec Entrée : ')
        # if not (1 <= int(user_answer) <= len(prod_nb)):
        #     print('Cette option n\'existe pas, veuillez choisir entre les numéros proposés')
        #     user_answer = self.prod_choice(prod_nb)
        return int(user_answer)

    def sub_choice(self, prod_nb):
        '''When the user choses a substitute among a list of proposal'''
        print()
        user_answer = input('Validez votre choix avec Entrée : ')
        # if not (1 <= int(user_answer) <= len(prod_nb)):
        #     print('Cette option n\'existe pas, veuillez choisir entre les numéros proposés')
        #     user_answer = self.prod_choice(prod_nb)
        return int(user_answer)
