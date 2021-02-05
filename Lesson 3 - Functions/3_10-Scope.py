current_year = 2048 # current_year can be used inside functions, its scope is global


def calculate_age(birth_year):
    age = current_year - birth_year # age and birth_year cannot be access outside the scope of the function
    return age


print(calculate_age(1970))
