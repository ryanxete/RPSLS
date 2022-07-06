import random
from player import Player

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)
        
    def choosing(self):
        self.chosen_gesture = random.choice(self.gesture_list)
        return self.chosen_gesture

# Rock crushes Scissors
# Scissors cuts Paper 
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock 
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock