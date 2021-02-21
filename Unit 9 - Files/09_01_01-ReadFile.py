"""
with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)

This opens a file object called cool_doc and creates a new indented block where you can read the contents of the opened
 file. We then read the contents of the file cool_doc using cool_doc.read() and save the resulting string into the
  variable cool_contents. Then we print cool_contents, which outputs the content of the file.
"""

with open('welcome.txt') as text_file:
    text_data = text_file.read()

print(text_data)

"""
welcome.txt

Congratulations on reading your first file at codecademy.com!
"""
