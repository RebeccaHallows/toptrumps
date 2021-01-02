import random
import requests

computer_score = 0
user_score = 0

print("\nLets play top trumps! Player 1 will go first.")

for game in range (5):
   # Player 1 card randomly generated
   random_number_player1 = random.randint(1, 83)
   url = 'https://swapi.dev/api/people/{}/'.format(random_number_player1)
   response = requests.get(url)
   character_player1 = response.json()

   # Computer card randomly generated
   random_number_computer = random.randint(1, 83)
   url = 'https://swapi.dev/api/people/{}/'.format(random_number_computer)
   response = requests.get(url)
   character_computer = response.json()

# Player 1 starts the game.
   if character_player1['height'] == 'unknown':
       character_player1['height'] = '0'
   if character_player1['mass'] == 'unknown':
       character_player1['mass'] = '0'
   if character_player1['films'] == 'unknown':
       character_player1['films'] = '0'
   if character_player1['vehicles'] == 'unknown':
       character_player1['vehicles'] = '0'

   if character_computer['height'] == 'unknown':
       character_computer['height'] = '0'
   if character_computer['mass'] == 'unknown':
       character_computer['mass'] = '0'
   if character_computer['films'] == 'unknown':
       character_computer['films'] = '0'
   if character_computer['vehicles'] == 'unknown':
       character_computer['vehicles'] = '0'

   print('\nYou have drawn {}! \n Height: {} \n Mass: {} \n Number of Films: {} \n Number of Vehicles: {} '.format(character_player1['name'],character_player1['height'],character_player1['mass'], len(character_player1['films']),len(character_player1['vehicles'])))
   category_player1 = input('\nWhat category would you like to challenge, height, mass, films or vehicles? ')
   print('\nYour opponent drew {}!\n Height: {} \n Mass: {} \n Number of Films: {} \n Number of Vehicles: {} '.format(character_computer['name'], character_computer['height'], character_computer['mass'],len(character_computer['films']), len(character_computer['vehicles'])))

   if category_player1 == 'height':
       # Condition 1: player 1 card greater than computer card
       if int(character_player1['{}'.format(category_player1)]) > int(
               character_computer['{}'.format(category_player1)]):
           print('You chose {}, this is greater than your opponents card, you win!'.format(category_player1))
           user_point = 1
           computer_point = 0
       # Condition 2: player 1 card lower than computer card
       if int(character_player1['{}'.format(category_player1)]) < int(
               character_computer['{}'.format(category_player1)]):
           print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(category_player1))
           user_point = 0
           computer_point = 1
       # Condition 3: cards are the same, choose alternate category
       if int(character_player1['{}'.format(category_player1)]) == int(
               character_computer['{}'.format(category_player1)]):
           print('The cards are the same! Choose a different category.')
           category_player1_replacement = input(
               'What category would you like to challenge, height, mass, films or vehicles? ')
           if category_player1_replacement == 'height':
               if int(character_player1['{}'.format(category_player1_replacement)]) > int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(character_player1['{}'.format(category_player1_replacement)]) < int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'mass':
               if int(character_player1['{}'.format(category_player1_replacement)]) > int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(character_player1['{}'.format(category_player1_replacement)]) < int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'films':
               if int(len(character_player1['{}'.format(category_player1_replacement)])) > int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(len(character_player1['{}'.format(category_player1_replacement)])) < int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'vehicles':
               if int(len(character_player1['{}'.format(category_player1_replacement)])) > int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(len(character_player1['{}'.format(category_player1_replacement)])) < int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1

   if category_player1 == 'mass':
       # Condition 1: player 1 card greater than computer card
       if int(character_player1['{}'.format(category_player1)]) > int(
               character_computer['{}'.format(category_player1)]):
           print('\nYou chose {}, this is greater than your opponents card, you win!'.format(category_player1))
           user_point = 1
           computer_point = 0
       # Condition 2: player 1 card lower than computer card
       if int(character_player1['{}'.format(category_player1)]) < int(
               character_computer['{}'.format(category_player1)]):
           print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(category_player1))
           user_point = 0
           computer_point = 1
       # Condition 3: cards are the same, choose alternate category
       if int(character_player1['{}'.format(category_player1)]) == int(
               character_computer['{}'.format(category_player1)]):
           print('The cards are the same! Choose a different category.')
           category_player1_replacement = input(
               'What category would you like to challenge, height, mass, films or vehicles? ')
           if category_player1_replacement == 'height':
               if int(character_player1['{}'.format(category_player1_replacement)]) > int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(character_player1['{}'.format(category_player1_replacement)]) < int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'mass':
               if int(character_player1['{}'.format(category_player1_replacement)]) > int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(character_player1['{}'.format(category_player1_replacement)]) < int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'films':
               if int(len(character_player1['{}'.format(category_player1_replacement)])) > int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(len(character_player1['{}'.format(category_player1_replacement)])) < int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'vehicles':
               if int(len(character_player1['{}'.format(category_player1_replacement)])) > int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(len(character_player1['{}'.format(category_player1_replacement)])) < int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1

   if category_player1 == 'films':
       # Condition 1: player 1 card greater than computer card
       if int(len(character_player1['{}'.format(category_player1)])) > int(
               len(character_computer['{}'.format(category_player1)])):
           print('\nYou chose {}, this is greater than your opponents card, you win!'.format(category_player1))
           user_point = 1
           computer_point = 0
       # Condition 2: player 1 card lower than computer card
       if int(len(character_player1['{}'.format(category_player1)])) < int(
               len(character_computer['{}'.format(category_player1)])):
           print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(category_player1))
           user_point = 0
           computer_point = 1
       # Condition 3: cards are the same, choose alternate category
       if int(len(character_player1['{}'.format(category_player1)])) == int(
               len(character_computer['{}'.format(category_player1)])):
           print('The cards are the same! Choose a different category.')
           category_player1_replacement = input(
               'What category would you like to challenge, height, mass, films or vehicles? ')
           if category_player1_replacement == 'height':
               if int(character_player1['{}'.format(category_player1_replacement)]) > int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(character_player1['{}'.format(category_player1_replacement)]) < int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'mass':
               if int(character_player1['{}'.format(category_player1_replacement)]) > int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(character_player1['{}'.format(category_player1_replacement)]) < int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'films':
               if int(len(character_player1['{}'.format(category_player1_replacement)])) > int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(len(character_player1['{}'.format(category_player1_replacement)])) < int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'vehicles':
               if int(len(character_player1['{}'.format(category_player1_replacement)])) > int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(len(character_player1['{}'.format(category_player1_replacement)])) < int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1

   if category_player1 == 'vehicles':
       # Condition 1: player 1 card greater than computer card
       if int(len(character_player1['{}'.format(category_player1)])) > int(
               len(character_computer['{}'.format(category_player1)])):
           print('\nYou chose {}, this is greater than your opponents card, you win!'.format(category_player1))
           user_point = 1
           computer_point = 0
       # Condition 2: player 1 card lower than computer card
       if int(len(character_player1['{}'.format(category_player1)])) < int(
               len(character_computer['{}'.format(category_player1)])):
           print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(category_player1))
           user_point = 0
           computer_point = 1
       # Condition 3: cards are the same, choose alternate category
       if int(len(character_player1['{}'.format(category_player1)])) == int(
               len(character_computer['{}'.format(category_player1)])):
           print('The cards are the same! Choose a different category.')
           category_player1_replacement = input(
               'What category would you like to challenge, height, mass, films or vehicles? ')
           if category_player1_replacement == 'height':
               if int(character_player1['{}'.format(category_player1_replacement)]) > int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(character_player1['{}'.format(category_player1_replacement)]) < int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'mass':
               if int(character_player1['{}'.format(category_player1_replacement)]) > int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(character_player1['{}'.format(category_player1_replacement)]) < int(
                       character_computer['{}'.format(category_player1_replacement)]):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'films':
               if int(len(character_player1['{}'.format(category_player1_replacement)])) > int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(len(character_player1['{}'.format(category_player1_replacement)])) < int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1
           if category_player1_replacement == 'vehicles':
               if int(len(character_player1['{}'.format(category_player1_replacement)])) > int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is greater than your opponents card, you win!'.format(
                       category_player1_replacement))
                   user_point = 1
                   computer_point = 0
               if int(len(character_player1['{}'.format(category_player1_replacement)])) < int(
                       len(character_computer['{}'.format(category_player1_replacement)])):
                   print('\nYou chose {}, this is lower than your opponents card, you lose!'.format(
                       category_player1_replacement))
                   user_point = 0
                   computer_point = 1


   computer_score += computer_point
   user_score += user_point
   print('Your Score: {}'.format(user_score))
   print('Computer Score: {}'.format(computer_score))
if user_score > computer_score:
   print('\nYou won the game!')
else:
   print('\nSorry, you lose the game!')