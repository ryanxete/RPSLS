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
            print(f"Computer chose {self.computer.chosen_gesture} and you chose {self.human.chosen_gesture}")
            self.comparing_gestures(self.human.chosen_gesture, self.computer.chosen_gesture)
            
        if self.human.count == 2:
            print("You won!!")
        else:
            print("Computer won!!")



    def human_vs_human(self):

        while self.human.count < 2 and self.human2.count < 2:
            self.human.choosing()
            self.human2.choosing()
            self.comparing_gestures(self.human.chosen_gesture, self.human2.chosen_gesture)
          

        
    def comparing_gestures(self, answer1, answer2):
        
        if answer1 == "rock" and answer2 == "paper":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "rock" and answer2 == "scissor":
            self.human.count +=1
        elif answer1 == "rock" and answer2 == "spock":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "rock" and answer2 == "lizard":
            self.human.count +=1
        elif answer1 == "paper" and answer2 == "rock":
            self.human.count +=1
        elif answer1 == "paper" and answer2 == "scissors":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "paper" and answer2 == "spock":
            self.human.count +=1
        elif answer1 == "paper" and answer2 == "lizard":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "scissors" and answer2 == "rock":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "scissors" and answer2 == "paper":
            self.human.count +=1
        elif answer1 == "scissors" and answer2 == "spock":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "scissors" and answer2 == "lizard":
            self.human.count +=1
        elif answer1 == "spock" and answer2 == "rock":
            self.human.count +=1
        elif answer1 == "spock" and answer2 == "paper":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "spock" and answer2 == "scissors":
            self.human.count +=1
        elif answer1 == "spock" and answer2 == "lizard":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "lizard" and answer2 == "rock":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "lizard" and answer2 == "paper":
            self.human.count +=1
        elif answer1 == "lizard" and answer2 == "scissors":
            self.human2.count +=1
            self.computer.count +=1
        elif answer1 == "lizard" and answer2 == "spock":
            self.human.count +=1
        elif answer1 == answer2:
            print("They are the same")
            pass

            
        
    def greeting(self):
        print("welcome to the game")

