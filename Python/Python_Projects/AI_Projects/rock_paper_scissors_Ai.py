import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("You can enter full names or r/p/s. Enter 'quit' or 'q' to stop.")
    
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    try:
        while True:
            user_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to stop: ").strip().lower()

            if user_choice in ("quit", "q"):
                break

            if user_choice in ("r", "p", "s"):
                user_choice = {"r": "rock", "p": "paper", "s": "scissors"}[user_choice]

            if user_choice not in choices:
                print("Invalid choice. Please choose rock, paper, or scissors.")
                continue

            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "scissors" and computer_choice == "paper") or \
                 (user_choice == "paper" and computer_choice == "rock"):
                print("You win this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1

            print(f"Score - You: {user_score}, Computer: {computer_score}")
            print()
    except (KeyboardInterrupt, EOFError):
        print("\nInterrupted.")
    finally:
        print(f"Final Score - You: {user_score}, Computer: {computer_score}")
        print("Thanks for playing!")

if __name__ == "__main__":
    rock_paper_scissors()