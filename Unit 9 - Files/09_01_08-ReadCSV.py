"""
We can read CSV lines as text without a problem, but there are ways to access the data in a format better suited for
 programming purposes. In Python we can convert that data into a dictionary using the csv library’s DictReader object.

import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])

In the above code we import the csv library, which gives us the tools to parse CSV file. We then create the empty list
'list_of_email_addresses' which we’ll later populate with the addresses from our CSV. Then we open the users.csv file
with the temporary variable users_csv.

We pass the additional keyword argument newline='' to open() so we don’t accidentally mistake a line break in a data
field for a new row in our CSV (read more here: https://docs.python.org/3/library/csv.html#id3).

After opening our CSV file we use csv.DictReader(users_csv) which converts the lines of our CSV file to Python
dictionaries which we can use access methods for. The keys of the dictionary are, by default, the entries in the first
line of our CSV file. Since our CSV’s first line calls the third field in our CSV “Email“, we can use that as the
key in each row of our DictReader.

When we iterate through the rows of our user_reader object, we access all of the rows in our CSV as dictionaries (except
for the first row, which we used to label the keys of our dictionary). By accessing the 'Email' key of each of these
rows we can grab the email address in that row and append it to our list_of_email_addresses.
"""

import csv

names = []

with open('cool_csv.csv', newline='') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for item in cool_csv_dict:
        names.append(item['Cool Name'])
        print(item)

print(names)

"""
cool_csv.csv

Cool Name,Cool Birthday,Cool Fact
Trevor Torres,03-09-08,Has never been out of the country.
Crystal Ellis,17-11-06,Published a small biography on a local legend.
Devin Patrick,22-09-85,Happened across a major movie star while biking once.
Phyllis Evans,06-02-70,Once ate three packages of cookies in one sitting.
Kayla Bridges,28-07-93,Has been to over fifteen different forests.
Jeremy Lopez,12-11-02,Old job was across the street from their new job.
Meredith Barker,05-07-05,Has a dog named Peanut.
William Sanchez,22-11-88,While working a phone bank accidentally called their mother.
Linda Brown,01-02-89,Can whistle the national anthem of twelve different nations.
Elizabeth Smith,23-01-75,Is triple-jointed.
"""
