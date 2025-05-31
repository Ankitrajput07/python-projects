#Adding availabel items in your hotal

items = {
    "Pizza" : 99,
    'Barger' : 60,
    'Pastaa' : 40,
    'Hakka nudals' : 80,
    'Rise' : 60,
    "Biryani" : 120,
    'Chate' : 30
}

#Greeting 
print('Welcome to the A.S 7*******STAR hotal.')

total_order = 0
print(f"Pizza:99\nBarger:60\nPastaa:40\nHakka nudals:80\nRise:60\nBiryani:120\nChate:30")

item1 = input("Enter your order").capitalize()

if item1 in items:
    total_order +=items[item1]
    print("Order taked sucssesfully:).")

else:
    print('I am so feel gladi but this item is not in our menu plz try something....!')

while True:
    somthing_order = input("Can you order somthing next?(Yes/No):").capitalize()

    if somthing_order == 'Yes':

        item2 = input("Enter your next order sir...:)").capitalize()

        if item2 in items:
            total_order+=items[item2]
            print("Your next order taked sucssesfully:).")

        else:
            print('I am so feel gladi but this item is not in our menu plz try something....!')

    else:
        break

print(f"Your billing amount is {total_order},\nhave a good day :)")
