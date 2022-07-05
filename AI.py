import random
from player import Player

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)
        
    
    def choosing(self):
        self.chosen_gesture = random.randint()##where we left off!