# -*- coding: utf-8 -*-

__author__ = 'Erik Rullestad'
__email__ = 'erikrull@nmbu.no'


class LCGRand:
    # This equation is taken from the exercise04 description
    A = 7**5
    M = 2**31-1

    def __init__(self, seed):
        self.r = [seed]

    def rand(self):
        self.r.append(self.r[-1] * self.A % self.M)
        return self.r[-1]


class ListRand:
    def __init__(self, num_list):
        self.num_list = num_list
        self.i = 0

    def rand(self):
        if self.i >= len(self.num_list):
            raise RuntimeError(
                'Last number of list has already been delivered'
            )

        rand_num = self.num_list[self.i]
        self.i += 1
        return rand_num


if __name__ == '__main__':
    seed_num = 131
    lgr = LCGRand(seed_num)
    print('\nPrinting from the LGRand-class:')
    for index in range(5):
        print(lgr.rand())

    print('\n')
    nums = [77, 3, 654, 17, 15, 3485, 65, 12, 854]
    lr = ListRand(nums)
    print('Printing from the ListRand-class:')
    for index in range(len(nums)):
        print(lr.rand())

    print('\033[1m' + '''\n\nTo check that it raises a runtime error when all 
numbers of the list have been delivered, i call the 
rand()-method from the ListRand-class once more:
    ''')
    try:
        print(lr.rand())
    except RuntimeError as err:
        print('\033[0m' + '\033[32m' + 'Runtime error traceback:', err)
