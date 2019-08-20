from .words import WORDSLIST
import unidecode


def parse(question):
    words = [word for word in question.split() if word not in WORDSLIST]
    for ind, word in enumerate(words):
        word = unidecode.unidecode(word)
        words[ind] = word
    return words

