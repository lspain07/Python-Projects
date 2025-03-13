import random #imports the random module's functions into the file
guess = int(input("Guess a number from 1 to 10: ")) #declares the "guess" variable as an integer meant to be entered by the user
answer = random.randint(1,10) #declares the "answer" variable and uses the randint function of the random module to assign a value from 1 to 10 to the answer variable
if guess == answer:
    print("You got it right!") 
else:
    print("You got it wrong! The answer was " + str(answer) + "!")
#the integer value of the guess and answer variables must be equal for the file to print the first message
