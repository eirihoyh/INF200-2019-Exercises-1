from collections import Counter
from math import log2


def letter_freq(txt):
    txt = txt.lower()
    return Counter(txt)


def entropy(message):
    frequencies = letter_freq(message)
    number_of_characters = len(message)
    result = 0
    for value in frequencies.values():
        number = value/number_of_characters * log2(value/number_of_characters)
        result += number
    total_entropy = -result
    return total_entropy


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
