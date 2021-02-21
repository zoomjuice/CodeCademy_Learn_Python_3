"""
All files with a list of different values are CSV files; they can use different delimiters (like a comma or tab) to
 indicate where the different values start and stop. For instance, if the data uses commas, a semicolon might be used to
 separate the values.

We can indicate the delimiter used in our data by passing the 'delimiter="<character>"' argument to csv.DictReader.
"""

import csv

isbn_list = []

with open('books.csv', newline='') as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter='@')
    for item in books_reader:
        isbn_list.append(item['ISBN'])

print(isbn_list)

"""
books.csv

Author@ISBN@Title
Lauren Murray@978-0-12-995015-8@"Enviornment Call, Amount Later Page Country"
Micheal Jones@978-1-78110-100-1@Rate Security Full
Alexander Carr@978-0-315-25137-3@Still Response Size
Michael Williams@978-0-388-70665-7@Position Result Five
Kathleen Ferguson@978-1-75098-721-6@Country Week Receive And Sign
Sarah Dorsey@978-1-06-483628-6@Audience Truth Small
Mary Middleton@978-0-7419-8114-1@Travel: Special Offer Near Allow Goal
William Todd@978-1-4457-0480-7@Money Exactly Drop Teach
Joan Martin@978-0-657-61030-2@Theory Do Half Change
Gary Roman@978-1-5039-7539-2@Bill Serve Pull Industry South Job
"""
