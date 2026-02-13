import numpy as np
import matplotlib.pyplot as plt
from entropy_tools import analyze_matrix
import os

def main():
    if not os.path.exists("data/M_all_gap6.npy"):
        print("Erreur : les matrices n'ont pas été générées.")
        return

    k_list = [2,4,6,8]

    labels = []
    entropies = []
    db_errors = []
    sizes = []

    # global
    M_global = np.load("data/M_all_gap6.npy")
    stats_g = analyze_matrix(M_global)
    labels.append("Global")
    entropies.append(stats_g["H_mean"])
    db_errors.append(stats_g["db_mean_error"])
    sizes.append(M_global.sum())

    # SG(k)
    for k in k_list:
        path = f"data/M_SG{k}_gap6.npy"
        if not os.path.exists(path):
            continue
        M = np.load(path)
        stats = analyze_matrix(M)
        labels.append(f"SG({k})")
        entropies.append(stats["H_mean"])
        db_errors.append(stats["db_mean_error"])
        sizes.append(M.sum())

    plt.figure(figsize=(6,5))
    for lab, H, db, n in zip(labels, entropies, db_errors, sizes):
        plt.scatter(db, H, s=20 + n/5000, label=lab)

    plt.xlabel("Detailed balance (erreur moyenne)")
    plt.ylabel("Entropie moyenne (bits)")
    plt.title("Comparaison SG(k) — Gap 6")
    plt.legend()
    plt.tight_layout()
    plt.savefig("figures/compare_SG_gap6_entropy_DB.png", dpi=200)
    plt.close()

    print("Comparaison générée.")

if __name__ == "__main__":
    main()
