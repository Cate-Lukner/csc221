''' Strong Password Detection

Author: <your name>
'''

import re

def strong_password(string):
    '''Given a string, return True if is strong, False otherwise

    A strong password is definied as one that is at least eight
    characters logn, contains both uppercase and lowercase characters,
    and has at least one digit.

    '''
    # Regex to test for at least 8 characters, one uppercase, one lowercase, and one digit
    if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[\w\d\W]{8,}', string):
        return True
    else:
        return False
    

