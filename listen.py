from pynput.keyboard import Key, Controller
import keyboard
import speech_recognition as sr
import sys
import winsound
import time

keyboardPresser = Controller()
r = sr.Recognizer()

## action variables
# Variables
LISTEN_DURATION = 2
STOP_LOOPING = False
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 100 ms

# Condition
STOP = ['stop', 'quit', 'exit']
OBJECTION_CON = 'objection'
PRESS_CON = 'press'
PRESENT_CON = 'present'
OPTION_CON = 'option'
RECORD_CON = 'record'
SAVE_CON = 'save'

# Keystroke
LISTEN = 'w'
OBJECTION = 'e'
PRESS = 'q'
PRESENT = 'e'
OPTION = Key.esc
RECORD = Key.tab


def keystroke(action):
    keyboardPresser.press(action)
    keyboardPresser.release(action)
    time.sleep(0.3)


def triggerCommand(command):
    if OBJECTION_CON in command:
        keystroke(OBJECTION)
        return True
    elif PRESS_CON in command:
        keystroke(PRESS)
        return True
    elif PRESENT_CON in command:
        keystroke(PRESENT)
        return True
    elif OPTION_CON in command:
        keystroke(OPTION)
        return True
    elif RECORD_CON in command:
        keystroke(RECORD)
        return True
    elif SAVE_CON in command:
        keystroke(Key.esc)
        keystroke(Key.enter)
        keystroke(Key.enter)
        keystroke(Key.left)
        keystroke(Key.enter)
        time.sleep(3)
        keystroke(Key.backspace)
        keystroke(Key.backspace)
        return True
    else:
        return False


def check_if_substring(word, substrings):
    return any(substring in word for substring in substrings)

def listen():
    global STOP_LOOPING
    STOP_LOOPING = False

    while True:
        if keyboard.is_pressed(LISTEN):
            while not STOP_LOOPING:
                # while True:
                with sr.Microphone() as source:
                    # know when the system is listening
                    winsound.Beep(frequency, duration)
                    # read the audio data from the default microphone
                    audio_data = r.record(source, duration=LISTEN_DURATION)
                    try:
                        text = r.recognize_google(audio_data)
                        # check text recognized
                        # print(text)
                        if check_if_substring(text, STOP):
                            sys.exit()
                        res = triggerCommand(text)
                        if res:
                            STOP_LOOPING = True
                    except sr.UnknownValueError:
                        print('No Voice Detected')
            STOP_LOOPING = False


if __name__ == '__main__':
    listen()
