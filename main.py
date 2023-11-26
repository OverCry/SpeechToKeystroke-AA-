from pynput.keyboard import Key, Controller
import keyboard
import speech_recognition as sr
import sys

keyboardPresser = Controller()
r = sr.Recognizer()

STOP_LOOPING = False
def triggerCommand(command):
    if command == 'objection':
        keyboardPresser.press('a')
    elif command == 'press':
        keyboardPresser.press('a')
    elif command == 'present':
        keyboardPresser.press('e')

def listen():
    global STOP_LOOPING
    STOP_LOOPING = False

    while True:
        if keyboard.is_pressed('w'):  # f
            print('detected w')
            while not STOP_LOOPING:
                print(STOP_LOOPING)
                with sr.Microphone() as source:
                    # read the audio data from the default microphone
                    audio_data = r.record(source, duration=3)
                    print("Recognizing...")
                    # convert speech to text
                    try:
                        text = r.recognize_google(audio_data)
                        print(text)
                        if text == 'stop' or text == 'exit':
                            print("Please exit")
                            sys.exit()
                        triggerCommand(text)
                        STOP_LOOPING = True
                    except sr.UnknownValueError:
                        print('No Voice Detected')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listen()

