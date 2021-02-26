"""
The open() function that is used to open a file to read needs another argument, w, to open a file to write to.

with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")

Pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is 'r' and
 passing 'r' to open() opens the file in read-mode as we've been doing.

A created file will be placed in the script's directory. If a file with the same name exists, it will be overwritten.
"""

with open('bad_bands.txt', 'w') as bad_bands_doc:
    bad_bands_doc.write('Foo')
