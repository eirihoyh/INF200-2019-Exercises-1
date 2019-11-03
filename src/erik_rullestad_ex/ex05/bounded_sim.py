# -*- coding: utf-8 -*-

__author__ = 'Erik Rullestad'
__email__ = 'erikrull@nmbu.no'


from src.erik_rullestad_ex.ex05.walker_sim import Simulation, Walker


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        if (self.get_position() is not
                self.left_limit - 1 or self.right_limit + 1):

            if self.get_position() is self.left_limit:
                self.position += 1
                self.steps += 1

            elif self.get_position() is self.right_limit:
                self.position -= 1
                self.steps += 1

            else:
                super().move()


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):
        wlk = BoundedWalker(self.start, self.home,
                            self.left_limit, self.right_limit)
        while not wlk.is_at_home():
            wlk.move()
        num_steps = wlk.get_steps()

        return num_steps


if __name__ == '__main__':

    seed_num = 1234
    start_pos = 0
    home_pos = 20
    right_lim = 20
    left_lim = -10
    sim = BoundedSimulation(start_pos, home_pos, seed_num, left_lim, right_lim)
    print('\033[1m' + f'''
Number of steps in 20 walks with start = {start_pos} and home = {home_pos}:''' 
          '\033[0m' + f'\n{sim.run_simulation(20)}')
