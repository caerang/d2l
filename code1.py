import numpy as np
import math
from matplotlib import pyplot as plt


def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma * 2)
    return p * np.exp(-0.5 / sigma ** 2 * (x - mu)**2)


def plot(X, Y=None, xlabel=None, ylabel=None, legend=[], xlim=None,
         ylim=None, xscale='linear', yscale='linear', fmts=None,
         figsize=(3.5, 2.5), axes=None):

    plt.rcParams['figure.figsize'] = figsize
    axes = axes if axes else plt.gca()
    
    if not hasattr(X[0], '__len__'): X = [X]
    if Y is None: X, Y = [[]]*len(X), X
    if not hasattr(Y[0], '__len__'): Y = [Y]
    if len(X) != len(Y): X = X * len(Y)
    if not fmts: fmts = ['-'] * len(X)
    axes.cla()
    for x, y, fmt in zip(X, Y, fmts):
        if len(x):
            axes.plot(x, y, fmt)
        else:
            axes.plot(y, fmt)
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)


def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend: axes.legend(legend)
    axes.grid()


if __name__ == '__main__':
    x = np.arange(-7, 7, 0.01)
    parameters = [(0,1), (0,2), (3,1)]
    plot(x, [normal(x, mu, sigma) for mu, sigma in parameters],
         xlabel='x', ylabel='p(x)', figsize=(4.5, 2.5),
         legend=['mean {}, var {}'.format(mu, sigma) for mu, sigma in parameters])
