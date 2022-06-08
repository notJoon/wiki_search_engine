from typing import List 

import re 
import string
from nltk.stem import PorterStemmer

## Most common words in English and "wikipedia"
STOPWORDS = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
                'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
                'do', 'at', 'this', 'but', 'his', 'by', 'from', 'wikipedia'])

PUNCTUATION = re.compile(f'[{re.escape(string.punctuation)}]')


def tokenize(text: str) -> List[str]:
    return text.split()

def to_lowercase(tokens: List[str]) -> List[str]:
    return [token.lower() for token in tokens]

def punctuation_filter(tokens: List[str]) -> List[str]:
    return [PUNCTUATION.sub('', token) for token in tokens]

def stopword_filter(tokens: List[str]) -> List[str]:
    return [token for token in tokens if token not in STOPWORDS]

# "An algorithm for suffix stripping" (Porter et. al., 1980) 
def stem_filter(tokens): 
    return PorterStemmer(tokens)

def processing(text: str) -> List[str]:
    tokens = tokenize(text)
    tokens = to_lowercase(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = stem_filter(tokens)

    return [token for token in tokens if token]