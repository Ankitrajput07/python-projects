#Find inter your number is even of odd.

num = abs(int(input("Enter your number:")))


if num % 2 == 0:
    print("Your number is even.")

elif num % 2 != 0:
    print("Your number is odd.")

else:
    print("Zero is middel part.")