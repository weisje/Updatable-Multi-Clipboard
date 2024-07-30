#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <KEYWORD> - Saves clipboard to keyword.
#        py.exe mcb.pyw <KEYWORD> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip
import shelve
import sys


def main():
    mcbShelf = shelve.open('mcb')

    # TODO: Save clipboard content

    # TODO: List keywords and load content

    mcbShelf.close()


if __name__ == '__main__':
    main()
