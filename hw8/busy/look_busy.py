#!/usr/bin/env python
'''
Make the mouse stay active while user is stepped away.

Author: Catherine Lukner
'''

import time
import pyautogui as pag
import argparse

SCREEN_SIZE = pag.size()
MAX_UP = (SCREEN_SIZE.width - 10, SCREEN_SIZE.height - 120)
MIN_DOWN = (SCREEN_SIZE.width - 10, SCREEN_SIZE.height - 80)

def mouse_movements():
    '''After waiting 10 seconds, moves the mouse up to the max height. Then,
    it waits another 10 seconds, moves the mouse to the minimum height.'''
    time.sleep(10)
    # Move Up
    pag.moveTo(MAX_UP, duration=0.25)
    time.sleep(10)
    # Move Down
    pag.moveTo(MIN_DOWN, duration=0.25)
    
    
def mouse_loop(timeout):
    ''' Moves the mouse for the specified time or until the user 
    presses CTRL+C'''
    pag.moveTo(MIN_DOWN)

    if timeout:
        print(f'>>> Mouse movement will end in {timeout} minutes. <<<')
        timeout_start = time.time()
        timeout = int(timeout) * 60

        # Move mouse until timeout
        while time.time() < timeout_start + timeout: 
            mouse_movements()

    else:
        print('>>> PRESS CTRL+C TO END THE MOUSE MOVEMENT <<<')
        # Move mouse until user presses CTRL+C
        while True:
            mouse_movements()
        
def main():
    ''' Main function.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', help="Minutes until mouse activity times out")

    args = parser.parse_args()

    if args.timeout:
        mouse_loop(args.timeout)
    else:
        mouse_loop(None)

if __name__=='__main__':
    main()


