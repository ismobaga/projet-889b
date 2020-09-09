from naive import naive
from greedy import greedy
from genetic import genetic
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('qt5agg')
import data

import statistics
import sys
import time
import numpy as np


class Benchmark:
    @staticmethod
    def run(function):
        timings = [] 
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(
                    1 + i, mean,
                    statistics.stdev(timings, mean) if i > 1 else 0))


def save(fig, filename, format):
    fig.savefig(f'{filename}.{format}', format=format)
def plot(x, y, title=""):
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()

    fig.show()

    fig.savefig("test.png")

l = 0.35
D = np.array([5, 10, 15, 20])
for m in (1, 4):
    greedyData = []
    geneticData = []
    naiveData = []
    for d in D:
        if l < 0.40:
            n = naive(data.get(l,m, delai=d))
            naiveData += [n]
        g = greedy(data.get(l, m,  delai=d))
        greedyData += [g]
        ge = genetic(data.get(l, m, delai=d))
        geneticData += [ge]

    naiveData =np.array(naiveData)
    greedyData =np.array(greedyData)
    geneticData =np.array(geneticData)

    fig, ax = plt.subplots()
    ax.plot(D[:len(naiveData)], naiveData[:,0], label='Naive')
    ax.plot(D[:len(greedyData)], greedyData[:,0], label='Glouton')
    ax.plot(D[:len(geneticData)], geneticData[:,0], label="Génétique")
    ax.set(xlabel='Le delai maximum [time slot]', ylabel='énergie [J]',
        title="Consommation d'énergie vs Le delai")
    legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
    save(fig, f'EvsD{m}', "eps")




