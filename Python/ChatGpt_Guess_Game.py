import random

# ---- Get Valid Number Input ----
def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Please enter a valid number!")

# ---- Main Game ----
def play_game():
    print("=" * 50)
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("=" * 50)
    
    # Choose difficulty
    print("\nChoose difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    
    difficulty = get_number("Enter your choice (1-3): ")
    
    if difficulty == 1:
        max_range = 50
        max_attempts = 10
    elif difficulty == 2:
        max_range = 100
        max_attempts = 7
    elif difficulty == 3:
        max_range = 200
        max_attempts = 5
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_range = 100
        max_attempts = 7
    
    # Generate random number
    secret_number = random.randint(1, max_range)
    attempts = 0
    
    print(f"\n🎯 I'm thinking of a number between 1 and {max_range}")
    print(f"You have {max_attempts} attempts to guess it!\n")
    
    # Game loop
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        guess = get_number(f"Attempt {attempts}/{max_attempts} - Enter your guess: ")
        
        if guess < 1 or guess > max_range:
            print(f"❌ Please guess between 1 and {max_range}!")
            attempts -= 1  # Don't count this as an attempt
            continue
        
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
            print(f"⭐ Score: {max_attempts - attempts + 1}/{max_attempts}")
            return True
        elif guess < secret_number:
            print(f"📈 Too low! You have {remaining} attempts left.")
        else:
            print(f"📉 Too high! You have {remaining} attempts left.")
    
    # Game over
    print(f"\n💔 Game Over! The number was {secret_number}")
    return False

# ---- Play Again Loop ----
def main():
    while True:
        play_game()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! Goodbye!")
            break
        print("\n" + "=" * 50 + "\n")

# ---- Start Game ----
if __name__ == "__main__":
    main()