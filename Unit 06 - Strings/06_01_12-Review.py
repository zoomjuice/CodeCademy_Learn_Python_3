"""
Create a function called username_generator take two inputs, first_name and last_name and returns a username. The
 username should be a slice of the first three letters of the first name and the first four letters of the last name.
 If the first name is less than three letters or the last name is less than four letters it should use the entire name.
 For example, if the employee's name is Abe Simpson the function should generate the username AbeSimp.
"""


def username_generator(first_name, last_name):
    return first_name[:3] + last_name[:4]


user = username_generator('Abraham', 'Simpson')
print(user)

"""
Create a function password_generator that takes one input, username and returns the string with the letters shifted
 by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the
 username is AbeSimp, then the temporary password generated should be pAbeSim.
"""


def password_generator(username):
    return username[-1] + username[0:-1]


password = password_generator(user)
print(password)
