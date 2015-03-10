import random

__author__ = 'niklas'

import numpy as np
import math


def generate_socio_matrix(g, delta):
    """
    Generates random socio matrix
    :param g: dimensionality
    :param delta: density
    :return: socio matrix
    """
    # delta = L / (g(g-1)/2)
    # <=> L = delta * ((g^2 -g)/2)
    # must be integer, thus floor it
    nr_links = math.floor(delta * ((g**2 - g)/2))
    print("nr links:", nr_links)
    s_matrix = np.zeros((g, g))
    random.seed(42)
    for _ in range(nr_links):
        c_x, c_y = (0, 0)
        while (c_x == c_y) or (s_matrix[c_x][c_y] == 1):
            #print("previous candidate ", c_x, c_y, "unfit, retrying")
            #print("current matrix:")
            #print(s_matrix)
            c_x, c_y = random.randint(0, g-1), random.randint(0, g-1)
        s_matrix[c_x][c_y] = 1
    return s_matrix


if __name__ == "__main__":
    # 1 generate socio matrix gxg with density Delta
    g = 10
    delta = 0.4
    s_matrix = generate_socio_matrix(g, delta)
    print("socio matrix:")
    print(s_matrix)