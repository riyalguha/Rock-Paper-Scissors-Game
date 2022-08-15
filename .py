rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
rand=[rock,paper,scissors]
com=random.choice(rand)
if user=='0':
  print(rock)
  if com==rock:
    print(com)
    print("Its a draw")
  elif com==paper:
    print(com)
    print("You Lose")
  else:
    print(com)
    print("You Win")
if user=='1':
  print(paper)
  if com==paper:
    print(com)
    print("Its a draw")
  elif com==rock:
    print(com)
    print("You Win")
  else:
    print(com)
    print("You Lose")
if user=='2':
  print(scissors)
  if com==scissors:
    print(com)
    print("Its a draw")
  elif com==rock:
    print(com)
    print("You Lose")
  else:
    print(com)
    print("You Win")
