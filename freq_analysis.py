import processing
import string
from const import EN_REL_FREQ


def get_letter_counts(text):
    text_upper = text.upper()
    letter_counts = {}
    for index, letter in enumerate(string.ascii_uppercase):
        letter_counts[letter] = text_upper.count(letter)
    return letter_counts


def _get_letter_frequencies(text):
    letter_counts = get_letter_counts(text)
    frequencies = {letter: count/len(text) for letter, count in letter_counts.items()}
    return frequencies


def shift(text, amount):
    shifted = ''
    letters = string.ascii_uppercase
    for letter in text:
        shifted += letters[(letters.index(letter)-amount) % len(letters)]
    return shifted


def _corr(text, lf):
    return sum([(lf[letter]*EN_REL_FREQ[letter]) for letter in text])


def _find_key_letter(text, lf):
    key_letter = ''
    max_corr = 0
    for count, letter in enumerate(string.ascii_uppercase):
        shifted = shift(text=text, amount=count)
        corr = _corr(text=shifted, lf=lf)
        if corr > max_corr:
            max_corr = corr
            key_letter = letter
    return key_letter


def restore_key(cyphertext, key_len):
    key = ''
    blocks = processing.get_blocks(text=cyphertext, size=key_len)
    columns = processing.get_columns(blocks)
    frequencies = _get_letter_frequencies(text=cyphertext)
    for column in columns:
        key += _find_key_letter(text=column, lf=frequencies)
    return key
