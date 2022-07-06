import random
from player import Player

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)
        
    
    def choosing(self):
        self.chosen_gesture = random.randint(1, 5)
        return self.chosen_gesture