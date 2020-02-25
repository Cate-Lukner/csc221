#! python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of the text on the clipboard

import pyperclip
text = pyperclip.paste()

#TODO: Seperate lines and add stars

lines = text.split('\n')
for line in range(len(lines)): # loop through all indexes in the "lines" list
    lines[line] = '* ' + lines[line] # add start to each string in "lines" list

text = '\n'.join(lines) # join with a new line
pyperclip.copy(text)
