import copy 

current_player = 'X'
next_player = 'O'
selection = 0
winner = ''

gameboard = [
  ['-','-','-'],
  ['-','-','-'],
  ['-','-','-']
]

def showBoard():
  print("Board:         Inputs: ")
  for i in range (3):
    for j in range(3):
      print(gameboard[i][j],"  ", end = '')
      if j==2:
        if i == 0:
          print("      0 | 1 | 2")
        elif i==1:
          print("      3 | 4 | 5")
        else:
          print("      6 | 7 | 8")
        print ('\n')
  
def checkValid(selection):
  valid = False
  if selection<=2 and selection>=0:
    if gameboard[0][selection-3] == '-':
      valid = True
  elif selection<=5 and selection>=3:
    if gameboard[1][selection-3] == '-':
      valid = True
  elif selection<=8 and selection>=6:
    if gameboard[2][selection-6] == '-':
      valid = True

  return valid


def yourTurn(player):
  print("your turn to play, ", current_player)
  selection = int(input("Choose a position from 0 to 8: "))
  while selection > 8 or selection <0:
    selection = int(input("That's an invalid input, please choose a position from 0 to 8: "))
  isValid = checkValid(selection)

  while isValid == False:
    selection = int(input(("Someone already played there, pick somewhere else (0-8): ")))
    isValid = checkValid(selection)
  else:
    print('\n')
    return selection

def insertSelection(selection):
  if selection<=2 and selection>=0:
    gameboard[0][selection] = current_player
  elif selection<=5 and selection>=3:
    gameboard[1][selection-3] = current_player
  elif selection<=8 and selection>=6:
    gameboard[2][selection-6] = current_player

def checkTie():
  tie = True
  for i in range (3):
    for j in range(3):
      if gameboard[i][j] != 'X' and gameboard[i][j] != 'O':
        tie = False
        return tie
  return tie


def checkRows():
  row1same = gameboard[0][0] == gameboard[0][1] == gameboard[0][2] != "-"
  row2same = gameboard[1][0] == gameboard[1][1] == gameboard[1][2] != "-"
  row3same = gameboard[2][0] == gameboard[2][1] == gameboard[2][2] != "-"
  
  global winner
  if row1same == True:
    winner = gameboard[0][0]
    return True

  elif row2same == True: 
    winner = gameboard[1][0]
    return True

  elif row3same == True: 
    winner = gameboard[2][0]
    return True

  return False


def checkColumns():
  col1same = gameboard[0][0] == gameboard[1][0] == gameboard[2][0] != "-"
  col2same = gameboard[0][1] == gameboard[1][1] == gameboard[2][1] != "-"
  col3same = gameboard[0][2] == gameboard[1][2] == gameboard[2][2] != "-"
  
  global winner
  if col1same == True:
    winner = gameboard[0][0]
    return True

  elif col2same == True: 
    winner = gameboard[0][1]
    return True

  elif col3same == True: 
    winner = gameboard[0][2]
    return True

  return False


def checkDiags():
  diag1same = gameboard[0][0] == gameboard[1][1] == gameboard[2][2] != "-"
  diag2same = gameboard[0][2] == gameboard[1][1] == gameboard[2][0] != "-"
  
  global winner
  if diag1same == True:
    winner = gameboard[0][0]
    return True

  elif diag2same == True: 
    winner = gameboard[0][2]
    return True


  return False


def checkGameOver():
  checkRows()
  checkColumns()
  checkDiags()
  if checkRows() == True or checkColumns() == True or checkDiags() == True:
    return True
  else:
    return False





while True:
  showBoard()
  selection = yourTurn(current_player)
  insertSelection(selection)

  gameOver = checkGameOver()
  if gameOver == True:
    showBoard()
    print("The game has ended,", winner, "has won!")
    break

  tie = checkTie()
  if tie == True:
    showBoard()
    print("The game has ended in a tie, thanks for playing :)")
    break
  temp = copy.deepcopy(current_player)
  current_player = copy.deepcopy(next_player)
  next_player = copy.deepcopy(temp)

