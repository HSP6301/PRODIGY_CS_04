# Keylogger with Telegram Integration

## Introduction

This application Python-based keylogger, designed to capture and log keystrokes from the keyboard in real-time. The logged data is saved in a text file (`key_log.txt`), and periodically, the log file is sent to a specified Telegram chat. This keylogger is developed using the `pynput` library for capturing keyboard inputs, `requests` for sending HTTP requests to Telegram, and `os` for managing file operations. This tool is a powerful way to monitor and analyze keystrokes, making it useful for cybersecurity research, monitoring system usage, or educational purposes.

## Features

1. **Real-time Keystroke Logging**:
   - Captures all keystrokes, including letters, numbers, and special characters.
   - Supports case sensitivity, ensuring that both lowercase and uppercase letters are logged accurately.

2. **Shift Key Handling**:
   - Detects when the Shift key is pressed to log the subsequent keystroke in uppercase if applicable.
   - Handles left and right Shift keys independently.

3. **Secure Log Transmission**:
   - Periodically sends the log file to a specified Telegram chat using the Telegram Bot API.
   - Ensures that only non-empty log files are sent, preventing unnecessary data transmission.

4. **File Management**:
   - Clears the log file after successfully sending it to Telegram, preventing duplicate logs and keeping the file size manageable.

5. **Log File Handling**:
   - The `log_keystroke` function logs keystrokes to a file named `key_log.txt`.
   - The `send_log_to_telegram` function reads this file and sends it to the specified Telegram chat using the `sendDocument` API method.

6. **Customizable Time Interval**:
   - Allows you to set the interval at which the log file is sent to Telegram (default is every 15 seconds).


## Usage

1. **Setting Up Telegram Bot**:
   - Create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather).
   - Obtain the bot token and the chat ID where you want to receive the logs.
    
2. **Code Configuration**:
   - Replace `'your-telegram-bot-token-here'` with your actual Telegram bot token.
   - Replace `'your-chat-id-here'` with the chat ID where you want to receive the log files.

3. **Running the Keylogger**:
   - Simply run the Python script. The keylogger will start capturing keystrokes and saving them to `key_log.txt`.
   - Every 15 seconds (or the interval you set), the log file will be sent to the specified Telegram chat.

4. **Stopping the Keylogger**:
   - The keylogger runs in a background thread. To stop it, you can terminate the script (e.g., by closing the terminal or using a keyboard interrupt like `Ctrl+C`).


## Error Handling

1. **File Operations**:
   - The code checks if the log file exists and is non-empty before attempting to send it to Telegram.
   - If the log file is empty or doesn't exist, the file is not sent, and a message is printed to the console.

2. **Telegram API Requests**:
   - The code sends the log file using a POST request to the Telegram Bot API.
   - If the request is successful (`status_code == 200`), a success message is printed.
   - If the request fails, the error status code is printed, helping to diagnose issues (e.g., invalid bot token, incorrect chat ID, network issues).

3. **Shift Key Handling**:
   - The code tracks the state of the Shift key to handle case sensitivity correctly. If the Shift key is active, the next keystroke is logged as uppercase.


## Requirements

To run the Keylogger with Telegram Integration, the following are required:

- **Python 3.x**: The application is written in Python, so a compatible version of Python 3.x is needed.
- **PyQt5**: The PyQt5 library is used for the graphical user interface. Install it using pip if it's not already installed: 
  ```bash
  pip install PyQt5
  ```
- **pynput**: For capturing keyboard input. Install it using pip
  ```bash
  pip install pynput
  ```
- **requests**: For sending HTTP requests to Telegram. Install it using pip
  ```bash
  pip install requests
  ```
- **Telegram Bot**:
   - A Telegram bot is required to send the log files. Create one and obtain the bot token and chat ID.


## Steps to Perform

1. **Install Python**:
   - Download and install Python from the [official website](https://www.python.org/).

2. **Install Required Libraries**:
   - Open your terminal or command prompt and run the following commands:
     ```bash
     pip install pynput requests
     ```


3. **Create a Telegram Bot**:
   - Open Telegram and search for `BotFather`.
   - Use the `/newbot` command to create a new bot.
   - Follow the instructions to name your bot and obtain the bot token.
   - Search for your bot in Telegram using the name you gave it.
   - Start a chat by clicking on the bot and sending a simple message, like "Hello."
     - **Get the Chat ID**
       - Open your web browser and navigate to the following URL:
       ```bash
       https://api.telegram.org/bot<YourBotToken>/getUpdates
       ```
       - Replace `<YourBotToken>` with the actual API token you received from `BotFather`.
       - Find the Chat ID:
        - Look for the message field in the JSON response.
        - Inside the message field, you will find a chat object.
        - The chat object contains the id, which is your Chat ID.

4. **Configure the Code**:
   - Open the Python script and replace the placeholder values with your bot token and chat ID.
     - Replace `your-chat-id-here` in your Python script with this Chat ID.
     - Replace `'your-telegram-bot-token-here'` with your actual Telegram bot token.
   - Adjust the time interval if needed by changing `time.sleep(15)` to your desired interval (e.g., `time.sleep(60)` for 60 seconds).

5. **Run the Script**:
   - Execute the script by running `python your_script_name.py` in your terminal.
   - The keylogger will start, capturing keystrokes and sending logs to your Telegram chat.

## Important Notes
  - **Ethical Use**: As with the basic keylogger, ensure you have explicit permission before deploying this script on any system.
  - **Security**: Store your Telegram Bot API token securely and avoid sharing it publicly.
  - **Legal Considerations**: Unauthorized use of keyloggers, especially ones that transmit data, is illegal in many jurisdictions.

## Conclusion

This keylogger is a powerful tool for monitoring and logging keystrokes, with secure and efficient log transmission via Telegram. Its features ensure accurate keystroke logging, secure file management, and seamless integration with Telegram for real-time log delivery. Whether you're using it for cybersecurity research, monitoring system usage, or educational purposes, this keylogger offers a practical and flexible solution.

Feel free to customize the code to fit your specific needs and ensure that you use it responsibly and ethically.
