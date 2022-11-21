#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""

def playerChoice():
  '''
  No input parameters needed.
  Function should ask the players to make their choice.  How you ask is unimportant, but the
  output must be consistent:
  0: rock
  1: paper
  2: scissors
  '''
  x = input("Enter a choice: ").strip()
  if x == "0" or x == "rock": y = 0
  elif x == "1" or x == "paper": y=  1
  elif x == "2" or x == "scissors": y= 2
  else: y= "invalid input"
  return y




if __name__ == "__main__":
  player = playerChoice()
  print(player)
