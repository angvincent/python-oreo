#         -----Rock,Paper and Scissors-----
from random import randint as rd #  rd short for randint
chars = ['Rock', 'Paper', 'Scissors']
#  ---- Generates Rock, paper, scissors ----
AI = chars[rd(0, 2)] 

player = True

while player == True:  #   infinite loop until player set to False
  player = input('Enter Rock/Paper/Scissors: ')
  if player == AI:
    print('Draw!')
  elif player == 'Rock':
    if AI == 'Paper':
      print('You loose ' + AI + ' covers ' + player)
    else:
      print('You win ' + player + ' smashes ' + AI)

  elif player == 'Paper':
    if AI == 'Scissors':
      print('You loose ' + AI + ' cuts ' + player)
    else:
      print('You win ' + player + ' covers '  + AI)
    
  
  elif player == 'Scissors':
    if AI == 'Rock':
      print('You loose ' + AI + ' smashes ' + player)
    else:
      print('You win ' + player + ' cuts ' + AI)
  
  else:
    print('Check your spelling!')

  player = True  #   setting player to True makes the loop continue 

  AI = chars[rd(0, 2)] #    genenrates new game
