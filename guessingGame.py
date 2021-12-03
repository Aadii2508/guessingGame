import random
number= random.randint(1, 9)
#random(guess)
chances= 0
while chances < 5:
    guess =int(input("enter your number: "))
    if guess == number:
        print('YOU WIN!!!')
    elif guess> number:
        print('YOUR GUESS WAS TOO HIGH, GUESS A NUMBER LOWER THAN THIS:', guess)
    else: 
        print('YOUR GUESS WAS TOO LOW, GUESS A NUMBER HIGHER THAN THIS:', guess)
    chances += 1

if not chances < 5:
    print("YOU LOSE", number)