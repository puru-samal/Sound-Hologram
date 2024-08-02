#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:09:30 2024

@author: puruboii
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from collections import deque
import seaborn as sns
from matplotlib.pyplot import subplots


def cross_corr(filename, true_peak=True):
    """
    Find the direction of arrival by using the time difference between 2 mics

    Parameters:
    filename    (str): Path to stereo audio file
    true_peak  (bool): True fits a parabola near top 3 maximum values to extimate true peak

    Returns:
    float: correlation lag in samples
    """

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


def two_mic_doa(delta_t, dis_mic, C, ideal_x=2.0, save_plot=False):
    """
    Find the direction of arrival by using the time difference between 2 mics

    Parameters:
    C (float): Speed of sound
    delta_t (float): Time difference between 2 mics in second
    dis_mic (float): Distance between 2 mics in meter
    ideal_x (float): Default is set to 2 meters. Specifies the x of the sound source position you would like to use 
                     to determine the direction angle. The relationship between the x and y of the position is not linear 
                     but approaches linearity. 
    save_plot (bool): Default is set to False. Specifies whether you want to save the plot of (x, y), (x, dy/dx), and (x, angle).

    Returns:
    float: The angle of sound direction in degree
    """
    if delta_t == 0:
        return 0.0

    delta_d = C*abs(delta_t)
    x_b = dis_mic * 0.5

    delta_d_2 = (delta_d**2)  # square of delta_d
    x_b_2 = (x_b**2)  # square of x_b

    # min_pos_x = np.sqrt(-(delta_d_2)*(delta_d_2 - 4*x_b_2)/(4*(4*x_b_2 - delta_d_2)))

    P = 0.25*delta_d_2 - x_b_2
    Q = ((4*x_b_2) / delta_d_2) - 1
    # print(f"P:{P}\nQ:{Q}\nmin_pos_x:{min_pos_x}")

    if ideal_x < dis_mic * 0.5:
        raise ValueError(
            f"ideal_x ({ideal_x}) needs to be greater than the half of the dis_mic ({dis_mic * 0.5})")
        return 0.0

    x = np.linspace(dis_mic * 0.5, ideal_x, 1000)
    y = (np.sqrt(P + (x**2)*Q))
    dy_dx = (Q*x) / (np.sqrt(P + (x**2)*Q))
    theta = (90 - np.rad2deg(np.arctan(dy_dx)))

    if delta_t < 0:  # change the sign if needed
        theta *= -1

    if save_plot:
        plt.figure(figsize=(22, 14))
        plt.subplot(3, 1, 1)
        plt.title(
            f"time_diff:{delta_t} (s), dist_mic:{dis_mic} (m), sound_speed:{C} (m/s)")
        plt.plot(x, y)
        plt.xlabel('x (meter)')
        plt.ylabel('y (meter)')

        plt.subplot(3, 1, 2)
        plt.plot(x, dy_dx)
        plt.xlabel('x (meter)')
        plt.ylabel('dy/dx')

        plt.subplot(3, 1, 3)
        plt.plot(x, theta)
        plt.xlabel('x (meter)')
        plt.ylabel('angle (degree)')
        plt.savefig(f"doa_{delta_t}_{dis_mic}_{C}.png", bbox_inches='tight')
        # plt.show()

    return theta[len(x) - 1]


def dfText2Dict(filename):
    # Parse data
    data = np.loadtxt(filename, dtype=str, delimiter='\t')

    # Generate Result Dict
    result_dict = {k: [] for k in data[0].split()}

    for row in data[1:]:
        row_split = row.split()[1:]
        assert(len(row_split) == len(result_dict.keys()))

        for i, key in enumerate(result_dict.keys()):
            try:
                d = round(float(row_split[i]), 3)
            except:
                d = row_split[i]

            result_dict[key].append(d)

    return result_dict


