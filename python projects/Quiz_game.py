#This is a small Quiz game only for me..!

print("Welcome To Your Owne Game.")

y_question = input("Can you dicering for playing this game?\n")
score = 0
total_qustions = 10


if y_question.lower() == "yes" :
    print("Great :) so, I will stared your Quiz.")
    Q1 = input("You are a inteligent parsen?\n")

    if Q1.lower() == "trying to my best":
        print("oh..! got it, right.")
        score +=1

    else:
        print("Not a parfect, Try keep :)")
    Q2 = input("What is the right way to clarefy thoughts?\n")

    if Q2.lower() == "writedown your though":
        print("oh..! got it, right.")
        score +=1
    else:
        print("Not a parfect, Try keep :)")
    Q3 = input("what is the type for humen to sutabel?\n")

    if Q3.lower() == "animal":
        print("oh..! got it, right.")
        score +=1
    else:
        print("Not a parfect, Try keep :)")

    Q5 = input("what the think that it make difrent bitween animels in human?\n")

    if Q5.lower() == "thinking ability":
        print("oh..! got it, right.")
        score +=1
    else:
        print("Not a parfect, Try keep :)")

    Q6 = input("Can ous say's the earth is flate?\n")

    if Q6.lower() == "no":
        print("oh..! got it, right.")
        score +=1
    else:
        print("Not a parfect, Try keep :)")

    Q7 = input("What is the main parpase of life?\n")

    if Q7.lower() == "understanding for life":
        print("oh..! got it, right.")
        score +=1
    else:
        print("Not a parfect, Try keep :)")

    Q8 = input("What is right think in life?\n")

    if Q8.lower() == "select right path in life":
        print("oh..! got it, right.")
        score +=1
    else:
        print("Not a parfect, Try keep :)")

    Q9 = input("Who is god?\n")
    
    if Q9.lower() == "unknown":
        print("oh..! got it, right.")
        score +=1
    else:
        print("Not a parfect, Try keep :)")

    Q10 = input("Can you beliving god?\n")

    if Q10.lower() == "yes":
        print("oh..! gt it, right.")
        score +=1
    else:
        print("Not a parfect, Try keep :)")
    
    print(f"Your final currect answers score is:{score} and Your parcenteg is{(score/total_qustions)*100}%.")

    print("Thank Q for plaing :) .")

elif y_question.lower() == "no":
    print("OK Thanks....!")

else:
    print("What's runing in your mind, can you play ?")

