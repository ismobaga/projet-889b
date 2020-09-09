import numpy as np
import csv
def reader(filename):
    output = []
    with open(filename) as f:
    #     output = [float(s) for line in f.readlines() for s in line[:-1].split(',')]
        rdr = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
        for row in rdr: # each row is a list
            output.append(row)
    return output
def writer(en, filename):
    np.savetxt(filename, en, delimiter=",")

def genReqs(l=2, de=5, m=4, T=20, seedv=1):
    from random import choices, randint, uniform, seed
    seed(seedv)
    np.random.seed(seedv)

    reqs = []

    for t, s in enumerate(np.random.poisson(l, T)):
        for i in range(s):

            a = t
            d = a + randint(1, de)
            reqs += [[
                a,
                d,
                choices(range(1,  m+1))[0],
                1/uniform(1.0, 2.0000001)
            ]]
    return reqs

def get(lam, m=4, delai=5):
    filename = "./data/%.2f-%d-%d.csv"%(lam, m, delai)
    return reader(filename)

def generate(m=4, delai=5):
    en = genReqs(l=0.30, m=m, seedv=10)
    filename = "./data/%.2f-%d-%d.csv"%(0.30, m, delai)
    writer(en, filename)

    en = genReqs(l=0.30, m=m, seedv=10)
    filename = "./data/%.2f-%d-%d.csv"%(0.35, m, delai)
    writer(en, filename)
    for l in np.arange(0.25, 5.001, 0.20):
        en = genReqs(l=l, m=m, seedv=10)
        filename = "./data/%.2f-%d-%d.csv"%(l, m, delai)
        writer(en, filename)


if __name__ == "__main__":
    for d in [5, 10, 15, 20]:
        generate(m=1, delai=d)
        generate(m=4, delai=d)
    