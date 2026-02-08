import random
import os
a = ""

# Function to clear the screen (works on Windows/Linux/Mac)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to calculate hand value (handles aces)
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            aces += 1
            value += 11
        else:
            value += int(card)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Function to deal a card
def deal_card(deck):
    return deck.pop()

# Main game function
def play_blackjack():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    player_value = calculate_hand_value([card.split()[0] for card in player_hand])
    dealer_value = calculate_hand_value([card.split()[0] for card in dealer_hand])
    
    print("Welcome to Blackjack!")
    print(f"Your hand: {player_hand} (Value: {player_value})")
    print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
    
    # Player's turn
    while player_value < 21:
        action = input("Do you want to (h)it or (s)tand? ").lower()
        if action == 'h':
            new_card = deal_card(deck)
            player_hand.append(new_card)
            player_value = calculate_hand_value([card.split()[0] for card in player_hand])
            print(f"Your hand: {player_hand} (Value: {player_value})")
            if player_value > 21:
                print("Bust! You lose.")
                return
        elif action == 's':
            break
        elif action == 'q':
            print("Thanks for playing!")
            return
        else:
            print("Invalid input. Type 'h' for hit or 's' for stand.")
    
    # Dealer's turn
    print(f"Dealer's hand: {dealer_hand} (Value: {dealer_value})")
    while dealer_value < 17:
        new_card = deal_card(deck)
        dealer_hand.append(new_card)
        dealer_value = calculate_hand_value([card.split()[0] for card in dealer_hand])
        print(f"Dealer hits: {new_card}. Dealer's hand: {dealer_hand} (Value: {dealer_value})")
    
    # Determine winner
    if dealer_value > 21:
        print("Dealer busts! You win!")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")
    
    # Play again?
    again = input("Play again? (y/n): ").lower()
    if again == 'y':
        clear_screen()
        play_blackjack()
    else:
        print("Goodbye!")

# Start the game
if __name__ == "__main__":
    play_blackjack()