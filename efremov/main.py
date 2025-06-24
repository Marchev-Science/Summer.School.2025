import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from kfilt import model, kf, logodds, elogodds, rgen, qgen, bin_data, kf_predict, mavg

# === Parameters ===
n_bins = 5
colors = ['blue', 'orange', 'green', 'red', 'purple']
Tfc = 1
T = 3*12 + Tfc
N = 10000
# Qc = 1.1
# Qtc = 0.1
# Rc = 700
Qc = 1
Qtc = 1
Rc = 1

cuts = np.linspace(0, 1, n_bins + 1)

# === Model ===
F, C = model(n_bins)

# === Data load ===
# data['month', 'ym', 'y']
data = pd.read_csv("data.csv")

# === Calc empirical log-odds matrix ===
elodds = elogodds(data, T, cuts)

Q = qgen(elodds, Qc, Qtc) # Q estimation

# === KF Initialization ===
x_kf = np.zeros((T, 2*n_bins))
x_kf[0] = np.zeros(2*n_bins)
xc = np.zeros(2*n_bins)
P = np.eye(2*n_bins)

# === KF loop ===
for k in range(1, T):
    data_k = data[data['month'] == k]
    model_p, empirical_p, y_k, Nk = bin_data(data_k, cuts)
    valid = ~np.isnan(y_k)
    if valid.sum() < n_bins:
        x_kf[k] = x_kf[k-1]
        continue

    R = rgen(empirical_p, Nk, Rc)  # R estimation
    xp, xc, P = kf(xc, P, y_k, F, C, Q, R)
    x_kf[k] = xp

# === next Tfc months forecast  ===
preds = kf_predict(x_kf[-Tfc, :], P, F, C, Q, n_steps=Tfc)
mavg_benchmark = mavg(elodds, window=Tfc)

# === Visualization ===
fig, ax = plt.subplots(figsize=(10, 6))
months = np.arange(len(x_kf))
months_forecast = np.arange(len(x_kf), len(x_kf) + preds.shape[0]) - Tfc
for i in range(n_bins):
    ax.plot(months, x_kf[:, i], color=colors[i])#, label=f'Kalman Bin {i + 1}')
    ax.plot(months, elodds[:, i], '--', color=colors[i])#, label=f'Empirical Bin {i + 1}', alpha=0.5)
    ax.plot(months, mavg_benchmark[:, i], ':', color=colors[i])#, label=f'MA Bin {i + 1}', alpha=0.7)
    ax.plot(months_forecast, preds[:, i], color=colors[i])#, label=f'Forecast Bin {i + 1}', alpha=0.8)

ax.set_title("Kalman vs Empirical vs MA Log-Odds (with Forecast)")
ax.set_xlabel("Month")
ax.set_ylabel("Log-Odds")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.tight_layout()
plt.show()

# === Performance metric ===
mseKF_list = []
mseMA_list = []
for k in range(T):
    valid = ~np.isnan(elodds[k])
    if k < 5 or valid.sum() == 0:
        continue
    mseKF_k = np.mean((x_kf[k, :n_bins][valid] - elodds[k, valid])**2)
    mseMA_k = np.mean((mavg_benchmark[k][valid] - elodds[k, valid])**2)

    mseKF_list.append(mseKF_k)
    mseMA_list.append(mseMA_k)

print(f"MSE KF: {np.mean(mseKF_list):.4f}")
print(f"MSE MA: {np.mean(mseMA_list):.4f}")
