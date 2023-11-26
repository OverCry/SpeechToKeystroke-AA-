# Speech To Action (Ace Attorney)
Using Python, convert audio phrases to trigger actions in Ace Attorney

Made to run on Windows

# Convert Script to .exe
1. Install pyinstaller (if missing)

- Open Command Prompt (as Admin)
- Paste in `pip install pyinstaller`

Ensure all packages are successfully installed
2. Run pyinstaller to convert file

- Redirect terminal to the file
- Paste in `pyinstaller --onefile listen.py`

If done correctly, the .exe file will be found in /dist in the project

# Usage
Rebind key presses depending on changes on the game

1. Run the script (which has been converted to an .exe)
2. Press the listening key (defaulted to `w`)
3. After the `~beep~`, say the action

# Actions
Phrases `Predefined actions`

- Listen `w`

- Objection `e`
- Press `q`
- Present `e`
- Option `esc`
- Record `tab`
- Save
- Quit/Stop
