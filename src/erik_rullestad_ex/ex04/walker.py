# -*- coding: utf-8 -*-

__author__ = 'Erik Rullestad'
__email__ = 'erikrull@nmbu.no'


import random


class Walker:
    steps = 0

    def __init__(self, x0, h):
        self.position = x0
        self.home = h

    def move(self):
        num = random.random()
        if num < 0.5:
            self.position += 1
        else:
            self.position -= 1

        self.steps += 1

    def is_at_home(self):
        if self.position == self.home:
            return True
        else:
            return False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps


if __name__ == '__main__':
    distances = [1, 2, 5, 10, 20, 50, 100]

    random.seed(10)

    for distance in distances:
        path_lengths = []
        for simulation in range(5):
            start = random.randint(1, 100)
            home = start + (1 if random.randint(0, 1) == 0 else -1) * distance
            wlk = Walker(start, home)

            while wlk.is_at_home() is not True:
                wlk.move()
            num_steps = wlk.get_steps()
            path_lengths.append(num_steps)

        print(f'Distance: {distance:3d} -> Path lengths: {path_lengths}')
