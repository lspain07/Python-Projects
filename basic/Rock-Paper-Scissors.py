import random
choice = str(input("Rock, Paper, or Scissors? "))
comp = random.randint(1,3) #1 is rock, 2 is paper, 3 is scissors
if choice == "Rock" or "rock" and comp == 2:
  print("Paper! You lose!")
elif choice == "Rock" or "rock" and comp == 1:
  print("Rock! Go again!")
elif choice == "Rock" or "rock" and comp == 3:
  print("Scissors! You win!")
if choice == "Paper" or "paper" and comp == 3:
  print("Scissors! You lose!")
elif choice == "Paper" or "paper" and comp == 1:
  print("Rock! You win!")
elif choice == "Paper" or "paper" and comp == 2:
  print("Paper! Go again!")
if choice == "Scissors" or "scissors" and comp == 1:
  print("Rock! You lose!")
elif choice == "Scissors" or "scissors" and comp == 2:
  print("Paper! You win!")
elif choice == "Scissors" or "scissors" and comp == 3:
  print("Scissors! Go again!")
#Is it trying to run different values of the comp variable?
#Edit to make sure it only produces one output