def plot_doa_results(result_dict, YM=3.53, SP=0.059, NUM_SPEAKERS=64):
    """
    Plot the result of the direction of arrival experiment

    Parameters:
    result_dict (dict): A dictonary created by running dfTest2Dict on the .txt file from DOA expt
    YM (float): Distance from listener to midpoint of speaker array
    SP (float): Spacing between each speaker in linear array
    NUM_SPEAKER (int): Number of speakers in linear array


    Returns:
    None: Plots the results
    """

    # Initialize Plots
    fig, ax = plt.subplots()
    fig.set_size_inches(12, 12)
    plt.axhline(0, color='green')  # x = 0
    plt.axvline(0, color='black')  # y = 0
    ax.set_aspect(1)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-0.1, 4)
    ax.set_title('Error between WFS angle and measured DOA')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')

    # Step 3: Add a subtitle
    subtitle_text = 'Recorded at 0.1*YM(m) and 2.5$^\circ$ intervals'
    subtitle_x = 1.0  # X position of the subtitle
    subtitle_y = 3.7  # Y position of the subtitle
    ax.text(subtitle_x, subtitle_y, subtitle_text,
            ha='center', fontsize=10, color='black')

    # Draw Circular Grid at 0.1 * radius intervals
    theta = np.linspace(0.0, np.pi, 150)
    radii = np.arange(0, 1.5, 0.1) * YM
    for r in radii:  # Plot Circles
        X = r * np.cos(theta)
        Y = r * np.sin(theta)
        ax.plot(X, Y, linewidth=0.23, color='black')

    # Draw lines at 2.5 degree intervals
    theta = np.linspace(0.0, np.pi, 72+1)
    radii = np.linspace(0, 1, num=100) * 5
    for t in theta:
        X = radii * np.cos(t)
        Y = radii * np.sin(t)
        ax.plot(X, Y, linewidth=0.23, color='black')

    # Plot Speakers
    XPOS = np.linspace(-1.0, 1.0, num=NUM_SPEAKERS, endpoint=True) * \
        ((SP * (NUM_SPEAKERS - 1))/2)
    ax.plot(XPOS, YM * np.ones_like(XPOS), 'r-',
            linewidth=6.0, markersize=10, alpha=0.75)

    # Set and normalize color map
    cmap = plt.get_cmap('plasma')
    norm = Normalize(vmin=min(result_dict['Error']),
                     vmax=max(result_dict['Error']))

    # Plot locations where DOA was calculated
    # Color indicates Error between Wfs angle and measured angle
    num_pos = len(result_dict['Radial_Distance'])
    for i in range(num_pos):
        dist = result_dict['Radial_Distance'][i] * YM
        angle = (-np.radians(result_dict['Wfs_Angle'][i]) + np.pi/2)
        X = dist * np.cos(angle)
        Y = dist * np.sin(angle)
        c = cmap(norm(result_dict['Error'][i]))
        ax.plot(X, Y, 'o', color=c, markersize=6, alpha=0.75)  # Plot Source

    # Plot coloebar indicating error rate
    cbar = fig.colorbar(ScalarMappable(norm=norm, cmap=cmap),
                        ax=ax, orientation='horizontal', shrink=0.5, pad=0.07)

    cbar.set_label("Error")
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

def get_separations(ranges, step_sizes, maximum=40.0, minimum=0.1):
    i = 0
    j = 1
    separations = [ranges[i]]
    while j < len(ranges):
        sep = separations[-1] - step_sizes[i]
        separations.append(sep)
        if sep <= ranges[j]:
            i += 1
            j += 1

    outer_ranges = []
    terminator = separations[0]
    while terminator < maximum:
            terminator += step_sizes[0]
            outer_ranges.append(min(terminator, maximum))
            
            
    start_idx = len(outer_ranges)
    separations = outer_ranges[::-1] + separations

    inner_ranges = []
    terminator = separations[-1]
    while terminator > minimum:
            terminator -= step_sizes[-1]
            inner_ranges.append(max(terminator, minimum))
    
    separations =  separations + inner_ranges

    assert(separations[start_idx] == ranges[0])
    return start_idx, separations

class MvAverage:
    def __init__(self, track, max_size=6):
        self.buffer = deque(maxlen=max_size)
        self.max_size = max_size
        self.reversals = 0
        self.track = track
    
    def update(self, val):
        self.buffer.append(val)
        self.reversals += 1

    def print_stats(self, trial):
        threshold = None if len(self.buffer) == 0 else sum(self.buffer) / len(self.buffer)
        print('')
        print(f"\033[92m|** Track:{self.track} | Trial:{trial}\033[0m")
        print(f"\033[92m|** Total Reversals: {self.reversals}\033[0m")
        print(f"\033[92m|** Separations (last {self.max_size} reversals): {list(self.buffer)}\033[0m")
        print(f"\033[92m|** Threshold: {threshold}\033[0m")
        print('')

def make_sep_plot(fname, data):
    fig, ax = subplots()
    sns.scatterplot(x=data['Trial'], y=data['Separation'],
                    hue=data['Reversal'], ax=ax)
    sns.lineplot(x=data['Trial'], y=data['Separation'], ax=ax)
    # save figure
    file_name = f"{fname}_figure.png"
    fig.savefig(file_name)
    print(f"SUCCESS: Saved plot in {file_name}")



#result_dict = dfText2Dict('test_rev.txt')
# plt.plot(result_dict['Separation'])
# plot_doa_results('doa_test/result.txt')
# print(two_mic_doa(0.00015, 0.15, 343, ideal_x=1, save_plot=True))
