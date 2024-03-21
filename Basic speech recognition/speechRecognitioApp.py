import speech_recognition as sr

# Function to record audio and perform speech recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 5 seconds...")
        audio = recognizer.listen(source, timeout=1)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Main execution
if __name__ == "__main__":
    recognize_speech()
