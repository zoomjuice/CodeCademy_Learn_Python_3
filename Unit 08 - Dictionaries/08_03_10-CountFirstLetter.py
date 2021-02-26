"""
Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a
 dictionary where the key is a last name and the value is a list of first names. For example:

names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}

The function should return a new dictionary where each key is the first letter of a last name, and the value is the
 number of people whose last name begins with that letter. In the example above, the function would return:

{"S" : 4, "L": 3}
"""


# Write your count_first_letter function here:


def count_first_letter(names):
    letter_count_dict = {}
    for key, value in names.items():
        if key[0] not in letter_count_dict:
            letter_count_dict.update({key[0]: len(value)})
        else:
            letter_count_dict[key[0]] += len(value)
    return letter_count_dict


# Uncomment these function calls to test your  function:

# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"],
                          "Lannister": ["Jaime", "Cersei", "Tywin"]}))

# should print {"S": 7}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"],
                          "Sannister": ["Jaime", "Cersei", "Tywin"]}))
