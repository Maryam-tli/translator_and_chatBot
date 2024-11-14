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


