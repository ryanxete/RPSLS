from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        
    def choosing(self):
        self.chosen_gesture = input(f"please choose your gesture from the list for this round \n{self.gesture_list}\nplease enter your desired gesture from the options above!")
        return self.chosen_gesture