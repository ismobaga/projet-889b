from utils import *


def is_group_ok(g):
  return  np.min(g[:,1]) > np.max(g[:,0])

def greedy(entries):
    """

    Args:
        entries ([](a, d, m, e))): L'ensemble des demandes

    Returns:
        [float]: L'energie 
        [float]: Le delais 
    """
    tries = np.array(entries)
    e = []
    d = []
    while(len(tries)):
    
        max_ei = np.argmax(tries[:,0])
        first = tries[max_ei]
        g = np.array([first])
        # print(first, g)
        # print(max_ei, tries)
        tries = np.delete(tries, max_ei, axis=0)
        for r in tries:
            # print(r)
            if r[2] == g[0][2]:
                if is_group_ok(np.append(g, [r], axis=0)):
                    g = np.append(g, [r], axis=0)
        e += [energy(np.array(g))]
        d += [delais(np.array(g))]
    return sum(e), sum(d)
