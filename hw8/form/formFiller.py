#!/usr/bin/env python
''' Automatic Form Filler

Author: Cate Lukner
'''
# imports
import argparse
import pyautogui as pag
import time
import webbrowser

SUBMIT_ANOTHER_RESPONSE = (172, 231)

FORMDATA = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]

def open_webbrowser(url):
    # Open the form
    webbrowser.open(url)
    print('Be sure not to click out of the browser that will open!')
    # To give time for my slow internet connection to load
    time.sleep(5)

def fill_form(form_data):
    for person in form_data:
        # Give the user a chance to kill the script.
        print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
        time.sleep(5)
    
        print('Entering %s info...' %(person['name']))
        pag.write(['\t', '\t'])

        # Fill out the Name field.
        pag.write(person['name'] + '\t')

        # Fill out the Greatest Fear(s) field.
        pag.write(person['fear'] + '\t')

        # Fill out the Source of Wizard Powers field.
        if person['source'] =='wand':
            pag.write(['down', 'enter', '\t'], 0.5)
        elif person['source']=='amulet':
            pag.write(['down', 'down', 'enter', '\t'], 0.5)
        elif person['source']=='crystal ball':
            pag.write(['down', 'down', 'down', 'enter', '\t'], 0.5)
        elif person['source']=='money':
            pag.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.5)
        
        # Fill out the RoboCop field
        if person['robocop']==1:
            pag.write(['right', 'left', '\t'], 0.5)
        elif person['robocop']==2:
            pag.write(['right', '\t'], 0.5)
        elif person['robocop']==3:
            pag.write(['right', 'right', '\t'], 0.5)
        elif person['robocop']==4:
            pag.write(['right', 'right', 'right', '\t'], 0.5)
        elif person['robocop']==5:
            pag.write(['right', 'right', 'right', 'right', '\t'], 0.5)

        # Fill out the Additonal comments field
        pag.write(person['comments'] + '\t')

        # Click Submit buttom by pressing Enter
        time.sleep(0.5) # Wait for button to activate.
        pag.press('enter')
        
        # Wait until form page has loaded
        print('Submitted form.')
        time.sleep(5)

        # Click the Submit another response link.
        pag.click(SUBMIT_ANOTHER_RESPONSE[0], SUBMIT_ANOTHER_RESPONSE[1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The URL to the form to be filled.')

    args = parser.parse_args()

    open_webbrowser(args.url)
    fill_form(FORMDATA)

if __name__=='__main__':
    main()

