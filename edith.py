import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime


# Create a recognizer instance
r = sr.Recognizer()

# Create a TTS engine instance
engine = pyttsx3.init()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # use the second voice

# Set the rate and volume
engine.setProperty('rate', 150)  # words per minute
engine.setProperty('volume', 0.5)  # range from 0 to 1

# Start the voice assistant
while True:
    # Listen for user input
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Convert speech to text
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)

        # Process the user's request
        if "play" in text.lower():
            query = text.lower().replace("play", "")
            pywhatkit.playonyt(query)

        elif "search" in text.lower():
            query = text.lower().replace("search", "")
            wikipedia.set_lang("en")  # set the language to English
            results = wikipedia.summary(query, sentences=2)
            engine.say(results)
            engine.runAndWait()

        elif "time" in text.lower():
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            engine.say("The current time is " + current_time)
            engine.runAndWait()

        elif "exit" in text.lower():
            engine.say("Goodbye!")
            engine.runAndWait()
            break

        else:
            engine.say("Sorry, I didn't understand what you said.")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


