#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from entropy_tools import analyze_matrix
import os

RESIDUES = [1,7,11,13,17,19,23,29]
IDX = {r:i for i,r in enumerate(RESIDUES)}

def sieve_primes(n):
    sieve = bytearray(b"\x01") * (n+1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            step = i
            start = i*i
            sieve[start:n+1:step] = b"\x00" * ((n - start)//step + 1)
    return [i for i in range(n+1) if sieve[i]]

def build_sg_families(primes, k_list):
    prime_set = set(primes)
    sg = {k: set() for k in k_list}
    for p in primes:
        for k in k_list:
            q = k*p + 1
            if q in prime_set:
                sg[k].add(p)
    return sg

def build_transition_matrices(primes, gaps, sg_families):
    prime_set = set(primes)
    M_all = {d: np.zeros((8,8), dtype=int) for d in gaps}
    M_sgk = {k: {d: np.zeros((8,8), dtype=int) for d in gaps}
             for k in sg_families.keys()}

    for p in primes:
        for d in gaps:
            q = p + d
            if q not in prime_set:
                continue

            r1 = p % 30
            r2 = q % 30
            if r1 not in IDX or r2 not in IDX:
                continue

            i = IDX[r1]
            j = IDX[r2]

            # transitions bidirectionnelles
            M_all[d][i,j] += 1
            M_all[d][j,i] += 1

            for k, sg_set in sg_families.items():
                if p in sg_set:
                    M_sgk[k][d][i,j] += 1
                    M_sgk[k][d][j,i] += 1

    return M_all, M_sgk

def main():
    os.makedirs("data", exist_ok=True)

    N_MAX = 50_000_000
    k_list = list(range(2, 300, 2))
    #k_list = [2,4,6,8,10,12,14,16,18,20,22,24]
    #k_list = [2,4,6,8]
    gaps = [2,4,6]

    print("Génération des nombres premiers...")
    primes = sieve_primes(N_MAX)

    print("Construction des familles SG(k)...")
    sg_families = build_sg_families(primes, k_list)

    print("Construction des matrices de transitions...")
    M_all, M_sgk = build_transition_matrices(primes, gaps, sg_families)

    print("\n=== Analyse globale (tous les premiers) ===")
    for d in gaps:
        print(f"\n  Gap {d} (global)...")
        stats = analyze_matrix(M_all[d])
        print(f"    Entropie moyenne : {stats['H_mean']:.4f}")
        print(f"    Entropie normalisée : {stats['H_norm']:.4f}")

        db = stats["db_mean_error"]
        if db is None:
            print("    Detailed balance (erreur moyenne) : N/A")
        else:
            print(f"    Detailed balance (erreur moyenne) : {db:.4f}")

    print("\n=== Analyse restreinte aux SG(k) ===")
    for k in k_list:
        print(f"\n=== SG({k}) ===")
        for d in gaps:
            print(f"  Gap {d}...")
            M = M_sgk[k][d]
            stats = analyze_matrix(M)
            print(f"    Total transitions : {M.sum()}")
            print(f"    Entropie moyenne : {stats['H_mean']:.4f}")
            print(f"    Entropie normalisée : {stats['H_norm']:.4f}")

            db = stats["db_mean_error"]
            if db is None:
                print("    Detailed balance (erreur moyenne) : N/A")
            else:
                print(f"    Detailed balance (erreur moyenne) : {db:.4f}")

    # Sauvegarde
    for d in gaps:
        np.save(f"data/M_all_gap{d}.npy", M_all[d])
    for k in k_list:
        for d in gaps:
            np.save(f"data/M_SG{k}_gap{d}.npy", M_sgk[k][d])

    print("\nMatrices sauvegardées dans data/")
    print("Analyse terminée.")

if __name__ == "__main__":
    main()
