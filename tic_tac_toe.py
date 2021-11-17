# ++++++ TIC TAC TOE ++++++

board = [' ',' ',' ', 
         ' ',' ',' ',
         ' ',' ',' ']
game_going = True
player_turn  = 'X'
winner = None

def display_board():  #  displays board
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print('---------')
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print('---------')
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])



def play_game():  #  runs the main functions
  display_board()
  while game_going:
    handle_turn(player_turn)
    flip_player()
    game_over()
    
  

def win_game():
  check_rows()
  check_diagonal()
  check_columns()
  

def check_rows():
  row1 = board[0] == board[1] == board[2] != ' '
  row2 = board[3] == board[4] == board[5] != ' '
  row3 = board[6] == board[7] == board[8] != ' '
  global game_going
  if row1 or row2 or row3:
    game_going = False

  
  if row1:
    print(board[0] + ' won')
  elif row2:
    print(board[4] + ' won')
  elif row3:
    print(board[7] + ' won')

  
  




def check_columns():
  col1 = board[0] == board[3] == board[6] != ' '
  col2 = board[1] == board[4] == board[7] != ' '
  col3 = board[2] == board[5] == board[8] != ' '
  global game_going
  if col1 or col2 or col3:
    game_going = False


  if col1:
    print(board[0] + ' won')
  elif col2:
    print(board[1] + ' won')
  elif col3:
    print(board[2] + ' won')

  



def check_diagonal():
  dia1 = board[0] == board[4] == board[8] != ' '
  dia2 = board[2] == board[4] == board[6] != ' '
  global game_going
  if dia1 or dia2:
    game_going = False

  
  if dia1:
    print(board[0] + ' won')
  elif dia2:
    print(board[2] + ' won')
  

 

def handle_turn(player):
  global player_turn
  print("It's " + player_turn + "'s" + " turn")
  location = input('Enter number between 1 and 9: ')
  
  valid = False
  while valid == False:
    
    while location not in['1','2','3','4','5','6','7','8','9']:
        location = input('Enter number between 1 and 9: ')

    location = int(location) -1
  

    if board[location] == ' ':
      valid = True
    else:
      print('You cant go here again!')

  board[location] = player 
  print('\n')
  display_board()

  

def flip_player():  #  switches players , starting with X 
  global game_going
  global player_turn

  if player_turn == 'X':
    player_turn = 'O'
  
  elif player_turn == 'O':
    player_turn = 'X'


def is_draw():
  global game_going
  global player_turn

  if ' ' not in board:  #     if full board then == draw
    print('No Winner!')
    game_going = False
 

  


def game_over():
  global game_going
  global player_turn
  win_game()
  is_draw()
  
play_game()
  
