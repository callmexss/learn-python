#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: bagels.py
"
"        Author: xss - callmexss@126.com
"   Description: A game
"        Create: 2018-06-30 17:21:14
"""""""""""""""""""""""""""""""""""""""""""""""

import random


def generate_secret():
    secret = random.randint
    secret_str = str(secret(100, 999))
    while len(set(secret_str)) != 3:
        secret_str = str(secret(100, 999))
    return secret_str


def play_again():
    ans = input('Play again? y or n: ')
    return True if ans.lower() == 'y' else False


def get_plots(guess, secret):
    plots = []
    for i in range(3):
        # print(guess[i], secret[i])
        if guess[i] in secret:
            if guess[i] == secret[i]:
                plots.append('fermi')
            else:
                plots.append('pico')
        else:
            continue
    if not plots:
        return "bagels"
    return ' '.join(plots)


def mainloop():
    while 1:
        win = False
        secret = generate_secret()

        for i in range(10):
            guess = input('Guess the secret: ')

            if guess == secret:
                print('You win!')
                win = True
                break

            else:
                plots = get_plots(guess, secret)
                print(plots)

        if win:
            if play_again():
                continue
            else:
                break
        else:
            print('Run out of try times!')
            print('The secret is', secret)
            if not play_again():
                break


if __name__ == "__main__":
    tag = input('Ready? y or n: ')
    if tag:
        mainloop()
