# refactor version - T5, 18/07/24

# Sorting hat decides which of four Hourses each freshman student goes to:
# 🦁 Gryffindor ❤️‍🔥
# 🐍 Slytherin 💚
# 🦅 Ravenclaw 💙
# 🦡 Hufflepuff 💛
# Program that asks user some question using int() and places them into one of the Houses based on their answers.
# If answer = 1, Gryffindor & Ravenclaw both get a +1.
# Else if answer = 2, Hufflepuff & Slytherin both get a +1.abs
# Else, output message "Wrong input" 

Gryffindor = Slytherin = Ravenclaw = Hufflepuff = 0


print("""                                
Oh you may not think I am pretty, but do not judge on what you see, I will eat myself if you can find a smarter hat than me.
                                 
I am the magical sorting hat 🪄🧙 and I will decide your fate or the house you belong in!
                                
To get sorted in a house, you need to answer some question...
                                
 Q1) Do you like Dawn or Dusk?'
     1) Dawn'
     2) Dusk'""")

answer = int(input('Your answer (1-2):    '))

match answer:
    case 1:
        Gryffindor += 1
        Ravenclaw += 1
    case 2: 
        Slytherin += 1
        Hufflepuff += 1
    case _:
        print("Error.")

print("\nQ2) When I'm dead, I want people to remember me as:")
print("     1) The Good"),
print("     2) The Great"),
print("     3) The Wise"),
print("     4) The Bold"),

answer = int(input("Your answer (1-4):    "))
match answer: 
    case 1: Hufflepuff +=1
    case 2: Slytherin +=1
    case 3: Ravenclaw +=1
    case 4: Gryffindor +=1
    case _: print('Wrong input.')

print("\nQ3) Which kind of instrument most pleases your ear?"),
print("     1) The violin"),
print("     2) The trumpet"),
print("     3) The piano"),
print("     4) The drum"),

answer = int(input("Your answer (1-4):    "))
match answer: 
    case 1: Slytherin +=1
    case 2: Hufflepuff +=1
    case 3: Ravenclaw +=1
    case 4: Gryffindor +=1
    case _: print('Wrong input.')

print('All done! Now, I will work my magical power to decide which house you belong in...')
print('                     ')


ready = int(input('Are you ready to know which house you belong in? 1) Yes      2) No  '))
if ready == 1:
    print('Drum rolls 🥁🥁🥁....')
elif ready == 2:
    print('Aw, you have nothing to worry about! Wait until you are ready again...🪄')
else: 
    print('Please try again, my magic cannot understand what you say...🧙')

print(Gryffindor)
print(Slytherin)
print(Ravenclaw)
print(Hufflepuff)

if Gryffindor >= 2 and Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
    print('GRYFFINDOR!🦁 You belong in the house of the bold Godric Gryffindor for your courage and boldness!')
elif Slytherin >= 2 and Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
    print('SLYTHERIN!🐍💚 You belong in the house of the great Salazar Slytherin for your ambition and cunning qualities!')
elif Ravenclaw >= 2 and Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print('RAVENCLAW!🦅💙 You belong in the house of the wise Rowena Ravenclaw for your intelligence and wit!')
elif Hufflepuff >= 2 and Hufflepuff > Gryffindor and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
    print('HUFFLEPUFF!🦡💛 You belong in the house of the good Helga Hufflepuff for your loyalty and patience!')
else:
    print('Hmmm... Difficult, very difficult... You are too difficult. Maybe you are better as a Muggle...')


# other = input('Your answer: ')
#if other == 'Gryffindor':
    #print('GRYFFINDOR!🦁❤️‍🔥 You belong in the house of the bold Godric Gryffindor for your courage and boldness!')
#elif other == 'Slytherin':
    #print('SLYTHERIN!🐍💚 You belong in the house of the great Salazar Slytherin for your ambition and cunning qualities!')
#elif other == 'Ravenclaw':
    #print('RAVENCLAW!🦅💙 You belong in the house of the bold Rowena Ravenclaw for your intelligence and wit') 
#elif other == 'Hufflepuff':
    #print('HUFFLEPUFF!🦡💛 You belong in the house of the good Helga Hufflepuff for your loyalty and patience!')
#else:
    #print('You are too difficult. Maybe you are better as a Muggle...')





