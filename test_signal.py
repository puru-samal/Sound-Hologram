#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:10:54 2024

@author: puruboii
"""

import numpy as np
from scipy import signal
from scipy.io.wavfile import write
import os
import matplotlib.pyplot as plt


class TestSignal:

    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.signal = None
        self.isGenerated = False

    def generate(self, dur=1.0, amp=1.0, repititions=0, *args, **kwargs):
        pass

    def write(self, filename):
        pass

    def plot(self):
        pass


class LogSineSweep(TestSignal):

    def __init__(self, sample_rate):
        super().__init__(sample_rate)

    def generate(self, dur, amp, repititions=1, f0=20, f1=20000, zero_pad=0):

        if repititions < 1:
            raise Exception("Invalid argument: repititions < 1")

        inv_fs = 1 / self.sample_rate
        padSamples = int(zero_pad * self.sample_rate)
        n = np.arange(0, dur, inv_fs)

        win = signal.windows.cosine(int(2/1000 * self.sample_rate))
        sig_win = np.ones_like(n)
        sig_win[0:len(win)//2] *= win[0:len(win)//2]
        sig_win[len(win)//2:len(win)] *= win[len(win)//2:]

        out = amp * signal.chirp(n, f0, n[-1],
                                 f1, method="logarithmic", phi=-90) * sig_win
        out = np.pad(out, pad_width=padSamples, mode="constant")

        # shape: ((dur + 2 * zero_pad) * repititions * sample_rate,)
        self.signal = np.array([])
        for _ in range(repititions):
            self.signal = np.append(self.signal, out)

        self.isGenerated = True

    def plot(self):
        if self.isGenerated:
            n = np.arange(0, len(self.signal) /
                          self.sample_rate, 1 / self.sample_rate)
            fig, axs = plt.subplots()
            axs.axis(ymin=-2, ymax=2)
            axs.set(xlabel="Time(s)")
            axs.set_title("Test Signal")
            axs.plot(n, self.signal)
        else:
            print("Generate test signal first!")

    def write(self, filename):
        if self.isGenerated:
            write(filename, self.sample_rate, self.signal.astype(np.float32))
        else:
            print("Generate test signal first!")


class WhiteNoise(TestSignal):

    def __init__(self, sample_rate):
        super().__init__(sample_rate)

    def generate(self, dur, amp, repititions=1, zero_pad=0):

        rng = np.random.default_rng()
        if repititions < 1:
            raise Exception("Invalid argument: repititions < 1")

        inv_fs = 1 / self.sample_rate
        padSamples = int(zero_pad * self.sample_rate)
        noise_power = 0.001 * self.sample_rate / 2
        n = np.arange(0, dur, inv_fs)

        win = signal.windows.cosine(int(2/1000 * self.sample_rate))
        sig_win = np.ones_like(n)
        sig_win[0:len(win)//2] *= win[0:len(win)//2]
        sig_win[len(win)//2:len(win)] *= win[len(win)//2:]

        out = rng.normal(scale=np.sqrt(noise_power), size=n.shape)
        out *= (amp * sig_win) / np.max(np.abs(out))
        out = np.pad(out, pad_width=padSamples, mode="constant")

        # shape: ((dur + 2 * zero_pad) * repititions * sample_rate,)
        self.signal = np.array([])
        for _ in range(repititions):
            self.signal = np.append(self.signal, out)

        self.isGenerated = True

    def plot(self):
        if self.isGenerated:
            n = np.arange(0, len(self.signal))/self.sample_rate
            fig, axs = plt.subplots()
            axs.axis(ymin=-2, ymax=2)
            axs.set(xlabel="Time(s)")
            axs.set_title("Test Signal")
            axs.plot(n, self.signal)
        else:
            print("Generate test signal first!")

    def write(self, filename):
        if self.isGenerated:
            write(filename, self.sample_rate, self.signal.astype(np.float32))
        else:
            print("Generate test signal first!")


# ###### USUAGE ######
# Instantiate Object
# test = LogSineSweep(sample_rate=44100)
# test = WhiteNoise(sample_rate=44100)

# Generate Signal
# test.generate(dur=250/1000, amp=0.25, zero_pad=0.001, repititions=1)

# Plot Signal
# test.plot()

# Write to file
# filename = "test_signal_250.wav"
# test.write(filename)

# Play file using appropriate sys command
# os.system("afplay " + filename)
