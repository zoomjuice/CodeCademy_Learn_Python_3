import random

# These are the possible answers a user can receive
answer_1 = "Yes - definitely."
answer_2 = "It is decidedly so."
answer_3 = "Without a doubt."
answer_4 = "Reply hazy, try again."
answer_5 = "Ask again later."
answer_6 = "Better not tell you now."
answer_7 = "My sources say no."
answer_8 = "Outlook not so good."
answer_9 = "Very doubtful."
answer_given = ""

# Collect input from user
name = input("Please tell me your name: ")
question = input("What is your question? Yes or no questions only, please!: ")

# Pick a random answer to give to the user
random_number = random.randint(1, 9)

if random_number == 1:
    answer_given = answer_1
elif random_number == 2:
    answer_given = answer_2
elif random_number == 3:
    answer_given = answer_3
elif random_number == 4:
    answer_given = answer_4
elif random_number == 5:
    answer_given = answer_5
elif random_number == 6:
    answer_given = answer_6
elif random_number == 7:
    answer_given = answer_7
elif random_number == 8:
    answer_given = answer_8
elif random_number == 9:
    answer_given = answer_9
else:
    answer_given = "Error"
    print("How did this even happen?")

# Tell the user the answer their question
if question == "":
    print("I'm sorry, it appears you forgot to ask a question. Please try again.")
elif name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer_given)
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer_given)
