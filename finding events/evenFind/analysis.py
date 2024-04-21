from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def sentence_similarity(sentence1, sentence2):
    # Tokenization
    words1 = word_tokenize(sentence1)
    words2 = word_tokenize(sentence2)
    
    # Remove stopwords
    words1 = [word.lower() for word in words1 if word.isalnum() and word.lower() not in stopwords.words('english')]
    words2 = [word.lower() for word in words2 if word.isalnum() and word.lower() not in stopwords.words('english')]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words1 = [lemmatizer.lemmatize(word, wordnet.VERB) for word in words1]
    words2 = [lemmatizer.lemmatize(word, wordnet.VERB) for word in words2]

    # Calculate similarity
    common_words = set(words1).intersection(set(words2))
    similarity = len(common_words) / (len(set(words1)) + len(set(words2)))

    return similarity