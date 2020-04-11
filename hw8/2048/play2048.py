#!/usr/bin/env python
''' 
Since I am not into playing video games, but want a score to show off
to my brothers, play2048.py will play 2048 game for me. 

Author: Cate Lukner
'''

# imports
import argparse
import pyautogui as pag
import time
import webbrowser

def open_webbrowser(url):
    # Open the game 
    webbrowser.open(url)
    print('Be sure not to click out of the browser that will open!')
    # To give time for my slow internet connection to load
    time.sleep(5)
    return active_window

def play_game(game_window):
    # TODO: boolean - test if game screen is active
    # TODO: Check for gameover conditons - end game once over
    # TODO: Add pause period of 5 seconds every 30 seconds
    while True:
        pag.press(['up', 'right', 'down', 'left'])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The URL to the form to be filled.')

    args = parser.parse_args()

    game_window = open_webbrowser(args.url)
    play_game(game_window)

if __name__=='__main__':
    main()

