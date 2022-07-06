from human import Human
from AI import Ai

class Game:

    def __init__(self):
     self.human = Human("user1")
     self.computer = Ai("Computer")

    def run_game(self):
        self.greeting()
        ##choice method
        if self.human.choosing() == '1':
            print("lets start the game!")
        
    ##choice method:
    ##AI or Human
    def greeting(self):
        print("welcome to the game")

