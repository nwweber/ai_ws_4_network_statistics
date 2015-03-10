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
            c_x, c_y = random.randint(0, g-1), random.randint(0, g-1)
        s_matrix[c_x][c_y] = 1
    return s_matrix


def generate_socio_bernoulli(g, p):
    """
    generate socio matrix, tie determined by bernoulli(p)
    :param g: matrix size
    :param p: bernoulli parameter
    :return:
    """
    random.seed(42)
    s_matrix = np.zeros((g, g))
    for row in range(g):
        for col in range(row):
            rand = random.random()
            if rand <= p:
                s_matrix[row][col] = 1
                s_matrix[col][row] = 1
    return s_matrix


def plot_matrix(s_matrix):
    import matplotlib as plt
    import networkx as nx
    nx.draw(s_matrix)


if __name__ == "__main__":
    # 1 generate socio matrix gxg with density Delta
    g = 10
    delta = 0.4
    s_matrix = generate_socio_matrix(g, delta)
    print("socio matrix:")
    print(s_matrix)
    # 2 generate random socio matrix, each tie is drawn from Bernoulli 0/1
    p = 0.5
    s_bern_matrix = generate_socio_bernoulli(g, p)
    print("bernoulli matrix:")
    print(s_bern_matrix)
    # 3 plot graph for g = 20
    print("plotting matrix g=20")
    plot_matrix(generate_socio_bernoulli(20, 0.4))