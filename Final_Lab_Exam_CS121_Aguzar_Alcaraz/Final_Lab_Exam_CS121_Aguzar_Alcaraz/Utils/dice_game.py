from random import randint
from user_manager import *

class DiceGame:
    def __init__ (self, username):
        self.dice_game = DiceGame()
        win = 0

    def load_score():
        pass

    def save_scores():
        pass

    def play_game(self):
        def __init__(self, cpu, user):
            self.cpu = cpu
            self.user = user
            
        while True:
            try:
                print ("Starting Dice Game...")
                for i in range (3):
                    self.cpu = randint(1, 6)
                    self.user = randint(1, 6)
                    print()
                    print (f"cpu: {self.cpu}")
                    print (f"user: {self.user}")
                    if self.user > self.cpu:
                        self.win += 1
                        print ("You win! You earned 1 point")
                    elif self.user < self.cpu:
                        print ("You lose! You didn't earn a point")
                    else:
                        print ("It's a tie")

                print (self.win)

                if self.win != 3:
                    print("You cannot proceed to the next stage")
                else:
                    print("You can proceed to the next stage")
                    choice = input("Would you like to continue?[y/or any character]: ").lower()
                    if choice == "y":
                        pass
                    else:
                        pass
            except ValueError as e:
                print(f"An error occured{e}")

    def show_top_scores():
        pass

    def logout():
        pass
    
    def menu():

        print("Menu:")
        print("1. Start Game")
        print("2. Show top scores")
        print("3. Log out")

        choice = input("Enter your choice, or leave in it blank to cancel ")
        if choice == "1":
            self.play_game()
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass