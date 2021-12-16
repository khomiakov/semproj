import numpy as np
import matplotlib.pyplot as plt


class Constants:
    def __init__(self):
        """
        Здесь параметры чёрной дыры - параметра Солнца.
        """
        self.m = 1.989 * (10 ** 30)  # масса чёрной дыры
        self.c = 299792458  # скорость света
        self.g = 6.67408 * 10 ** (-11)  # гравитационная постоянная
        self.d = 149597870700  # расстояние до чёрной дыры
        self.width = 1000  # ширина экрана, условность
        self.x0 = self.width / 2  # координата x центра чёрной дыры на экране
        self.height = 500  # высота экрана, условность
        self.y0 = self.height / 2  # координата y центра чёрной дыры на экране
        self.s = 1500
        self.r_bh_screen = 50
        self.r_bh = 696340000


c = Constants()


def f1(alpha):
    return - alpha / 2 + np.power((alpha / 2) ** 2 + 4 * c.m * c.g / c.d / (c.c ** 2), 1 / 2)


def f2(m):
    alpha = np.arctan(c.r_bh_screen / c.s)
    return - alpha / 2 + np.power((alpha / 2) ** 2 + 4 * m * c.g / c.d / (c.c ** 2), 1 / 2)


def f3(d):
    alpha = np.arctan(c.r_bh_screen / c.s)
    return - alpha / 2 + np.power((alpha / 2) ** 2 + 4 * c.m * c.g / d / (c.c ** 2), 1 / 2)


x_f1 = np.arange(1, 3600, 1 / 60)
x_f2 = np.arange(1, 10000, 1)
x_f3 = np.arange(1, 1000, 1)

plt.figure(figsize=(20, 7))
plt.plot(x_f1, f1(x_f1 * np.pi / 180 / 3600) * 180 * 3600 / np.pi, label=r'$f(a)$')
plt.xlabel(r'$a(arc seconds)$', fontsize=14)
plt.ylabel(r'$f(arc seconds)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)

plt.figure(figsize=(20, 7))
plt.plot(x_f2, f2(x_f2 * c.m) * 180 * 3600 / np.pi, label=r'$f(m)$')
plt.xlabel(r'$m(solar masses)$', fontsize=14)
plt.ylabel(r'$f(arc seconds)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)

plt.figure(figsize=(20, 7))
plt.plot(x_f3, f3(x_f3 * c.d) * 180 * 3600 / np.pi, label=r'$f(d)$')
plt.xlabel(r'$a.u.$', fontsize=14)
plt.ylabel(r'$f(arc seconds)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.show()
