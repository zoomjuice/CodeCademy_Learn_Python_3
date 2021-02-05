import random

# These are the possible answers a user can receive
answer_pool = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.",
               "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.",
               "Very doubtful."]

# Collect input from user
name = input("Please tell me your name: ")
question = input("What is your question? Yes or no questions only, please!: ")

# Pick a random answer to give to the user
random_number = random.randint(0, len(answer_pool) - 1)

# Tell the user the the answer their question
if question == "":
    print("I'm sorry, it appears you forgot to ask a question. Please try again.")
elif name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer_pool[random_number])
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer_pool[random_number])
