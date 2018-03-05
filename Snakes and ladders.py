# importing random module to simulate dice roll
import random

# initialising all my variables
name = input(str("please enter your name:"))
comp_score = 0
player_score = 0
active_player = 0
winner = None
allLadders = {1: 4, 2: 44, 3: 50, 4: 70}
allSnakes = {30: 10, 75: 35, 99: 10}


# DEFINING ALL MY FUNCTIONS

# rolls dice
def dice_roll():
    return random.randint(2, 13)


# Decides who goes first
def determine_first_move():
    global active_player

    while active_player == 0:
        player_roll = dice_roll()
        comp_roll = dice_roll()

        if player_roll > comp_roll:
            active_player = 1
            print("Good job you're first roller")
        elif comp_roll > player_roll:
            active_player = 2
            print(" Aww man the computer beat you for the first roll")


# Checks for winners
def check_for_winner(player_score, comp_score):
    global winner

    if player_score >= 100:
        winner = 1
    elif comp_score >= 100:
        winner = 2


def check_snake_or_ladder(active_player, score):
    new_score = 0
    if score in allSnakes:
        new_score = allSnakes[score]
        print(" Oh no " + str(active_player) + " went down a snake")

    if score in allLadders:
        new_score = allLadders[score]
        print(" Weeee! " + str(active_player) + " went up a ladder")

    return new_score


print("\n Hello welcome to the game" + name)
determine_first_move()

while not winner:
    if active_player == 1:
        input("\t \n Player 1 hit enter to roll")
        roll = dice_roll()
        player_score += roll
        player_score = check_snake_or_ladder(1, player_score)

        print(" You rolled " + str(roll) + " your new score is " + str(player_score))
        check_for_winner(player_score, comp_score)

    elif active_player == 2:
        roll = dice_roll()
        comp_score += roll
        player_score = check_snake_or_ladder(2, comp_score)
        print(" The computer rolled " + str(roll) + " their new score is " + str(comp_score))
        check_for_winner(player_score, comp_score)

    if active_player == 1:
        active_player = 2
    else:
        active_player = 1

print("Oh great we have a winner player " + str(winner))
