import numpy as np
import matplotlib.pyplot as plt


def analyze2(filename):
    '''load a file and plot the mean, max, and min of the data through time '''

    data = np.loadtxt(filename, delimiter=',')

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(np.mean(data, axis=0), label="mean")
    ax.plot(np.max(data, axis=0), label="max")
    ax.plot(np.min(data, axis=0), label="min")
    
    ax.set_ylabel('Inflammation')
    ax.set_xlabel('Days')
    
    ax.legend()
