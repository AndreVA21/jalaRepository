"""
demostracion elif
"""
import random
roll = random.randint(1, 6)
print(roll)
guess = int(input("Guess the dice roll:\n"))
if guess == roll:
   print('Correct!')
else:
   print('Wrong!')