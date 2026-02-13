import os
import numpy as np
import matplotlib.pyplot as plt

RESIDUES = [1,7,11,13,17,19,23,29]

def plot_heatmap(M, title, filename):
    plt.figure(figsize=(5,4))
    plt.imshow(M, cmap="viridis")
    plt.colorbar()
    plt.xticks(range(8), RESIDUES)
    plt.yticks(range(8), RESIDUES)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    plt.close()

def main():
    os.makedirs("figures", exist_ok=True)

    gaps = [2,4,6]
    k_list = [2,4,6,8]

    # global
    for d in gaps:
        path = f"data/M_all_gap{d}.npy"
        if not os.path.exists(path):
            print(f"Fichier manquant : {path}")
            continue
        M = np.load(path)
        plot_heatmap(M, f"Global gap {d}", f"figures/global_gap{d}.png")

    # SG(k)
    for k in k_list:
        for d in gaps:
            path = f"data/M_SG{k}_gap{d}.npy"
            if not os.path.exists(path):
                continue
            M = np.load(path)
            if M.sum() == 0:
                continue
            plot_heatmap(M, f"SG({k}) gap {d}", f"figures/SG{k}_gap{d}.png")

    print("Heatmaps générées.")

if __name__ == "__main__":
    main()
