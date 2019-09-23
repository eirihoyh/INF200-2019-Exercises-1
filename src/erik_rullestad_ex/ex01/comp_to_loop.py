def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k ** 2)
    return squares


if __name__ == '__main__':
    num = 4
    if squares_by_comp(num) != squares_by_loop(num):
        print('ERROR!')
