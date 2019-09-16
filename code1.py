import numpy as np

x = np.arange(-7, 7, 0.01)

def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma * 2)
    return p * np.exp(-0.5 / sigma ** 2 * (x - mu)**2)
