last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

subjects.append('computer science')
grades.append(100)

gradebook = list(zip(subjects, grades))

gradebook.append(('visual arts', 93))

print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)

# Convert tuples in zipped list back into lists
for i in range(len(full_gradebook)):
    full_gradebook[i] = list(full_gradebook[i])

print(full_gradebook)
