# Maggi - Voice and Type Assistant

Maggi is a voice and type assistant that allows you to interact with your computer via speech or typed commands. You can control various functions, like opening websites, launching applications, performing Google searches, checking the battery status, setting timers, and more. Additionally, it includes an AI mode for conversational interactions.

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Running the Assistant](#running-the-assistant)
* [Usage](#usage)
* [Help Command](#help-command)
* [Contributing](#contributing)
* [License](#license)

## Features

* **Voice Mode:** Interact with the assistant using voice commands.
* **Type Mode:** Interact with the assistant by typing commands.
* **Website Opening:** Open popular websites like YouTube, Google, Facebook, etc.
* **Application Opening:** Open applications like Music, Safari, Calendar, Notes, etc.
* **Google Search:** Search Google for any term or query.
* **Battery Check:** Check the battery status of your device.
* **Timer:** Set a timer for a specified number of minutes.
* **AI Mode:** Engage in a conversation with the assistant powered by LLaMA.
* **Help Command:** Get a list of available commands.

## Requirements

To run this project, you need the following:

* Python 3.x
* `psutil` for battery status
* `speechrecognition` for voice recognition
* `webbrowser` for opening websites
* `subprocess` for opening applications
* A microphone (for voice mode)

## Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/Kishore-Nair/Maggie.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd maggi-assistant
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Assistant

Before running Maggi, ensure that Ollama is running in the background, as the AI mode relies on it.
Download ollama from: <https://ollama.com/>

**Starting Ollama:**

1.  **Open a new terminal or command prompt.** This will allow Ollama to run independently of Maggi.

2.  **Run the Ollama service.** The command to start Ollama might vary slightly depending on your installation method. Common commands include:

    * If you installed Ollama using the official method:
        ```bash
        ollama serve
        ```
    * On some systems, it might start automatically in the background. You can check if it's running by trying to interact with it or by checking your system's process monitor.

3.  **Keep this terminal window running in the background while you use Maggi.**

**Running Maggi:**

1.  Make sure you have a microphone connected to your system.

2.  Open a **new** terminal or command prompt (separate from the one running Ollama).

3.  Run the assistant script:

    ```bash
    python maggi_assistant.py
    ```

4.  You will be prompted to choose your mode:

      * **Voice Mode:** Speak commands to Maggi.
      * **Type Mode:** Type commands to interact with Maggi.

**Important:** Make sure Ollama is running *before* you try to use the "Invoke AI" command in Maggi. If Ollama is not running, the AI mode will not function correctly.

## Usage

### Voice Mode

Speak the command after Maggi says, "Listening...". For example:

* "Open YouTube"
* "Search for 'Artificial Intelligence' on Google"
* "Set a timer for 5 minutes"
* "What is the time?"

### Type Mode

Type your command when prompted:

* Type `open youtube`
* Type `search for Machine Learning`
* Type `check battery`

## Help Command

You can ask for help at any time by typing or saying: "Help"
Maggi will provide a list of all available commands with descriptions.

```txt
🛠️ Maggi's Commands:
1. 'Open <website name>' - Open a website (e.g., 'Open YouTube').
2. 'Open <application name>' - Open a system application (e.g., 'Open Music').
3. 'Search <query> on Google' - Search a term on Google.
4. 'Set a timer for <minutes>' - Set a timer.
5. 'Check battery' - Check battery status.
6. 'The time' - Get the current time.
7. 'Switch to type mode' - Switch to typing commands instead of speaking.
8. 'Switch to voice mode' - Switch to voice commands.
9. 'Invoke AI' - Activate the AI mode to interact with LLaMA.
10. 'Help' - Show this help message.
11. 'Exit' or 'Bye' - Exit the program.
```

## Contributing

If you would like to contribute to Maggi, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear messages.
4.  Push your changes to your forked repository.
5.  Submit a pull request with a description of the changes you have made.

