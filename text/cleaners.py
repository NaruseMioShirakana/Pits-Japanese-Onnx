import re
from text.japanese import clean_japanese
def none_cleaner(text):
    return text

def japanese_cleaners(text):
    text = clean_japanese(text)
    text = re.sub(r'([A-Za-z])$', r'\1.', text)
    return text