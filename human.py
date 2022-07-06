from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        
    def choosing(self):
        self.chosen_gesture = input(f"please choose your gesture from the list below for this round \n{self.gesture_list}")
        self.chosen_gesture = self.chosen_gesture.lower()
        if self.chosen_gesture == "rock" or self.chosen_gesture == "paper" or self.chosen_gesture == "scissors" or self.chosen_gesture == "spock" or self.chosen_gesture == "lizard":
            pass
        else:
            print("please enter a valid gesture!")
            self.choosing()
        return self.chosen_gesture