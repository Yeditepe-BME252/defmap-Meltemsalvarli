# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

def plotgrid(map_func, xlim=(-3,3), ylim=(-3,3), grid_size=21):

    x_vals = np.linspace(xlim[0], xlim[1], grid_size)
    y_vals = np.linspace(ylim[0], ylim[1], grid_size)

    plt.figure(figsize=(7,7))

    # vertical lines
    y = np.linspace(ylim[0], ylim[1], 400)

    for x0 in x_vals:

        x = x0*np.ones_like(y)

        X, Y = map_func(x, y)

        plt.plot(X, Y, color='steelblue', linewidth=1)

    # horizontal lines
    x = np.linspace(xlim[0], xlim[1], 400)

    for y0 in y_vals:

        y = y0*np.ones_like(x)

        X, Y = map_func(x, y)

        plt.plot(X, Y, color='steelblue', linewidth=1)

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.xlim(xlim)
    plt.ylim(ylim)

    plt.xlabel('a1')
    plt.ylabel('a2')

    plt.gca().set_aspect('equal')

    plt.show()


def case_26(x, y):

    return x - 0.20*np.exp(-0.6*y**2), y


plotgrid(case_26)
