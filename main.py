from pynput.keyboard import Key, Controller
import keyboard
import speech_recognition as sr
import sys
import winsound
import time

keyboardPresser = Controller()
r = sr.Recognizer()

STOP_LOOPING = False
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 100 ms

def keystroke(action):
    keyboardPresser.press(action)
    keyboardPresser.release(action)
    time.sleep(0.3)

def triggerCommand(command):
    if 'objection' in command:
        keystroke('e')
        return True
    elif 'press' in command:
        keystroke('q')
        return True
    elif 'present' in command:
        keystroke('e')
        return True
    elif 'option' in command:
        keystroke('e')
        return True
    elif 'record' in command:
        keystroke('e')
        return True
    elif 'save' in command:
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


def listen():
    global STOP_LOOPING
    STOP_LOOPING = False

    while True:
        if keyboard.is_pressed('w'):
            while not STOP_LOOPING:
                # while True:
                with sr.Microphone() as source:
                    # know when the system is listening
                    winsound.Beep(frequency, duration)
                    # read the audio data from the default microphone
                    audio_data = r.record(source, duration=2)
                    try:
                        text = r.recognize_google(audio_data)
                        # check text recognized
                        # print(text)
                        if 'stop' in text or 'quit' in text:
                            sys.exit()
                        res = triggerCommand(text)
                        if res:
                            STOP_LOOPING = True
                    except sr.UnknownValueError:
                        print('No Voice Detected')
            STOP_LOOPING = False

if __name__ == '__main__':
    listen()
