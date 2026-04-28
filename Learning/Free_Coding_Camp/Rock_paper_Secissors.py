# ---- rock, paper and secissors game ----

import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors) : ")
    all_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(all_choices)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices



def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer :
        return "it is a tie!"
    elif player == "rock" :
        if computer == "scissors":
         return "player is the winner "

    elif player == "rock" :
            if computer == "paper":
             return "computer is the winner "

    elif player == "paper" :
                if computer == "rock":
                 return "player is the winner "

    elif player == "paper" :
                    if computer == "scissors":
                     return "computer is the winner "

    elif player == "scissors" :
                    if computer == "rock":
                     return "computer is the winner "

    elif player == "scissors" :
                    if computer == "paper":
                     return "player is the winner "

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)


