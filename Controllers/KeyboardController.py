#! /usr/bin/env python3
# coding: utf-8


class KeyboardController:

    def __init__(self):
        pass

    def binary_choice(self):
        print()
        user_answer = input('Validez votre choix avec Entrée : ')
        if user_answer not in ['1', '2']:
            print('Cette option n\'existe pas, veuillez choisir entre les numéros proposés')
            user_answer = self.binary_choice()
        return int(user_answer)

    def cat_choice(self, cat_nb):
        print()
        user_answer = input('Validez votre choix avec Entrée : ')
        if not (1 <= int(user_answer) <= len(cat_nb)):
            print('Cette option n\'existe pas, veuillez choisir entre les numéros proposés')
            user_answer = self.cat_choice(cat_nb)
        return int(user_answer)
