from .words import WORDSLIST
import unicodedata


def parse(question):
    words = [word for word in question.split() if word not in WORDSLIST]
    for ind, word in enumerate(words):
        nfkd_form = unicodedata.normalize('NFKD', word)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        words[ind] = only_ascii
    return words

