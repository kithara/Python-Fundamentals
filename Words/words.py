#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:
    python words.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of wrods from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of string containing the wrods from the document.
    
    """
    try:
        with urlopen(url) as story:
            story_words = []
            for line in story:
                line_words = line.decode('utf-8').split()
                for word in line_words:
                    story_words.append(word)
        return story_words
    except IOError:
        print ("I experienced an exception. Check the url: '{url}'".format(url=url))
        raise



def print_items(items):
    """Print a list of items

    Args:
        An iterable list of printable items

    Returns:
        None

    """
    dic = dict()

    for item in items:
        if item not in dic:
            dic[item]=1
        else:
            dic[item] +=1

    for dic_item in dic:
        print("word = {0} | count = {1}".format(dic_item, dic[dic_item]))
# 'http://sixty-north.com/c/t.txt' 


def main(url):
    """Main program from command line

    Args:
        URL
    """
    print ("your are fetching words from ", url)
    words = fetch_words(url)
    print_items(words)


print(__name__)


if __name__ == "__main__":
    url = sys.argv[1] 
    # print(url)
    main(url)

