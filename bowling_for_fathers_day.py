# Import necessary modules from the tkinter library
import tkinter as tk
import random
import time
import math

# Create the main window
root = tk.Tk()
root.title("Bowling For Fathers Day!")

# Set the dimensions of the game window
canvas = tk.Canvas(root, width=600, height=800, bg="lightblue")
canvas.pack()


# Create the bowling lane
def create_lane(canvas):
    lane_color = "#D2B48C"  # Light brown or tan color
    lane_top = 30
    lane_bottom = 775
    lane_left = 200
    lane_right = 400
    canvas.create_rectangle(
        lane_left, lane_top, lane_right, lane_bottom, fill=lane_color, outline=""
    )


# Create the bowling pins in a triangular formation
def create_pins(canvas):
    pin_color = "white"
    pin_radius = 10
    pin_positions = [
        (300, 125),  # Front pin
        (275, 100),
        (325, 100),  # Second row
        (250, 75),
        (300, 75),
        (350, 75),  # Third row
        (225, 50),
        (275, 50),
        (325, 50),
        (375, 50),  # Fourth row
    ]
    pins = []
    for pos in pin_positions:
        pin = canvas.create_oval(
            pos[0] - pin_radius,
            pos[1] - pin_radius,
            pos[0] + pin_radius,
            pos[1] + pin_radius,
            fill=pin_color,
        )
        pins.append(pin)
    return pins


# Create the bowling ball at the bottom center of the screen
def create_ball(canvas):
    ball_radius = 25
    ball_x = 300
    ball_y = 750
    ball = canvas.create_oval(
        ball_x - ball_radius,
        ball_y - ball_radius,
        ball_x + ball_radius,
        ball_y + ball_radius,
        fill="black",
    )
    return ball


# Handle the ball's motion when the mouse is clicked
def roll_ball(event, canvas, ball, pins):
    ball_speed = -10  # Negative value to move the ball upwards
    while canvas.coords(ball)[1] > 50:
        canvas.move(ball, 0, ball_speed)
        root.update()
        time.sleep(0.05)
    knock_down_pins(canvas, pins, ball)


# Knock down pins and display fireworks
def knock_down_pins(canvas, pins, ball):
    canvas.delete(ball)
    for pin in pins:
        canvas.delete(pin)

    display_fireworks(canvas)


# Create star-shaped fireworks
def create_star(canvas, x, y, size, color):
    points = []
    for i in range(5):
        angle = i * 144  # Star points (144 degrees between each point)
        x_offset = size * math.cos(math.radians(angle))
        y_offset = size * math.sin(math.radians(angle))
        points.extend([x + x_offset, y + y_offset])
    star = canvas.create_polygon(points, fill=color, outline=color)
    return star


# Display fireworks
def display_fireworks(canvas):
    start_time = time.time()
    while time.time() - start_time < 4:  # Display fireworks for 4 seconds
        x = random.randint(200, 500)
        y = random.randint(150, 750)
        size = random.randint(100, 200)  # Larger size for the star
        color = random.choice(["red", "green", "blue", "yellow", "purple", "orange"])
        firework = create_star(canvas, x, y, size, color)
        root.update()
        time.sleep(0.5)
        canvas.delete(firework)
    display_message(canvas)


# Display "HAPPY FATHER'S DAY!!!" message
def display_message(canvas):
    canvas.create_text(
        300, 200, text="HAPPY FATHER'S DAY!!!", font=("Arial", 35), fill="black"
    )


# Initialize the game elements
create_lane(canvas)
pins = create_pins(canvas)
ball = create_ball(canvas)

# Bind the mouse click event to the roll_ball function
canvas.bind("<Button-1>", lambda event: roll_ball(event, canvas, ball, pins))

# Start the Tkinter main loop
root.mainloop()
