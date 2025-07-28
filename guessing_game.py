#Guessing game- Azhar, Diana, Amonji, Felix 
import random 

def guessing_game():
    return random.randint(1,100)
print(guessing_game())

def get_user_guess():
    while True:
        try:
            guess = int(input("Input guess: "))
            if guess >= 1 or guess <= 100: 
            # if user input is valid so between 1 and 100 return <= range()
                return guess
            else: print("")
            # else say that they need to re enter
        except ValueError:
            print("Enter an integer.")

get_user_guess()
