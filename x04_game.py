#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import playerChoice
from x02_computer import computerChoice 
from x03_winner import playerWins 
print("Enter a Pick in Rock Paper Scissors\n0 for rock\n1 for paper\n2 for scissors")
y = playerChoice()
t = computerChoice()
if t == 0:
  print("opponent chose Rock.")
elif t == 1:
  print("opponent chose Paper")
elif t == 2:
  print("opponent chose Scissors")
else:
  print("oh no, an error")

if playerWins(t,y) == -1:
  print("You lost")
elif playerWins(t,y) == 1:
  print("You Won")
elif playerWins(t,y) == 0:
  print("Draw")



if __name__ == "__main__":
  pass

