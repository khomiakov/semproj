import numpy as np
import matplotlib.pyplot as plt
from Constants import *


class Plot1:
    def __init__(self):
        self.x_f1 = np.arange(1, 3600, 1 / 60)
        self.zzz = None

    def f1(self, alpha):
        self.zzz = None
        return - alpha / 2 + np.power((alpha / 2) ** 2 + 4 * c.m * c.g / c.d / (c.c ** 2), 1 / 2)

    def draw_plot(self):
        plt.figure(figsize=(20, 7))
        plt.plot(self.x_f1, self.f1(self.x_f1 * np.pi / 180 / 3600) * 180 * 3600 / np.pi, label=r'$f(a)$')
        plt.xlabel(r'$m(solar masses)$', fontsize=14)
        plt.ylabel(r'$f(arc seconds)$', fontsize=14)
        plt.grid(True)
        plt.legend(loc='best', fontsize=12)
        plt.show()


class Plot2:
    def __init__(self):
        self.x_f2 = np.arange(1, 10000, 1)
        self.zzz = None

    def f2(self, m):
        self.zzz = None
        alpha = np.arctan(c.r_bh_screen / c.s)
        return - alpha / 2 + np.power((alpha / 2) ** 2 + 4 * m * c.g / c.d / (c.c ** 2), 1 / 2)

    def draw_plot(self):
        plt.figure(figsize=(20, 7))
        plt.plot(self.x_f2, self.f2(self.x_f2 * c.m) * 180 * 3600 / np.pi, label=r'$f(m)$')
        plt.xlabel(r'$a(arc seconds)$', fontsize=14)
        plt.ylabel(r'$f(arc seconds)$', fontsize=14)
        plt.grid(True)
        plt.legend(loc='best', fontsize=12)
        plt.show()


class Plot3:
    def __init__(self):
        self.x_f3 = np.arange(1, 1000, 1)
        self.zzz = None

    def f3(self, d):
        alpha = np.arctan(c.r_bh_screen / c.s)
        self.zzz = None
        return - alpha / 2 + np.power((alpha / 2) ** 2 + 4 * c.m * c.g / d / (c.c ** 2), 1 / 2)

    def draw_plot(self):
        plt.figure(figsize=(20, 7))
        plt.plot(self.x_f3, self.f3(self.x_f3 * c.d) * 180 * 3600 / np.pi, label=r'$f(d)$')
        plt.xlabel(r'$a.u.$', fontsize=14)
        plt.ylabel(r'$f(arc seconds)$', fontsize=14)
        plt.grid(True)
        plt.legend(loc='best', fontsize=12)
        plt.show()
