from human import Human
from AI import Ai

class Game:

    def __init__(self):
     self.human = Human("user1")
     self.human.choosing()
     self.human_choice = self.human.chosen_gesture
     self.computer = Ai()

    def greeting(self):
        print("welcome to the game")