#!/usr/bin/env python3
''' Link Verification

Author: <your name>
'''
import argparse
import requests
import re

def verify_links(url):
    '''Given a URL of a web page, attempt to download every linked
    page on the page. Flage any pages that have a 404 "Not Found"
    status code and print them out as broken links.

    Args:
      url (str): URL to crawl and verify

    Returns:
      None

    '''
    
    # Get the url passed as an arguement and find all the urls
    res = requests.get(url)
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', res.text)
    
    # Test each link in urls to see if broken
    for link in urls:
        res = requests.get(link)
        if res.status_code != requests.codes.ok:
            # Flag as broken
            print('{} is a broken link. Response: 404 Not Found.'.format(link))

def main():
    ''' Main function '''

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL to verify links')

    args = parser.parse_args()

    # Run verify_links function with url given as an arguement
    verify_links(args.url)

if __name__=='__main__':
    main()
