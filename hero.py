# hero.py for hero profile Azhar Saleh
import random

class Hero:
# we want hero to have a default starting health, by default is 100
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
	  # these parameters are passed in so set them as such
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def battle(self, opponent): 
        self.opponent = opponent 
        winner = random.choice({self, opponent})
        print(f"The winner is:{winner.name}") 

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200
    
    def battle(self, opponent):

    # '''Fight another hero and randomly declare a winner'''
        self.opponent = opponent
        print(f"{self.name} battles {opponent}!")

        # Randomly choose winner
        winner = random.choice([self, opponent])
        print(f"{winner} wins the battle!")


