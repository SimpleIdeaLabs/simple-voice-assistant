from datetime import datetime
from re import T
import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia

def talk(text):
  speech_engine = pyttsx3.init()
  voices = speech_engine.getProperty('voices')
  speech_engine.setProperty('voice', voices[7].id)
  speech_engine.say(text)
  speech_engine.runAndWait()

def take_command():
  listener = sr.Recognizer()
  try:
    with sr.Microphone() as source:
      print('Listening...')
      voice = listener.listen(source)
      command = listener.recognize_google(voice)
      command = command.lower()
      print(command)
      if "kevin" in command:
        return command.replace("kevin", "")
      return "unrecognized"
  except Exception as e:
    print(e)

def run_kevin():
  while True:
    try:
      command = take_command()
      if "play" in command:
        talk(command + " now.")
        pywhatkit.playonyt(command)
      elif "time" in command:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        talk("Its " + current_time + " as of now.")
      elif "wikipedia" in command:
        summary = wikipedia.summary(command.replace("wikipedia", ""))
        talk(summary)
      elif "exit" in command:
        talk("Got to go now. Bye")
        exit(0)
      else:
        talk("Did not get that. Say it again.")
        print("Unrecognized command")
    except Exception as e:
      print(e)

def main():
  run_kevin()

if __name__ == "__main__":
  main()
