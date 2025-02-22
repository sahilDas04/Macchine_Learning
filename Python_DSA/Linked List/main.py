import random

def game():
    choice = input("1. Start \n 2. Exit \n")
    num = random.randint(1, 100)
    guess_number = int(input("Guess Number : "))
    
    if num == guess_number:
        print("Congratulations! You Won the Guess!!!")
    elif num > guess_number:
        print("You have to think higher!!!")
    elif num < guess_number:
        print("You have to think smaller!!!")
    exit()

game()