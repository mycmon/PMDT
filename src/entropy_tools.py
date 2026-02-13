# entropy_tools.py
import math
import numpy as np

def analyze_matrix(M):
    total = M.sum()
    if total == 0:
        return {
            "pi": np.zeros(8),
            "db_mean_error": None,
            "H_i": np.zeros(8),
            "H_mean": 0.0,
            "H_norm": 0.0
        }

    out_counts = M.sum(axis=1)
    pi = out_counts / total

    db_errors = []
    for i in range(8):
        for j in range(8):
            if M[i,j] > 0 or M[j,i] > 0:
                a = pi[i] * M[i,j]
                b = pi[j] * M[j,i]
                if a + b > 0:
                    err = abs(a-b) / ((a+b)/2)
                    db_errors.append(err)
    db_mean = float(np.mean(db_errors)) if db_errors else 0.0

    H_i = []
    for i in range(8):
        if out_counts[i] == 0:
            H_i.append(0.0)
            continue
        probs = M[i,:] / out_counts[i]
        h = -sum(p*math.log2(p) for p in probs if p > 0)
        H_i.append(h)
    H_i = np.array(H_i)

    weights = out_counts / total
    H_mean = float((weights * H_i).sum())
    H_norm = H_mean / math.log2(8)

    return {
        "pi": pi,
        "db_mean_error": db_mean,
        "H_i": H_i,
        "H_mean": H_mean,
        "H_norm": H_norm
    }
