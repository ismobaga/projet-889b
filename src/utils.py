"""
a est l'instant d'arriver de la requête 
d est le dernier instant que peut tolérer la requête 
m est l'identifiant du contenu (message) demandé par la requête  
e l'énergie nécessaire pour répondre à la requête 


Une partition contient un ou plusieurs envois
"""



import numpy as np


def energy(reqs):
    """Maximum d'energy d'un ensemble de requetes

    Args:
        reqs ([](a, d, m, e)): Un ensmble de requetes

    Returns:
        [float]: L'energie qui prends pour envoye cet ensemble
    """
    return np.max(reqs[:,3])




def delais(reqs):
    """Le delais pour servier d'un ensemble de requetes

    Args:
        reqs ([][(a, d, m, e)]): Un ensmble de requetes

    Returns:
        [float]: Une accumation de delais pour l'nnvoie de des requetes
    """
    def exceed_by(req, t_envoie):
        ex = t_envoie - req[1]
        return ex if ex > 0 else 0
    # TransmisTransmission ne peut avoir que que si tous les
    # requêtes sont arrivées 
    t_envoie = np.max(reqs[:,0])
    acc =0
    for r in reqs:
        acc = acc + exceed_by(r, t_envoie)
    return acc


def partition(collection):
    """Une generateur de toutes les combinaisons d'un ensemble
    Source : https://stackoverflow.com/a/30134039 

    Args:
        collection ([]): [description]

    Yields:
        [type]: une combinaison
    """
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller



def is_partition_ok(p):
    """Verifier si un envoie reponds qu'a un seul contenu
    La condition qu'un seul meessage a la fois

    Args:
        p ([][](a, d, m, e))): une partition, un ensemble d'envoie

    Returns:
        [bool]: 
    """
    chck = []
    for envoie in p:
        un = np.array(envoie)
        # Un seul contenu par envoie
        chck += [len(np.unique(un[:,2]))==1]
    
    # Tous les envoies doivent etre cool
    return all(chck)



def ok_partition(entries):
    """Generer et filtrer les partitions
    seulement les partitions qui respecte un seul envoie a la fois 

    Args:
        entries ([](a, d, m, e))): L'ensemble des demande

    Yields:
        [type]: une bonne partition
    """
    for p in partition(entries):
        if is_partition_ok(p):
            yield p
    return