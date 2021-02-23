"""
Now you know all about files! You were able to:

    Open up file objects using open() and with.
    Read a file's full contents using Python's .read() method.
    Read a file line-by-line using .readline() and .readlines()
    Create new files by opening them in write-mode.
    Append to a file non-destructively by opening a file in append-mode.
    Apply all of the above to different types of data-carrying files including CSV and JSON!

You have all the skills necessary to read, write, and update files programmatically, a very useful skill in Python!
"""

with open('file.txt') as file_object:
    print(file_object.read())

"""
file.txt

Thank you for learning about files in Python with us!
"""
