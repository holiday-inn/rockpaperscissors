#!python3

'''
Create a function that takes 2 input parameters:
int: computer choice
int: player choice

the choices correspond to:
0: rock
1: paper
2: scissors

Based on the classic rules for Rock Paper Scissors, the return value should be an integer value that indicates if the player is the wins, loses or ties
Output:
-1: player loses
0: tie
1: player wins
'''

def playerWins(computer,player):
  
  if computer == player: 
    i = 0
  elif computer == 0 and player == 1: 
    i = 1
  elif computer == 1 and player == 2: 
    i = 1
  elif computer == 2 and player == 0: 
    i = 1
  elif computer == 0 and player == 2:
     i = -1
  elif computer == 1 and player == 0: 
    i = -1
  elif computer == 2 and player == 1: 
    i = -1
  else: i = print("Invalid")
  
  return i
print(playerWins(1,2))
if __name__ == "__main__":
  assert playerWins(1,1) == 0
  assert playerWins(1,0) == -1
  assert playerWins(1,2) == 1
  assert playerWins(2,1) == -1
  
