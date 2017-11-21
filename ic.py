import string
import processing
import freq_analysis as fa
from sys import maxsize
from const import EN_IC


def _ic(letter_counts):
    numerator = sum([letter_counts[l]*(letter_counts[l]-1) for l in string.ascii_uppercase])
    text_size = sum(occurrences for occurrences in letter_counts.values())
    denominator = text_size*(text_size-1)
    return numerator/denominator


def find_key_length(cyphertext, max_key_len):
    min_diff = maxsize
    key_len = 0
    for candidate_length in range(1, max_key_len + 1):
        groups = processing.get_blocks(text=cyphertext, size=candidate_length)
        columns = processing.get_columns(groups)
        ics = [_ic(letter_counts=fa.get_letter_counts(text=column)) for column in columns]
        delta_bar_ic = sum(ics) / len(ics)
        if EN_IC-delta_bar_ic < min_diff:
            min_diff = EN_IC-delta_bar_ic
            key_len = candidate_length
        print('KEY_LENGTH: ' + str(candidate_length) + '\n')
        print('IC by column: '+str(ics))
        print('delta bar IC: '+str(delta_bar_ic)+'\n')
    return key_len
