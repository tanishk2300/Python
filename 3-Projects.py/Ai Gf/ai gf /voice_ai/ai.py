import speech_recognition as sr
import pyttsx3
import time
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")
chat_history = [
    {"role": "system", "content": "You are a caring AI girlfriend who speaks softly and listens patiently."}
]


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_history
)

reply = response.choices[0].message.content


# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    return r.recognize_google(audio)

# Start assistant
speak("Hello beta .")

while True:
    try:
        user_input = listen()
        chat_history.append({"role": "user", "content": user_input})
        # chat_history.append({"role": "assistant", "content": reply})

        print("You:", user_input)

        if user_input.lower() in ["exit", "stop", "bye"]:
            speak("Okay, talk to you later.")
            break

        # TEMP RESPONSE (brain will be added next)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a calm, caring assistant who speaks politely."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": reply})

        print("AI:", reply)
        speak(reply)

    except Exception as e:
        print("Error:", e)
        speak("Sorry, I didn't understand. Please repeat.")

