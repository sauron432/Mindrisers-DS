import random

number = random.randint(1,100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("Too low! Try again!")
    elif guess > number:
        print("Too high! Try again!")
    else:
        print("You guessed it! The number was " + str(number) + ".")
        play_again = input("Do you wanna play again?(Y/N)")
        if play_again.upper() == "N":
            break
            

        