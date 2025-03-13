import random
guess = int(input("Guess a number from 1 to 10: "))
answer = random.randint(1,10)
if guess == answer:
    print("You got it right!")
else:
    print("You got it wrong! The answer was " + str(answer) + "!")