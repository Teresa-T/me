"""Week 3, Exercise 2.

An example of how a guessing game might be written.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between 0 and {} ?".format(upperBound)) #ask for input for upper bounds
    upperBound = int(upperBound) #make sure the input is an integer and not a string

    actualNumber = random.randint(0, upperBound) #generate a random integer within the range set

    guessed = False #set condition for the while loop

    while not guessed: #condition for the while loop (terminating condition))
        guessedNumber = int(input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),) #print the input number
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True #terminating condition for while loop
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
