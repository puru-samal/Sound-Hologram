import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import librosa

def find_time_difference(file_path, true_peak=True):
    """
    Find the time difference between two channels of a audio file using cross-correlation

    Parameters:
    file_path (string): The path to a stereo wav file
    true_peak (bool):   Whether calculate the lag index for the true peak correlation value

    Returns:
    float: sample rate
    float: lag between two channels in samples
    float: lag between two channels in seconds
    """
    y, sr = librosa.load(file_path, sr=None, mono=False)

    left_channel = y[0]
    right_channel = y[1]

    correlation = sp.signal.correlate(left_channel, right_channel, mode='full')
    lags = sp.signal.correlation_lags(left_channel.size, right_channel.size, mode='full')
    idx = np.argmax(correlation)
    lag = lags[idx]

    if true_peak:
        alpha = correlation[idx-1]
        beta = correlation[idx]
        gama = correlation[idx+1]
        p = 0.5 * (alpha - gama) / (alpha - 2*beta + gama)
        # print(f"sr:{sr}, lag:{lag}, p:{p}, true_lag:{lag+p}")
        return sr, lag+p, (lag+p)/sr
    else:
        return sr, lag, lag/sr

def two_mic_doa(delta_t, dis_mic, C, ideal_x = 2.0, save_plot=False):
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

    delta_d_2 = (delta_d**2) # square of delta_d
    x_b_2 = (x_b**2) # square of x_b

    # min_pos_x = np.sqrt(-(delta_d_2)*(delta_d_2 - 4*x_b_2)/(4*(4*x_b_2 - delta_d_2)))

    P = 0.25*delta_d_2 - x_b_2
    Q = ((4*x_b_2) / delta_d_2) - 1
    # print(f"P:{P}\nQ:{Q}\nmin_pos_x:{min_pos_x}")

    if ideal_x < dis_mic * 0.5:
        raise ValueError(f"ideal_x ({ideal_x}) needs to be greater than the half of the dis_mic ({dis_mic * 0.5})")
        return 0.0
    
    x = np.linspace(dis_mic * 0.5, ideal_x, 1000)
    y = (np.sqrt(P + (x**2)*Q))
    dy_dx = (Q*x) / (np.sqrt(P + (x**2)*Q))
    theta = (90 - np.rad2deg(np.arctan(dy_dx)))

    if delta_t < 0: # change the sign if needed
        theta *= -1

    if save_plot:
        plt.figure(figsize=(22, 14))
        plt.subplot(3,1,1)
        plt.title(f"time_diff:{delta_t} (s), dist_mic:{dis_mic} (m), sound_speed:{C} (m/s)")
        plt.plot(x, y)
        plt.xlabel('x (meter)')
        plt.ylabel('y (meter)')
        
        plt.subplot(3,1,2)
        plt.plot(x, dy_dx)
        plt.xlabel('x (meter)')
        plt.ylabel('dy/dx')

        plt.subplot(3,1,3)
        plt.plot(x, theta)
        plt.xlabel('x (meter)')
        plt.ylabel('angle (degree)')
        plt.savefig(f"doa_{delta_t}_{dis_mic}_{C}.png", bbox_inches='tight')
        # plt.show()

    return theta[len(x) - 1]


# print(two_mic_doa(0.00015, 0.15, 343, ideal_x=1, save_plot=True))