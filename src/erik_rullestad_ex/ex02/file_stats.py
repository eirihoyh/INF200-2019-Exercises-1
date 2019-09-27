from collections import Counter


def char_counts(textfilename):
    with open(textfilename, 'r', encoding='utf-8') as f:
        string = f.read().replace('\n', '')
        code_points = [ord(symbol) for symbol in string]
        result = Counter(code_points)
    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
