
import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random


chatStr = ""


def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr = f"Mudit: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["text"])

    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    # with open(f"Openai/prompt- {random.randint(1,23423423423)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
       f.write(text)



def ai(prompt):
    global chatStr
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *********\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside a try catch block
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    #with open(f"Openai/prompt- {random.randint(1,23423423423)}","w") as f:
    with open(f"Openai/{''.join(prompt[0:20])}.txt", "w") as f:
        f.write(text)


def say(text):
    os.system(f"say {text}")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occured. Sorry from Jarvis"

def country_cap():

    # Dictionary of country names
    countries = {
        "Afghanistan": "Kabul",
        "Argentina": "Buenos Aires",
        "Australia": "Canberra",
        "Brazil": "Brasilia",
        "Canada": "Ottawa",
        "China": "Beijing",
        "Egypt": "Cairo",
        "France": "Paris",
        "Germany": "Berlin",
        "India": "New Delhi",
        "Italy": "Rome",
        "Japan": "Tokyo",
        "Mexico": "Mexico City",
        "Russia": "Moscow",
        "South Africa": "Pretoria",
        "United Kingdom": "London",
        "United States": "Washington, D.C.",
    }

    def quiz_country():
        # Select a random country from the dictionary
        country = random.choice(list(countries.keys()))

        # Prompt the user to guess the capital of the country
        print("What is the capital of", country, "?")
        say(f'What is the capital of {country} ?')
        user_answer = input("Enter your answer: ")

        # Check if the answer is correct
        if user_answer.lower() == countries[country].lower():
            print("Correct!")
            say("Correct!")
        else:
            print("Incorrect! The capital of", country, "is", countries[country])
            say(f'Incorrect! The capital of {country} is {countries[country]}')


    # Main program loop
    while True:
        print("\nWelcome to the Country Capitals Quiz!")
        print("Type 'exit' to quit the quiz.\n")

        # Call the quiz function
        quiz_country()

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes=y/no=n): ")
        if play_again.lower() == "n" or play_again.lower() == "exit":
          break


if __name__ == '__main__':
    print('Personal A.I assistant')
    say("Hi")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song

        if "open music" in query:
            musicPath = "/Users/muditjoshi/Downloads/l_theme_death_note.mp3"
            os.system(f"open {musicPath}")

        elif "time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} {minute}")

        elif "country name".lower() in query.lower():
            country_cap()

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open spotify".lower() in query.lower():
            os.system(f"open /Applications/Spotify.app")

        elif "artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif "Jarvis quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""


        else:
            print("Chatting...")
            chat(query)

# say(query)


