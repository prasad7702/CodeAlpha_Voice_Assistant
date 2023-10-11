import speech_recognition as sr
from gtts import gTTS
import pygame

recognizer = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print("User said: " + command)
            return command
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results. Please check your internet connection.")
    return ""

def main():
    speak("Hello! i'm an intern in codealpha")
    while True:
        command = take_command()
        if "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
