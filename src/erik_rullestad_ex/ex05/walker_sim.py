# -*- coding: utf-8 -*-

__author__ = 'Erik Rullestad'
__email__ = 'erikrull@nmbu.no'

import random


class Walker:

    def __init__(self, x0, h):
        self.position = x0
        self.home = h
        self.steps = 0

    def move(self):
        num = random.random()
        if num < 0.5:
            self.position += 1
        else:
            self.position -= 1

        self.steps += 1

    def is_at_home(self):
        return self.position == self.home

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps


class Simulation:
    def __init__(self, start, home, seed):
        """
        Initialise the simulation
        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        wlk = Walker(self.start, self.home)
        while wlk.is_at_home() is not True:
            wlk.move()
        num_steps = wlk.get_steps()

        return num_steps

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        global num_steps
        path_lengths = []
        for walk in range(num_walks):
            num_steps = self.single_walk()
        path_lengths.append(num_steps)

        return path_lengths


if __name__ == '__main__':

    seed_nums = [12345, 54321]
    for seed_num in seed_nums:
        print('\n\nSeed number is now:' '\033[1m' + f' {seed_num}')
        start_pos = 0
        home_pos = 10
        sim = Simulation(start_pos, home_pos, seed_num)
        for i in range(2):
            print('\033[1m' + f'''
            Number of steps in 20 walks with start = {start_pos} 
            and home = {home_pos}:''''\033[0m' + f'\n{sim.run_simulation(20)}'
                  )

        start_pos = 10
        home_pos = 0
        sim = Simulation(start_pos, home_pos, seed_num)
        print('\033[1m' + f'''
        Number of steps in 20 walks with start = {start_pos} 
        and home = {home_pos}:''''\033[0m' + f'\n{sim.run_simulation(20)}'
              )
