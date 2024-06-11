# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt


def cross_corr(filename, true_peak=True):

    Fs, x = scipy.io.wavfile.read(filename)
    x = x.astype(np.float32)
    left_ch = x[:, 0]
    left_ch /= np.max(np.abs(left_ch))
    right_ch = x[:, 1]
    right_ch /= np.max(np.abs(right_ch))

    corr = scipy.signal.correlate(left_ch, right_ch, mode='full')
    lags = scipy.signal.correlation_lags(
        left_ch.size, right_ch.size, mode="full")

    x_mid = lags[np.argmax(corr)]
    if true_peak:
        alpha = corr[np.argmax(corr) - 1]
        beta = corr[np.argmax(corr)]
        gamma = corr[np.argmax(corr) + 1]
        p = 0.5 * (alpha - gamma) / (alpha - 2 * beta + gamma)
        return x_mid + p
    else:
        return x_mid
