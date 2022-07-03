region = input("Select your region (EU/US): ")
if region == "US":
    age = input("Type your age: ")
    if age.isdigit() == False:
        exit("Age has to be a number!")
    age = int(age)
    while age > 120:
        print("Come on, your real age. Let's try again.")
        age = input("Type your age: ")
        age = int(age)
    if age >= 21 and age <= 50:
        drink = input("Welcome to 'World's Alcohols'. Please, select your drink: ")
        print(f"You selected {drink}. It will be served within 10 minutes.")
    elif age > 50 and age <= 120:
        print("Welcome to 'World's Alcohols'. Please, be reminded that in your age alcoholic drinks are harmful.")
        drink = input("If you wish to order anyway, please, select your drink: ")
        print(f"You selected {drink}. It will be served within 10 minutes.")
    else:
        exit("You are too young for alcohol!")
elif region == "EU":
    age = input("Type your age: ")
    if age.isdigit() == False:
        exit("Age has to be a number!")
    age = int(age)
    while age > 120:
        print("Come on, your real age. Let's try again.")
        age = input("Type your age: ")
        age = int(age)
    if age >= 18 and age <= 50:
        drink = input("Welcome to 'World's Alcohols'. Please, select your drink: ")
        print(f"You selected {drink}. It will be served within 10 minutes.")
    elif age > 50 and age <= 120:
        print("Welcome to 'World's Alcohols'. Please, be reminded that in your age alcoholic drinks are harmful.")
        drink = input("If you wish to order anyway, please, select your drink: ")
        print(f"You selected {drink}. It will be served within 10 minutes.")
    else:
        exit("You are too young for alcohol!")
else:
    exit("You can only pick EU or US.")
gender = input("Select your gender: ")
if gender == "Female":
    exit("Great! You get bonus aperol. Thank you for ordering with us. Enjoy your day!")
else:
    exit("Sorry, no bonuses here. Thank you for ordering with us. Enjoy your day!")
