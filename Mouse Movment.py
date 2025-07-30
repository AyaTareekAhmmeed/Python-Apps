import time
import random
import pyautogui

jiggle_interval = 5  # Seconds before jiggle
jiggle_amount = 10  # Pixels
stop_threshold = 5  # How much movement counts as "user moved the mouse"

def get_mouse_position():
    """Get the current mouse position."""
    return pyautogui.position()

print("Mouse jiggler running... Move your mouse to stop it.")

last_position = get_mouse_position()

while True:
    time.sleep(jiggle_interval)

    current_position = get_mouse_position()

    # Check if the mouse moved significantly
    if abs(current_position[0] - last_position[0]) > stop_threshold or abs(current_position[1] - last_position[1]) > stop_threshold:
        print("Mouse movement detected. Exiting.")
        break  # Stop the loop if the mouse was moved

    # Move the mouse slightly in a random direction
    dx = random.choice([-jiggle_amount, jiggle_amount])
    dy = random.choice([-jiggle_amount, jiggle_amount])

    pyautogui.moveRel(dx, dy, duration=0.2)  # Move smoothly
    print(f"Mouse moved by {dx}, {dy}")

    # Update last known position
    last_position = get_mouse_position()

print("Mouse jiggler stopped.")
