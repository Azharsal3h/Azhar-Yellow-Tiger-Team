import random

class armor:
    def __init__(self, name, max_block):
        self.name = name 
        self.max_block = max_block

    def block(self):
        return random.radint(0, self.max_block)
    


