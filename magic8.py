# Magic 8 Balls is a popular office toy invented in 1940s for fortune telling and advice seeking 🎱🎱🎱
# It's an oversized 8 ball with some of the following answers:
    # Yes - definitely.
    # It is decidedly so.
    # Without a doubt.
    # Reply hazy, try again.
    # Ask again later.
    # Better not tell you now.
    # My sources say no.
    # Outlook not so good.
    # Very doubtful.

# Program that respond to any Yes/No questions with a different answer each time it executes:

import random

print("I am Magic 8 Ball 🎱 and I am here to answer your questions. Yes/No questions only!!");
question = input('Question: ')

# magic8ball = random.randstring("Yes - definitely", "It is decidedly so", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful.")

random_number = random.randint(1,9)

if random_number == 1:
    answer = 'Yes - definitely.'
elif random_number == 2:
    answer = 'It is decidedly so.'
elif random_number == 3:
    answer = 'Without a doubt.'
elif random_number == 4:
    answer = 'Reply hazy, try again.'
elif random_number == 5:
    answer = 'Ask again later.'
elif random_number == 6:
    answer = 'Better not tell you now.'
elif random_number == 7:
    answer = 'My sources say no.'
elif random_number == 8:
    answer = 'Outlook not so good.'
elif random_number == 9:
    answer = 'Very doubtful.'
else: 
    answer = 'Error. Please input a number from 1 to 9.'


print('Magic 8 Ball:    ' + answer)