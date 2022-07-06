from human import Human
from AI import Ai

class Game:

    def __init__(self):
     self.human = Human("user1")
     self.computer = Ai("Computer")
     self.human2 = Human("user2")

    def run_game(self):
        self.greeting()
        self.game_mode()
        
    
       
            
    def game_mode(self):
        answer = input("Would you like to play Solo(press 1) or Multiplayer(press 2)?")
        if answer == "1":
            self.human_vs_Ai()
        else:
            self.human_vs_human()

    def human_vs_Ai(self):
        print("1asfa")


    def human_vs_human(self):
        self.human.choosing()
        self.human2.choosing()
        


    def comparing_gestures(self):

        self.human.choosing()
        if self.human.chosen_gesture == '1':
            print(self.human.chosen_gesture)
        

    ##AI or Human
    def greeting(self):
        print("welcome to the game")

