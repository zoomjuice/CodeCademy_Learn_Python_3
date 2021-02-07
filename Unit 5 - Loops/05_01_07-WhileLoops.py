all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:  # A while loop repeats until its condition is False
    students_in_poetry.append(all_students.pop())  # list.pop() removes the last element of a list and returns it

print(students_in_poetry)
