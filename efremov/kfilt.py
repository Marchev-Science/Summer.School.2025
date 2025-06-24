# kfilt.py

import numpy as np
from numpy.linalg import inv
import pandas as pd

# ==== LOG ODDS FUNCTION ====
def logodds(p, eps=1e-4):
    p = np.clip(p, eps, 1 - eps)
    return np.log(p / (1 - p))

def elogodds(data, T, cuts):
    n_bins = len(cuts) - 1
    lodds = np.full((T, n_bins), np.nan)
    for k in range(T):
        data_k = data[data['month'] == k]
        _, _, log_y, _ = bin_data(data_k, cuts)
        lodds[k] = log_y
    return lodds


def rgen(empirical_p, Nk, Rc=1, eps=1e-6):
    var = np.where(
        (empirical_p > 0) & (empirical_p < 1),
        empirical_p * (1 - empirical_p) / Nk,
        1e6
    )
    R = np.diag(var * Rc + eps)
    return R

def qgen(log_odds_matrix, Qc=1, Qtc=1, eps=1e-6):
    diff = np.diff(log_odds_matrix, axis=0)
    diff_clean = diff[~np.isnan(diff).any(axis=1)]
    # log-odds covariance
    Q_lo = np.cov(diff_clean.T) * Qc + np.eye(diff_clean.shape[1]) * eps
    n = Q_lo.shape[0]
    # trend covariance /usually smaller uncertainty/
    Q_tr = np.eye(n)*0.01*Qtc

    # Final block matrix
    Q = np.block([[Q_lo,             np.zeros((n, n))],
                  [np.zeros((n, n)), Q_tr]])
    return Q

def model(n_bins):
    F = np.block([[np.eye(n_bins), np.eye(n_bins)],
        [np.zeros((n_bins, n_bins)), np.eye(n_bins)]])
    C = np.block([np.eye(n_bins), np.zeros((n_bins, n_bins))])
    return F, C


def kf(xc, Pc, y_k, F, C, Q, R):
    # Prediction
    xp = F @ xc
    Pp = F @ Pc @ F.T + Q

    S = C @ Pp @ C.T + R
    K = Pp @ C.T @ inv(S)
    # Correction
    xc = xp + K @ (y_k - C @ xp)
    Pc = (np.eye(len(xc)) - K @ C) @ Pp

    return xp, xc, Pc

def kf_predict(x_k, P_k, F, C, Q, n_steps=1):
    # One-step-ahead extrapolator
    preds = []
    for _ in range(n_steps):
        x_k = F @ x_k  # F = I
        P_k = P_k + Q
        preds.append(x_k.copy())
    return np.array(preds)

def mavg(elodds, window):
    T, N = elodds.shape
    result = np.zeros_like(elodds, dtype=float)
    for j in range(N):
        for t in range(window, T):
            result[t, j] = np.mean(elodds[t - window:t, j])
    return result



def bin_data(data_k, bin_edges):
    data_k = data_k.copy()
    data_k['risk_zone'] = pd.cut(data_k['ym'], bins=bin_edges, labels=False, include_lowest=True)
    n_bins = len(bin_edges) - 1
    model_p, empirical_p, log_odds_y, Nk = [], [], [], []

    for i in range(n_bins):
        data_bin = data_k[data_k['risk_zone'] == i]
        N_bin = len(data_bin)
        Nk.append(N_bin)

        if N_bin == 0:
            model_p.append(np.nan)
            empirical_p.append(np.nan)
            log_odds_y.append(np.nan)
            continue

        p_model = data_bin['ym'].mean()
        p_emp = data_bin['y'].mean()
        model_p.append(p_model)
        empirical_p.append(p_emp)
        log_odds_y.append(logodds(p_emp))

    return np.array(model_p), np.array(empirical_p), np.array(log_odds_y), np.array(Nk)
