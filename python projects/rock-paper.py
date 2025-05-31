import random
user_point = 0
computer_point = 0
option = ["rock","paper","secierss"]
while True:
    user_input = input("Enter your choice (rock,paper,secierss,Q for quit and show_point):").lower()
    computer_input = random.choice(["rock","paper","secierss"])
    if user_input == "q":
        print("Thanks, have a good day....!")
        quit()

    elif user_input == "show_point":
        print("Your point is",user_point)
        print("Computer point is",computer_point)

    elif user_input not in option:
        print("Select valied options so, plz try again... !)")

    elif user_input == "rock" and computer_input == "paper" or user_input == 'secierss' and computer_input == "paper" or user_input == "paper" and computer_input == "rock":
        print("computer choice is",computer_input)
        print("Great..! you are won")
        user_point +=1


    else:
        print("computer choice is",computer_input)
        print("sorry you are lost")
        computer_point +=1






