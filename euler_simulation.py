from random import random
from statistics import mean


def sum_to_one():
    x = 0
    count = 0
    while x < 1:
        count += 1
        x += random()
    return count


def mean_of_x_simulations(x):
    return mean([sum_to_one() for i in range(x)])


if __name__ == '__main__':
    print('Eulers number simulation')
    for i in range(1, 50):
        print(mean_of_x_simulations(i))