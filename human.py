from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        
    def choosing(self):
        self.chosen_gesture = input("please choose your gesture from the list for this round\n1: rock\n2: paper\n3: sciccors\n4: lizard\n5: spock\nplease enter your desired number!")