from human import Human
from AI import Ai

class Game:

    def __init__(self):
     self.human = Human()
     self.computer = Ai()

    def greeting(self):
        print("welcome to the game")