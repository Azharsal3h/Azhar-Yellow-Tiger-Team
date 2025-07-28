#Guessing game- Azhar, Diana, Amonji, Felix 
import random 

def generate_random_number():
    return random.randint(1,100)
print(generate_random_number())

def get_user_guess():
    while True:
        try:
            guess = int(input("Input guess: "))
            if guess >= 1 and guess <= 100: 
            # if user input is valid so between 1 and 100 return <= range()
                return guess
            else: 
                print("enter valid number") 
            # else say that they need to re enter
        except ValueError:
            print("Enter an integer.")


get_user_guess()
def game_loop():
    secret_number = generate_random_number()

    while True:
        guess = get_user_guess()

        if guess < secret_number:
            print("Try going higher")
        elif guess > secret_number:
            print("Try going lower")
        else:
            print(f"You did it, you guessed the correct number.")
            

if __name__ == "__main__": 
    game_loop()
#secret_number(too_high):
    #def game_loop():
     #   txt = "96"
   #     x = txt.lower(96)
  #      print(x)
 #       if __name__ == "__main__": 
#            game_loop()

# mainly low guesses and mid guesses and got 11 guesses 