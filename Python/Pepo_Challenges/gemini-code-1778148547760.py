

class Player:
    # The __init__ function runs automatically when a new player is created
    def __init__(self, player_name, player_color):
        
        # 'self' means "MY personal stuff"
        self.name = player_name
        self.color = player_color
        self.health = 100  # Everyone gets 100 health automatically


# The moment we write this, __init__ runs in the background!
player1 = Player("Bob", "Blue")
player2 = Player("Alice", "Red")

print(player1.name) # Prints: Bob
print(player2.health) # Prints: 100