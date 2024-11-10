import random

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
    user_answer = input("Enter your answer: ")

    # Check if the answer is correct
    if user_answer.lower() == countries[country].lower():
        print("Correct!")
    else:
        print("Incorrect! The capital of", country, "is", countries[country])

# Main program loop
while True:
    print("\nWelcome to the Country Capitals Quiz!")
    print("Type 'exit' to quit the quiz.\n")

    # Call the quiz function
    quiz_country()

    # Ask the user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "no" or play_again.lower() == "exit":
        break
