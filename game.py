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
        while self.human.count < 2 and self.computer.count < 2:
            self.human.choosing()
            self.computer.choosing()
            self.comparing_gestures(self.human.chosen_gesture, self.computer.chosen_gesture)


    def human_vs_human(self):
        while self.human.count < 2 and self.human2.count < 2:
            self.human.choosing()
            self.human2.choosing()
            self.comparing_gestures(self.human.chosen_gesture, self.human2.chosen_gesture)
        
    def comparing_gestures(self, answer1, answer2):
        if answer1 == "1":
            print("dsdsd")
            
        
    def greeting(self):
        print("welcome to the game")

