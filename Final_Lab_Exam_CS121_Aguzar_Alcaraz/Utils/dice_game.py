from random import randint
from user_manager import *

class DiceGame:
    def __init__ (self, username):
        pass

    def load_score():
        pass

    def save_scores():
        pass

    def play_game(self, cpu, username):
        print ("Starting Dice Game...")
        win = 0
        for i in range (3):
            cpu = randint(1, 6)
            user = randint(1, 6)
            print()
            print (f"cpu: {cpu}")
            print (f"user: {user}")
            if user > cpu:
                win += 1
                print ("You win! You earned 1 point")
            elif user < cpu:
                print ("You lose! You didn't earn a point")
            else:
                print ("It's a tie")

        print (win)

        if win != 3:
            print("You cannot proceed to the next stage")
        else:
            print("You can proceed to the next stage")
            choice = input("Would you like to continue?[y/or any character]: ").lower()
            if choice == "y":
                pass
            else:
                pass

        pass

    def show_top_scores():
        pass

    def logout():
        pass
    
    def menu():
        pass