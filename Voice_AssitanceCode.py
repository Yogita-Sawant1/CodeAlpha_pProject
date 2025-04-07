import speech_recognition as sr
import pyttsx3
import openai
import datetime
import webbrowser

# Set up OpenAI API (replace 'your-api-key' with your actual API key)
openai.api_key = "your-api-key"

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        print("Could not request results, please check your internet connection.")
        return ""

def ask_openai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.AuthenticationError:
        return "Invalid API key. Please check your OpenAI credentials."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def execute_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"Searching for {search_query}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        response = ask_openai(command)
        speak(response)

if __name__ == "__main__":
    speak("Hello, how can I assist you today?")
    while True:
        user_command = listen()
        if user_command:
            execute_command(user_command)
