# ability.py Azhar saleh

import random

class Ability:
    def __init__(self, name, max_damage):
   	# implement code here
        self.name = name 
        self.max_damage = max_damage 
    
    def attack(self):
        '''Return a random value between 0 and max_damage'''
        return random.randint(0, self.max_damage)
	# implement code here


# testing!
if __name__ == "__main__":
    fireball = Ability("Fireball", 20000)
    print(fireball.attack())

