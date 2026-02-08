import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()
        self.canvas.focus_set()  # Ensure keyboard input works

        # Game variables
        self.snake = [(200, 200)]  # Starting position
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.game_over = False

        # Bind keys
        self.root.bind("<Key>", self.change_direction)

        # Score display
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

        # Wall collision
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400:
            self.game_over = True
            return

        new_head = (head_x, head_y)
        self.snake.insert(0, new_head)

        # Self collision (ignore tail)
        if new_head in self.snake[1:]:
            self.game_over = True
            return

        # Food collision
        if new_head == self.food:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.create_food()
        else:
            self.snake.pop()  # Remove tail

    def draw(self):
        self.canvas.delete("all")

        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x, y, x + 20, y + 20,
                fill="green", outline=""
            )

        # Draw food (slightly padded)
        self.canvas.create_oval(
            self.food[0] + 2, self.food[1] + 2,
            self.food[0] + 18, self.food[1] + 18,
            fill="red", outline=""
        )

    def update_game(self):
        if not self.game_over:
            self.move_snake()
            self.draw()

            # Dynamic speed (faster as score increases)
            speed = max(60, 200 - self.score * 10)
            self.root.after(speed, self.update_game)
        else:
            self.canvas.create_text(
                200, 190,
                text="Game Over",
                font=("Arial", 24),
                fill="white"
            )
            self.canvas.create_text(
                200, 230,
                text=f"Final Score: {self.score}",
                font=("Arial", 16),
                fill="white"
            )

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
