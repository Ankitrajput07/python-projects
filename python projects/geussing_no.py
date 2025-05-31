import random


print("Welcome to the gussing game.")

options = input("Do you want to play the game?\n")

if options.lower() == "yes":
    print("great!:)so, I will start your game.")
    guess = random.randint(1,10)
    given_chance = 1
    
    while True:
        g_number = int(input("guess a number between 1 and 10:"))
        if g_number == guess:
            print("You guessed it right! The number was", guess)
            print("You won the game! whit a score of", given_chance)
            break
        else:
            print("Sorry, you guessed it wrong. The number was", guess , "please try again.")
            print("I give you a next chance.")
            given_chance +=1

    

elif options.lower() == "no":
    print("Okay, have a nice day!:)")

else:
    print("please enter a valid option.")
    



    