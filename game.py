from human import Human
from AI import Ai

class Game:

    def __init__(self):
     self.human = Human("user1")
     self.computer = Ai("Computer")

    def run_game(self):
        self.greeting()
        self.human.choosing()
        
    def greeting(self):
        print("welcome to the game")

