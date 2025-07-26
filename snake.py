import tkinter as tk
import random

# Game settings
GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 100  # milliseconds between moves
SPACE_SIZE = 20  # size of each segment
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for _ in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.food = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Wrap-around logic
    if x < 0:
        x = GAME_WIDTH - SPACE_SIZE
    elif x >= GAME_WIDTH:
        x = 0
    if y < 0:
        y = GAME_HEIGHT - SPACE_SIZE
    elif y >= GAME_HEIGHT:
        y = 0

    new_head = [x, y]

    # Insert new head
    snake.coordinates.insert(0, new_head)
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Check if snake ate the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        canvas.delete("food")
        food = Food()
    else:
        # Remove tail
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if new_direction != opposites.get(direction):
        direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Self collision only
    for segment in snake.coordinates[1:]:
        if x == segment[0] and y == segment[1]:
            return True
    return False

def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2,
                       text="GAME OVER", fill="red", font=("Arial", 30, "bold"))

# Set up window
window = tk.Tk()
window.title("Snake Game - Wrap Around Edition")
window.resizable(False, False)

direction = "right"

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
