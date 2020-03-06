#!/usr/bin/env python3
''' Regex Search

Author: Cate Lukner 
'''

# Imports
import argparse
from pathlib import Path
import os
import glob
import re

def regex_search(folder_path, regex):
    '''Given a path to a folder, opens all .txt files in a folder and
    searches for any line that matches a user-supplied regular
    expression. Returns all lines that contain the given regular
    expression.

    Args:
      folder_path (str): Path to a folder in the file system
      regex (str): Regular expression (as a string)

    Returns:
      list: List of all lines containing the regular expression

    '''
    # Search each text file in the given folder
    for text_file in glob.glob(f"{folder_path}**/*.txt", recursive=True):
        with open(text_file) as f:
            # Read the file lines and search for the regex
            for i, line in enumerate(f.readlines()):
                if regex.search(line):
                    # Yield instead of return for format of returned lines
                    yield line.rstrip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='Folder to search for .txt files')
    parser.add_argument('regex', help='Regular expression to search for')

    args = parser.parse_args()

    # Compile given regex
    regex = args.regex
    rgx = re.compile(regex)
    
    # Create path to directory and check validity 
    folder_path = Path(args.folder)
    if not os.path.isdir(folder_path):
        print("You did not pass in a valid directory")

    for line in regex_search(folder_path, rgx):
        print(line)

if __name__=='__main__':
    main()
