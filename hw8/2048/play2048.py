#!/usr/bin/env python
''' 
Since I am not into playing video games, but want a score to show off
to my brothers, play2048.py will play 2048 game for me. 

Author: Cate Lukner
'''

# imports
import pyautogui as pag
import time
import webbrowser

URL = 'https://gabrielecirulli.github.io/2048/'
RUN_TIME = 30 
PAUSE_TIME = 5

def open_webbrowser(url):
    ''' Opens the game '''
    # Open the game 
    webbrowser.open(url)
    print('Be sure not to click out of the browser that will open!')
    # To accomodate my slow internet
    time.sleep(5)

def play_game():
    ''' Follows the up, right, down, left arrow key pattern to play.'''
    pag.press(['up', 'right', 'down', 'left'])

def check_game_over():
    ''' Checks for Try Again button on the screen. If it does not exist, it
    returns True. If the Try Again button does exist, it returns False.'''
    # Locate Try Again button
    try_again = pag.locateOnScreen('try_again_button.png', confidence=0.8)   
    # Return True or False based on existence of Try Again button
    if not try_again:
        return True
    elif try_again:
        return False

def main():
    '''Main function'''
    # Open game
    open_webbrowser(URL)

    # Set the start time
    time_start = time.time()
    
    # Play game for the set run time then pause
    while check_game_over():
        if time.time() < time_start + RUN_TIME:
            play_game()
        else:
            print('Here\'s your chance to kill the script!')
            time.sleep(PAUSE_TIME)
            time_start = time.time()

if __name__=='__main__':
    main()

