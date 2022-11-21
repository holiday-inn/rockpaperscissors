#!python3
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""
from random import *
def computerChoice():
  x = randint(0,2)
  if x == 0: t = 0
  elif x == 1: t = 1
  elif x == 2: t=2
  return t



if __name__ == "__main__":
  computer = computerChoice()
  print(computer)
