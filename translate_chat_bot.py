# Importing the required libraries
from difflib import get_close_matches
from textblob import TextBlob
from googletrans import Translator


# Function to get the closest match for the user's question from the knowledge base
def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)  # Match threshold is 60%

    if matches:
        return matches[0]


# Main chatbot function to interact with the user
def chatbot(knowledge: dict):
    while True:
        user_input: str = input('You : ')

        # Find the best match for the user input
        best_match: str | None = get_best_match(user_input, knowledge)

        # Respond based on the knowledge base
        if answer := knowledge.get(best_match):
            print(f'Chatbot : {answer}')
