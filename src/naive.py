from utils import *


def naive(entries):
    """

    Args:
        entries ([](a, d, m, e))): L'ensemble des demandes

    Returns:
        [float]: L'energie 
        [float]: Le delais 
    """
    energie = []
    delay = []
    h=0
    i = 1
    for p in ok_partition(entries):
        i+=1
        # print(i)
        e =[]
        d= []
        for envoie in p:
            e += [energy(np.array(envoie))]
            d += [delais(np.array(envoie))]
        energie += [sum(e)]
        delay += [sum(d)]
    i = np.argmin(energie)

    return energie[i], delay[i]