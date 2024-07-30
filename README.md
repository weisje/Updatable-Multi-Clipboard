# Updatable-Multi-Clipboard
Script that saves the content of the clipboard under a keyword that can be retrieved later via previous keyword

# Project Description
The program will save each piece of clipboard text under a keyword.
For example, when you run py mcb.pyw save spam, the current contents of the
clipboard will be saved with the keyword spam. This text can later be loaded
to the clipboard again by running py mcb.pyw spam. And if the user forgets
what keywords they have, they can run py mcb.pyw list to copy a list of all
keywords to the clipboard.

# Project Requirements
1. The command line argument for the keyword is checked.
2. If the argument is save, then the clipboard contents are saved to
the keyword.
3. If the argument is list, then all the keywords are copied to the clipboard.
4. Otherwise, the text for the keyword is copied to the clipboard.

The code will need to do the following:
1. Read the command line arguments from sys.argv.
2. Read and write to the clipboard.
3. Save and load to a shelf file.

# Source
Chapter 9 "Project: Updatable Multi-Clipboard" from Al Sweigart's "Automate the Boring Stuff 2nd Edition"