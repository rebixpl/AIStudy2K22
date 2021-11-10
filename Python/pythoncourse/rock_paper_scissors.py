import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?").lower()

    if player == computer:
        print("Player: " + player)
        print("Computer: " + computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You lose!")
        if computer == "scissors":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You lose!")
        if computer == "paper":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You lose!")
        if computer == "rock":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You win!")

    play_again = input("Play Again? (yes/no)").lower()

    if play_again != "yes":
        break

print("bye!")

