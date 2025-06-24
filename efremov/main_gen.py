# generate_data.py

import numpy as np
import pandas as pd

np.random.seed(0)

# === parameters ===
N_per_month = 10000  # contracts per month
Tfc = 1
T = 3*12 + Tfc           # months
n_bins = 5

# === Drift in log-odds per bin ===
true_log_odds = np.zeros((T, n_bins))
true_log_odds[0] = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])  # initial values

for t in range(1, T):
    drift = np.random.normal(0, 0.1, size=n_bins)
    true_log_odds[t] = true_log_odds[t - 1]*0.7 + true_log_odds[np.max([t - 2, 0])]*0.3 - 0*true_log_odds[np.max([t - 3, 0])]*0.01 + drift

# === generate individual contracts ===
all_data = []
bin_edges = np.linspace(0, 1, n_bins + 1)

for t in range(T):
    ym = np.random.uniform(0, 1, N_per_month)
    bins = np.digitize(ym, bin_edges) - 1
    bins = np.clip(bins, 0, n_bins - 1)

    # log-odds -> probabilities per bin
    p = 1 / (1 + np.exp(-true_log_odds[t][bins]))
    y = np.random.binomial(1, p) # true target

    # add noise (5% target noise)
    noise_flip = np.random.binomial(1, 0.05, size=N_per_month)
    flipped_y = 1 - y
    y_noisy = np.where(noise_flip == 1, flipped_y, y)

    df_month = pd.DataFrame({
        'month': t,
        'ym': ym,
        'risk_zone': bins,
        'true_log_odds': true_log_odds[t][bins],
        'y': y
    })

    all_data.append(df_month)

df_all = pd.concat(all_data, ignore_index=True)
df_all[['month', 'ym', 'y']].to_csv('data.csv', index=False)
print("data.csv - generated data with drift.")
