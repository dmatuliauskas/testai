import random
import time

print("Player, please choose Heads or Tails by entering 1 or 2. ")
Choice = input("Your choice is: ")
print("Tossing a coin...")
time.sleep(2)
print("The coin flips in the air...")
time.sleep(2)
print("The coin fell on the ground...")

HeadsTails = [1,2]
pickHeadsTails = random.choice(HeadsTails)
if pickHeadsTails == 1:
    print("It's Heads")
if pickHeadsTails == 2:
    print("It's Tails")
time.sleep(2)
if Choice == pickHeadsTails:
  print("You won!")
else:
  print("You lose.")