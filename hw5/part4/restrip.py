''' Regex Version of strip

Author: Cate Lukner 
'''

import re

def restrip(string, chars=None):
    '''Given a string, do the same thing as the strip() string method.

    If no other arguments are passed other than the string, then
    whitespace characters will be removed from the beginning and end
    of the string. Otherwise, the characters speci ed in the second
    argu- ment to the function will be removed from the string.

    '''

    # Strip white space at beginning or end of string if no chars passed
    if chars == None:
        strip = re.compile(r'^\s+|\s+$')
        striped_string = strip.sub('', string)
        return striped_string
    # Strip characters specified by chars arguement
    else:
        strip = re.compile(r'^{}+|{}+$'.format(chars,chars))
        striped_string = strip.sub('', string)
        return striped_string
        
