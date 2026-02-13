#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os

def load_scores():
    scores = {}
    with open("period9_scores.txt", "r") as f:
        for line in f:
            if "SG(" in line:
                parts = line.strip().split()
                k = int(parts[0].replace("SG(", "").replace(")", ""))
                score = float(parts[-1])
                scores[k] = score
            if line.startswith("Global"):
                scores["Global"] = float(line.split("=")[-1])
    return scores

def main():
    if not os.path.exists("period9_scores.txt"):
        print("Erreur : fichier period9_scores.txt manquant.")
        return

    scores = load_scores()

    ks = sorted(k for k in scores.keys() if isinstance(k, int))
    ys = [scores[k] for k in ks]

    plt.figure(figsize=(10,5))
    plt.plot(ks, ys, marker="o", linestyle="-", color="blue")

    plt.axhline(0, color="black", linewidth=0.8)
    plt.title("Score période 9 en fonction de k")
    plt.xlabel("k")
    plt.ylabel("Score période 9 (autocorr lag=9)")
    plt.grid(True)

    plt.savefig("figures/period9_vs_k.png", dpi=200)
    plt.close()

    print("Graphique généré : figures/period9_vs_k.png")

if __name__ == "__main__":
    main()
