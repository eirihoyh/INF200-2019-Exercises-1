from collections import Counter


def letter_freq(txt):
    txt = txt.lower()
    return Counter(txt)


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')
    frequencies = letter_freq(text).items()
    for letter, count in sorted(frequencies):
        print('{:3}{:10}'.format(letter, count))
