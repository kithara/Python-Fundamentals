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
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print a list of items

    Args:
        An iterable list of printable items

    Returns:
        None

    """
    for item in items:
        print(item)
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

