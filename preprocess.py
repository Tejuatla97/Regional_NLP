import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from stopwords import stopwords_dict

def Charlie(text, language):

    language = language.lower()

    if language not in stopwords_dict:
        return "Language not supported"

    tokens = word_tokenize(text)

    filtered_words = []

    selected_stopwords = stopwords_dict[language]

    for word in tokens:

        if word not in selected_stopwords:

            filtered_words.append(word)

    return filtered_words