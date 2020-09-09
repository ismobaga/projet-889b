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
    fig.savefig(f'rapport/{filename}.{format}', format=format)

l = 0.45

lam = np.arange(0.25, 3.001, 0.20)
lam =  np.insert(lam, 1, [0.30, 0.35])

for m in (1, 4):
    greedyData = []
    geneticData = []
    naiveData = []
    for l in lam:
        if l < 0.40:
            n = naive(data.get(l))
            naiveData += [n]
        g = greedy(data.get(l, m))
        greedyData += [g]
        ge = genetic(data.get(l, m))
        geneticData += [ge]
        # print(g)
        # print(ge)

    naiveData =np.array(naiveData)
    greedyData =np.array(greedyData)
    geneticData =np.array(geneticData)

    # Energie vs Lambda
    fig, ax = plt.subplots()
    ax.plot(lam[:len(naiveData)], naiveData[:,0], label='Naive')
    ax.plot(lam[:len(greedyData)], greedyData[:,0], label='Glouton')
    ax.plot(lam[:len(geneticData)], geneticData[:,0], label="Génétique")
    ax.set(xlabel='La charge du système [requetes / time slot]', ylabel='énergie [J]',
        title="Consommation d'énergie vs La charge du système")
    legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
    save(fig, f'EvsL{m}', "eps")

    # Delais vs Lambda
    fig, ax = plt.subplots()
    ax.plot(lam[:len(naiveData)], naiveData[:,1], label='Naive')
    ax.plot(lam[:len(greedyData)], greedyData[:,1], label='Glouton')
    ax.plot(lam[:len(geneticData)], geneticData[:,1], label="Génétique")
    ax.set(ylabel='Retard [ms]', xlabel='La charge du système',
        title="Pénalité de retard vs La charge du système")
    legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')

    save(fig, f'DvsL{m}', "eps")



