#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os

RESIDUES = [1,7,11,13,17,19,23,29]

def extract_sequence(M):
    """Construit une séquence linéaire à partir des diagonales décalées."""
    seq = []
    n = M.shape[0]
    for shift in range(n):
        diag = np.diag(M, k=shift)
        seq.extend(diag.tolist())
    return np.array(seq)

def autocorrelation(x):
    """Autocorrélation normalisée."""
    x = x - np.mean(x)
    corr = np.correlate(x, x, mode='full')
    corr = corr[corr.size//2:]
    return corr / corr[0] if corr[0] != 0 else corr

def period9_score(M):
    seq = extract_sequence(M)
    corr = autocorrelation(seq)
    if len(corr) > 9:
        return corr[9]
    return 0.0

def main():
    print("=== Détection automatique de la période 9 ===")

    k_list = list(range(2, 62, 2))

    # Global
    M_global = np.load("data/M_all_gap6.npy")
    score_global = period9_score(M_global)
    print(f"Global : score période 9 = {score_global:.4f}")

    # SG(k)
    for k in k_list:
        path = f"data/M_SG{k}_gap6.npy"
        if not os.path.exists(path):
            continue
        M = np.load(path)
        score = period9_score(M)
        print(f"SG({k}) : score période 9 = {score:.4f}")

    print("\nDétection période 9 terminée.")


    with open("period9_scores.txt", "w") as f:
        f.write(f"Global = {score_global}\n")
        for k in k_list:
            f.write(f"SG({k}) = {period9_score(np.load(f'data/M_SG{k}_gap6.npy'))}\n")
    


if __name__ == "__main__":
    main()
