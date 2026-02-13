#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os

RESIDUES = [1,7,11,13,17,19,23,29]
IDX = {r:i for i,r in enumerate(RESIDUES)}

# Définition des orbites du cycle sexy mod 30
SEXY_ORBITS = [
    [(1,7), (7,13), (13,19), (19,25), (25,1)],   # orbite 1 (mod 30)
    [(11,17), (17,23), (23,29), (29,5), (5,11)]  # orbite 2 (mod 30)
]

def load_matrix(path):
    if not os.path.exists(path):
        return None
    return np.load(path)

def count_orbit_activity(M):
    """Compte combien de transitions tombent dans chaque orbite sexy."""
    if M is None:
        return [0,0]

    counts = [0,0]

    for k, orbit in enumerate(SEXY_ORBITS):
        for (a,b) in orbit:
            if a in IDX and b in IDX:
                i = IDX[a]
                j = IDX[b]
                counts[k] += M[i,j]
    return counts

def main():
    gaps = [6]  # on analyse les orbites sexy
    k_list = [2,4,6,8,10,12,14,16,18,20,22,24]

    print("=== Analyse des orbites du cube30 ===")

    # Global
    M_global = load_matrix("data/M_all_gap6.npy")
    global_orbits = count_orbit_activity(M_global)
    print(f"Global : orbite A = {global_orbits[0]}, orbite B = {global_orbits[1]}")

    # SG(k)
    for k in k_list:
        M = load_matrix(f"data/M_SG{k}_gap6.npy")
        if M is None:
            continue
        counts = count_orbit_activity(M)
        print(f"SG({k}) : orbite A = {counts[0]}, orbite B = {counts[1]}")

    print("\nAnalyse des orbites terminée.")

if __name__ == "__main__":
    main()
