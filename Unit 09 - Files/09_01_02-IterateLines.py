"""
When we read a file, we might want to grab the whole document in a single string, like .read() would return. But what
 if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line by line
 instead of having the whole thing.

with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)

The above script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt. It then
 iterates over each line in the document and prints the entire file out.

Note: The .readlines() method generates a list of lines. Omitting it in a for loop causes the loop to iterate over each
 line individually, then discards it when it's done.
"""

with open('how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)

"""
how_many_lines.txt

1. How many lines do we write on the daily,
2. Many money, we write many many many
3. How many lines do you write on the daily,
4. Say you say many money, you write many many many
"""
