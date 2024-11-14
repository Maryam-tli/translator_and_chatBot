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

        elif user_input == ("can you translate?" or "can you translate again" or "please translate this text").lower():
            user_input = input("please Enter Your Text: ")
            text = TextBlob(user_input)
            translator = Translator()

            # Detect the language of the input text
            detected_language = translator.detect(text.string).lang
            print(f"Language detected: {detected_language}")

            # Translate based on the detected language
            if detected_language == 'fa':
                # Translate from Persian to English if input is in Persian
                translation = translator.translate(text.string, dest='en')
                print(f"Translated text (English): {translation.text}")
            elif detected_language == 'en':
                # Translate from English to Persian if input is in English
                translation = translator.translate(text.string, dest='fa')
                print(f"Translated text (Persian): {translation.text}")
            else:
                print("Your Input Text Is Not English or Persian.")

        else:
            print('Bot: I cannot understand...')


if __name__ == '__main__':
    brain: dict = {
        'hello': 'hey there!',
        'how are you': 'I am good, thanks',
        'what is your name': 'I am a chatbot',
        'what time is it ?': 'I don\'t have idea',
        'what can you do ?': 'I can answer the questions',
        'thank you': 'You\'re welcome',
        'bye': 'Goodbye! Have a great day!',
        'how old are you?': 'I don\'t age like humans!',
        'where are you from?': 'I live in the cloud.',
        'tell me a joke': 'Why don’t skeletons fight each other? They don’t have the guts!',
        'can you help with math?': 'Yes, I can help with basic math problems. What do you need help with?',
        'who are you': 'I am a friendly chatbot here to assist you!',
        'do you know programming?': 'Yes, I can provide you with information about programming concepts.',
        'what can you tell me about Python?': 'Python is a popular programming language known for its simplicity'
                                              ' and readability.',
        'how can I improve my English?': 'Practice daily, speak with native speakers if possible, '
                                         'and watch English media.',
        'can you tell me a story?': 'Once upon a time, in a land full of data...',
    }

    # Start the chatbot with the predefined knowledge base
    chatbot(knowledge=brain)
