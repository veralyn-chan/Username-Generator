# Making a simple video game user/screen name generator

# List of adjectives and nouns obtained from http://www.ashley-bovan.co.uk/words/partsofspeech.html

# Format: AB
# where A is an adjective; B is a noun
# where A and B has a maximum of two syllables


# Extracting 1 & 2 syllable adjectives and combining into single list
adj1_open = open('1syllableadjectives.txt')
adj1 = adj1_open.read().split()
adj2_open = open('2syllableadjectives.txt')
adj2 = adj2_open.read().split()
adj_list = adj1 + adj2

# Extracting 1 & 2 syllable nouns and combining into single list
noun1_open = open('1syllablenouns.txt')
noun1 = noun1_open.read().split()
noun2_open = open('2syllablenouns.txt')
noun2 = noun2_open.read().split()
noun_list = noun1 + noun2

# Generating random username
from random import choice
reroll = 'y'
while reroll == 'y':
    # Picking random adjective and noun
    adj = choice(adj_list).capitalize()
    noun = choice(noun_list).capitalize()

    # Combining adj and noun to create result
    result = adj + noun
    print("Your username is: ", result)

    # Chance to reroll username
    reroll = input('Reroll username? (y/n) :')

# Goodbye message
while reroll == 'n':
    print('Thank you for using this generator! Have a nice day :D')
    break