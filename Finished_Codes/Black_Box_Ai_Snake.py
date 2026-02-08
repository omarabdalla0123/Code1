import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()
        
        # Game variables
        self.snake = [(200, 200)]  # Starting position (head)
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.game_over = False
        
        # Bind keys for movement
        self.root.bind("<Key>", self.change_direction)
        
        # Display score
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack()
        
        # Start game loop
        self.update_game()
    
    def create_food(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake:
                return (x, y)
    
    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
    
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 20
        elif self.direction == "Down":
            head_y += 20
        elif self.direction == "Left":
            head_x -= 20
        elif self.direction == "Right":
            head_x += 20
        
        # Check wall collision
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400:
            self.game_over = True
            return
        
        # Check self collision
        if (head_x, head_y) in self.snake:
            self.game_over = True
            return
        
        self.snake.insert(0, (head_x, head_y))
        
        # Check food collision
        if (head_x, head_y) == self.food:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.create_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten
    
    def draw(self):
        self.canvas.delete("all")
        # Draw snake
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+20, segment[1]+20, fill="green")
        # Draw food
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0]+20, self.food[1]+20, fill="red")
    
    def update_game(self):
        if not self.game_over:
            self.move_snake()
            self.draw()
            self.root.after(200, self.update_game)  # Update every 200ms
        else:
            self.canvas.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="white")
            self.canvas.create_text(200, 230, text=f"Final Score: {self.score}", font=("Arial", 16), fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
