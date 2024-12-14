
import random

print("I am Mrs. Clark and I am here to give you a psychology practice question 🔮. No matter what you say, you shall be given a question. You better know how to answer them 😈👿😈.");
question = input('Are you ready 💌🌷: ')

# magic8ball = random.randstring("Yes - definitely", "It is decidedly so", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful.")

random_number = random.randint(1,62)

if random_number==1:
    answer = 'Explain the use of one research method in one study using the biological approach to understanding human behavior.'
elif random_number == 2:
    answer = 'Explain the use of one research method in one study of the brain and behavior.'
elif random_number == 3:
    answer = 'Explain the use of one research method in one study of hormones or pheromones and behavior.'
elif random_number == 4:
    answer = 'Explain the use of one research method in one study of genetics and behavior.'
elif random_number == 5:
    answer = 'Explain one ethical consideration relevant to one study using a biological approach to understanding human behavior.'
elif random_number == 6:
    answer = 'Explain one ethical consideration relevant to one study of the brain and behavior.'
elif random_number == 7:
    answer = 'Explain one ethical consideration relevant to one study of hormones or pheromones and behavior.'
elif random_number == 8:
    answer = 'Explain one ethical consideration relevant to one study of genetics and behavior.'
elif random_number == 9:
    answer = 'Explain one technique used to study the brain in relation to behavior.'
elif random_number == 10:
    answer = 'Explain one study of localization of function.'
elif random_number == 11:
    answer = 'Explain one study of neuroplasticity.'
elif random_number == 12:
    answer = 'Discuss neurotransmitters and their effect on behavior.'
elif random_number == 13:
    answer = 'Explain one effect of neurotransmission in human behavior, making use of one study.'
elif random_number == 14:
    answer = 'Explain the formation of neural networks using one study.'
elif random_number == 15:
    answer = 'Explain the role of one agonist, making use of one study.'
elif random_number == 16:
    answer = 'Explain the role of one antagonist, making use of one study.'
elif random_number == 17:
    answer = 'Explain neural pruning, making use of one study.'
elif random_number == 18:
    answer = 'Explain how excitatory or inhibitory synapses (neurotransmitters) play a role in one behavior, making use of one study.'
elif random_number == 19:
    answer = 'Explain the role of one hormone in human behavior, making use of one study.'
elif random_number == 20:
    answer = 'Explain one study of the role of pheromones in human behaviour.'
elif random_number == 21:
    answer = 'Explain the role of one gene in human behaviour.'
elif random_number == 22:
    answer = 'Explain one evolutionary explanation of one behaviour.'
elif random_number == 23:
    answer = 'Explain the use of twin studies and/or kinship studies using one study.'
elif random_number == 24:
    answer = 'Explain the use of one research method in one study used in the study of the individual and the group.'
elif random_number == 25:
    answer = 'Explain one ethical consideration relevant to one study of cultural influences on behavior or cognition.'
elif random_number == 26:
    answer = 'Discuss the use of one research method in the sociocultural approach in the study of the role of culture in the origins of behavior or cognition.'
elif random_number == 27:
    answer = 'Discuss ethical considerations relevant to the study of the individual and the group.'
elif random_number == 28:
    answer = 'Explain Social Identity Theory, making use of one study.'
elif random_number == 29:
    answer = 'Explain one study of Social Identity Theory.'
elif random_number == 30:
    answer = 'Explain Social Cognitive Theory, making use of one study.'
elif random_number == 31:
    answer = 'Explain one theory of stereotypes, making use of one study.'
elif random_number == 32:
    answer = 'Explain one study of stereotypes.'
elif random_number == 33:
    answer = 'Explain one study that shows one effect of stereotypes on behavior.'
elif random_number == 34:
    answer = 'Describe one study of social groups. (best to approach this with a study of SIT)'
elif random_number == 35:
    answer = 'Explain one cultural dimension.'
elif random_number == 36:
    answer = 'Explain one study of one cultural dimension.'
elif random_number == 37:
    answer = 'Describe one study of cultural groups. (Same question as one study of one effect of culture on behavior or cognition)'
elif random_number == 38:
    answer = 'Explain one study of one effect of culture on behavior or cognition.'
elif random_number == 39:
    answer = 'Explain one study of enculturation.'
elif random_number == 40:
    answer = 'Explain one study of acculturation.'
elif random_number == 41:
    answer = 'Explain one study of assimilation.'
elif random_number == 42:
    answer = 'Explain the use of one research method in one study of cognitive processes.'
elif random_number == 43:
    answer = 'Explain the use of one research method in one study of emotion and cognition.'
elif random_number == 44:
    answer = 'Explain one ethical consideration relevant to one study of the reliability of cognitive processes.'
elif random_number == 45:
    answer = 'Explain one study related to schema theory'
elif random_number == 46:
    answer = 'Explain one model of memory.'
elif random_number == 47:
    answer = 'Explain the working memory model with reference to one study.'
elif random_number == 48:
    answer = 'Explain the multi-store model with reference to one study.'
elif random_number == 49:
    answer = 'Explain one study that supports one model of memory.'
elif random_number == 50:
    answer = 'Explain one study of thinking and decision making.'
elif random_number == 51:
    answer = 'Explain one study of rational and/or intuitive thinking.'
elif random_number == 52:
    answer = 'Explain one study of reconstructive memory.'
elif random_number == 53:
    answer = 'Explain one study of one cognitive bias.'
elif random_number == 54:
    answer = 'Explain one theory of how emotion may affect one cognitive process, using one study.'
elif random_number == 55:
    answer = 'Explain Flash Bulb Memory.'
elif random_number == 56:
    answer = 'Discuss a biological approach to understanding one health problem.'
elif random_number == 57:
    answer = 'Discuss a cognitive approach to understanding one health problem.'
elif random_number == 58:
    answer = 'Discuss a sociocultural approach to understanding one health problem.'
elif random_number == 59:
    answer = 'Discuss ethical considerations in the study of one health problem.'
elif random_number == 60:
    answer = 'Discuss one or more research methods in the study of one health problem.'
elif random_number == 61:
    answer = 'Discuss one explanation of one health problem.'
elif random_number == 62:
    answer = 'Discuss prevalence of rates of health problems.'
else: 
    answer = 'Error. Please input a number from 1 to 9.'


print('Mrs.Clark🔮:    ' + answer)