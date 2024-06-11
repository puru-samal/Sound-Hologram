#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:03:44 2024

@author: puruboii
"""

import numpy as np
import test_signal as T
import cmd
import os
import config
from osc4py3.as_allthreads import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
import logging
import preset_generator
from pathlib import Path
import pandas as pd
import queue
import cross_corr
import socket
from scipy.io import wavfile
import scipy.signal as sps
import doa

# Optional: A logger to monitor activity... and debug.
logging.basicConfig(format='%(asctime)s - %(threadName)s ø %(name)s - '
                    '%(levelname)s - %(message)s')
logger = None  # Comment and uncomment lines below to log OSC messages
#logger = logging.getLogger("osc")
# logger.setLevel(logging.DEBUG)


class ExptShell(cmd.Cmd):

    intro = 'Experiment shell for Sound Hologram. Type help or ? to list commands.'
    prompt = '> '

    # Max Comms
    IP = "127.0.0.1"    # Local Server
    CLIENT_PORT = 1338  # Sending Port
    SERVER_PORT = 1339  # Listening Port
    CLIENT = "PyToMax"
    SERVER = "MaxToPy"

    # iPad Comms
    WIFI_CLIENT_IP = None  # Ipad's IP
    WIFI_SERVER_IP = None  # Computers IP
    WIFI_CLIENT_PORT = 1340       # Sending Port
    WIFI_SERVER_PORT = 1341       # Listening Port
    WIFI_CLIENT = "PyToIpad"
    WIFI_SERVER = "IpadToPy"

    # Environment Setup
    NUM_SPEAKERS = 64
    YM = 3.53   # Horizontal Distance of Midpoint from origin (Make Input)
    SP = 0.059  # SPacing between SPeakers (Make Input)
    XPOS = np.linspace(-1.0, 1.0, num=64, endpoint=True) * \
        ((SP * (NUM_SPEAKERS - 1))/2)
    NUM_SOURCES = 1
    SAMPLE_RATE = 48000  # Make sure Max is set to the same

    # Shell State Variables
    IPAD_STATE = 'none'
    ACCEPT_IPAD_INPUT = False
    IPAD_AVAILABLE = False
    max_size = 500
    pos_queue = []
    input_queue = []
    msg_queue = queue.Queue()

    # Default Test Signals
    test = T.WhiteNoise(sample_rate=SAMPLE_RATE)
    test.generate(dur=20/1000, amp=0.25, zero_pad=0.001, repititions=1)
    filename = "wn_20.wav"
    test.write(filename)
    test.generate(dur=50/1000, amp=0.25, zero_pad=0.001, repititions=1)
    filename = "wn_50.wav"
    test.write(filename)
    test.generate(dur=100/1000, amp=0.25, zero_pad=0.001, repititions=1)
    filename = "wn_100.wav"
    test.write(filename)
    test.generate(dur=250/1000, amp=0.25, zero_pad=0.001, repititions=1)
    filename = "wn_250.wav"
    test.write(filename)
    test.generate(dur=500/1000, amp=0.25, zero_pad=0.001, repititions=1)
    filename = "wn_500.wav"
    test.write(filename)

    print(f'Generated 4 test signals at {SAMPLE_RATE}Hz: ')
    print("\tWhite Noise  (20ms)  as  wn_20.wav")
    print("\tWhite Noise  (50ms)  as  wn_50.wav")
    print("\tWhite Noise (100ms)  as  wn_100.wav")
    print("\tWhite Noise (250ms)  as  wn_250.wav")
    print("\tWhite Noise (500ms)  as  wn_500.wav")

    ############################
    #### OSC EVENT HANDLERS ####
    ############################

    def max_conn(self, addr, x):
        if logger and logger.isEnabledFor(logging.INFO):
            logger.info("##### %d handler function called with: %r",
                        1, [addr, x])

        self.msg_queue.put(addr)

    def ipad_conn(self, addr, x):
        if logger and logger.isEnabledFor(logging.INFO):

            logger.info("##### %d handler function called with: %r",
                        1, x)

        if self.ACCEPT_IPAD_INPUT:
            self.msg_queue.put(addr)

    ############################
    ####      HELPERS       ####
    ############################

    def close(self):
        osc_terminate()

    def block_until_recieved(self):
        item = self.msg_queue.get(block=True, timeout=None)
        return item

    def check_conn_max(self):
        # Install message methods
        osc_method("/max/conn", self.max_conn, argscheme=osm.OSCARG_ADDRESS +
                   osm.OSCARG_DATAUNPACK)
        osc_method("/ipad/*", self.ipad_conn,
                   argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)

        # Send Message to Max
        msg = oscbuildparse.OSCMessage("/max/conn", ",s", ["Sent"])
        osc_send(msg, self.CLIENT)

    ############################
    ####    Dummy CMDs      ####
    ############################

    def do_ipad_user_input(self, arg):
        if len(self.input_queue) > self.max_size // 2:
            self.input_queue.clear()

        self.ACCEPT_IPAD_INPUT = True
        msg = oscbuildparse.OSCMessage(
            "/ipad/centre/", ",f", [1.0])
        osc_send(msg, self.WIFI_CLIENT)

        ipad_state = self.block_until_recieved().split('/')[-1]
        self.ACCEPT_IPAD_INPUT = False
        self.input_queue.append(ipad_state)

        msg = oscbuildparse.OSCMessage(
            "/ipad/centre/", ",f", [0.0])
        osc_send(msg, self.WIFI_CLIENT)
        return

    def do_key_user_input(self, arg):
        if len(self.input_queue) > self.max_size // 2:
            self.input_queue.clear()

        key_state = input("Enter (, | .): ")
        SUCCESS = False

        while not SUCCESS:
            if key_state == ',':
                self.input_queue.append('left')
                SUCCESS = True
            elif key_state == '.':
                self.input_queue.append('right')
                SUCCESS = True
            else:
                print('Entered wrong key. Re-enter.')
                continue

    ############################
    ####    SHELL CMDs      ####
    ############################

    def do_quit(self, arg):
        'Exit the shell:  quit'
        print('Thank you!')
        self.close()
        return True

    def do_init_conn(self, arg):
        'Establish client-server connection with Max/MSP: init'
        try:
            try:
                osc_terminate()
            except:
                pass
            osc_startup()
            # Initialize Client
            osc_udp_client(self.IP, self.CLIENT_PORT, self.CLIENT)
            # Initialize Server
            osc_udp_server(self.IP, self.SERVER_PORT, self.SERVER)

            self.check_conn_max()
            self.block_until_recieved()
            print(f"SUCCESS: Connection established @ {self.IP}.")
            print(f"\tSending   at port: {self.CLIENT_PORT}")
            print(f"\tListening at port: {self.SERVER_PORT}")

            ipad_input = input("Use iPad input? [y/n]: ")

            if ipad_input.lower() == 'y':
                hostname = socket.gethostname()
                self.WIFI_SERVER_IP = socket.gethostbyname(hostname)

                # Initialize Server
                osc_udp_server(self.WIFI_SERVER_IP, self.WIFI_SERVER_PORT,
                               self.WIFI_SERVER)

                self.WIFI_CLIENT_IP = input("Enter iPad's IP addr: ")
                # Initialize Client
                osc_udp_client(self.WIFI_CLIENT_IP, self.WIFI_CLIENT_PORT,
                               self.WIFI_CLIENT)

                print(f"\tSending   at port: {self.WIFI_CLIENT_PORT}")
                print(f"\tListening at port: {self.WIFI_SERVER_PORT}")
                print("Ensure iPad's TouchOSC is set to: ")
                print(f"\tConnection    : UDP")
                print(f"\tHost          : {self.WIFI_SERVER_IP}")
                print(f"\tSend Port     : {self.WIFI_SERVER_PORT}")
                print(f"\tRecieve Port  : {self.WIFI_CLIENT_PORT}")
                inp = input(
                    "Set in iPad and press and press key to continue...")
                print("Pinging iPad. Press any button in iPad to continue...")

                try:
                    self.do_ipad_user_input("Test")
                    self.IPAD_AVAILABLE = True
                    print(
                        f"SUCCESS: iPad connection established @ {self.WIFI_SERVER_IP}.")
                except Exception as e:
                    print(str(e))
                    print("FAIL: Connection timed out.")
                    print("Using keyboard input.")
                    self.IPAD_AVAILABLE = False
                    return
            else:
                IPAD_AVAILABLE = False
                print("Using keyboard input.")
                return

        except Exception as e:
            print("Error initializing: ")
            print(str(e))
            osc_terminate()

    def do_init_spat(self, arg):
        'Initialize spat5.wfs~: init_spat'

        # Setup Speakers
        Speakers = config.Speakers(self.NUM_SPEAKERS)
        ### Set Speaker Positions ####
        for i in range(Speakers.num_speakers):
            Speakers.set_speaker_pos(i+1, [self.XPOS[i], self.YM, 0.0])

        # Setup Sources
        # spat5.wfs~ needs to be initialized with number of sources and speakers and
        # cannot be chance later via a message so init with 1 and iterate
        sources = config.Sources(self.NUM_SOURCES)
        angles = np.array([0]) if self.NUM_SOURCES < 2 else np.linspace(-90, 90,
                                                                        self.NUM_SOURCES,
                                                                        endpoint=True)
        for i in range(self.NUM_SOURCES):
            sources.set_source_pos(i+1, [angles[i], 0, self.YM/2])
            self.pos_queue.append(f'{self.YM/2}/{angles[i]}')

        filename = "config.txt"
        if os.path.isfile(os.path.join(os.getcwd(), filename)):
            pass
        else:
            # Write To Preset File
            with open("config-init.txt", "r") as init, open("config.txt", "w") as f:
                f.truncate(0)
                for line in init:
                    f.write(line)

                f.write("\n")
                f.writelines(Speakers.toStrList())
                f.writelines(sources.toStrList())

        msg = oscbuildparse.OSCMessage(
            "/init-spat/preset/load", ",s", [filename])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        print("SUCCESS: spat5.wfs~ initialized.")
        return

    def do_test_signal(self, arg):
        'Generate Test Signal: test_signal filepath'
        arg = arg.split()
        if len(arg) != 1:
            print("Error: see usage (hint: help test_signal)")
            return

        test_file = Path(arg[0])
        file_name = arg[0]
        if test_file.is_file():
            # Resample if not self.SAMPLE_RATE
            curr_Fs, data = wavfile.read(file_name)
            if int(curr_Fs) != int(self.SAMPLE_RATE):
                num_samples = round(
                    data.shape[0] * float(self.SAMPLE_RATE) / curr_Fs)
                resampled_data = sps.resample(data, num_samples)
                resampled_data = resampled_data.astype(np.float32)
                resampled_data /= np.max(np.abs(resampled_data))
                wavfile.write(file_name, self.SAMPLE_RATE, resampled_data)
            else:
                pass
            msg = oscbuildparse.OSCMessage(
                "/playback-file/open", ",s", [file_name])
            osc_send(msg, self.CLIENT)
            self.block_until_recieved()
            print("SUCCESS: test signal set.")
            return
        else:
            print("Error: Specified file does not exist.")
            return

    def do_set_pos(self, arg):
        'Set Source Position: set_pos index angle distance'
        'Keep in mind, distance is multiplied with YM.'
        'Intended to be used as a ratio.'
        arg = arg.split()
        try:
            idx = int(arg[0])
            angle = float(arg[1])
            dist = float(arg[2])
        except:
            print("Parse Error: Invalid Arguments")
            return

        if len(self.pos_queue) > self.max_size:
            self.pos_queue.clear()

        msg = oscbuildparse.OSCMessage(
            f"/set-source/source/{idx}/aed", ",fff", [angle, 0, dist*self.YM])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        self.pos_queue.append(f'{dist}/{angle}')

    def do_set_speaker(self, arg):
        'Set Active speaker: set_speaker speakeridx0 speakeridx1 ...'
        'Speakers are 0-indexed'
        'Make sure Max is in Speaker Out mode'

        arg = arg.split()
        gains = np.zeros(self.NUM_SPEAKERS)

        try:

            for speaker in arg:
                sp = int(speaker)
                gains[sp] = 1.0

        except Exception as e:
            print("Error initializing: ")
            print(str(e))

        fmt = ',' + ''.join('f' for i in range(64))
        msg = oscbuildparse.OSCMessage(
            f"/speaker-ch/gains", fmt, list(gains))
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()

    def do_play(self, arg):
        'Plays all unmuted sources: play'
        print("Playing...")
        attr = self.pos_queue[-1].split('/')
        print(f"\tSource: Dist:{attr[0]} | Angle:{attr[-1]}")
        # Playback
        msg = oscbuildparse.OSCMessage(
            "/play", ",i", [1])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()

    def do_play_rec(self, arg):
        'Play/Record: play_rec filename duration(ms)'
        'Make sure Recording duration > Playback Duration'
        print("Play/Recording...")

        arg = arg.split()
        if len(arg) != 2:
            print("Error: see usage (hint: help play_rec)")
            return

        try:
            filename = arg[0]
            rec_dur = int(arg[1])
        except:
            print("Parse Error: Invalid Arguments")
            return

        filename = os.path.join(os.getcwd(), filename)

        # Remove the file if it exists
        try:
            os.remove(filename)
        except OSError:
            pass

        msg = oscbuildparse.OSCMessage(
            "/record-file/open", ",s", [filename])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        print("SUCCESS: Record File set.")
        RECORD_FILE = arg[0]

        print("Play/Recording...")
        attr = self.pos_queue[-1].split('/')
        print(f"\tSource     : Dist:{attr[0]} | Angle:{attr[-1]}")
        print(f"\tRecord File: {RECORD_FILE}")

        # Playback
        msg = oscbuildparse.OSCMessage(
            "/play-rec/record", ",i", [rec_dur])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()

    def do_mute(self, arg):
        'Mute a source: mute idx[0:mutes all]'
        arg = arg.split()
        if len(arg) != 1:
            print("Error: see usage (hint: help test_signal)")
            return

        try:
            idx = int(arg[0])
        except:
            print("Parse Error: Enter valid integer")
            return

        if idx > self.NUM_SOURCES:
            print(
                f"Error: source idx out of range. Must be in range [1..{self.NUM_SOURCES}]")

        if idx == 0:
            msg = oscbuildparse.OSCMessage(
                "/set-source/source/*/mute", ",i", [1])
            osc_send(msg, self.CLIENT)
        else:
            msg = oscbuildparse.OSCMessage(
                f"/set-source/source/{idx}/mute", ",i", [1])
            osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        if idx == 0:
            print("SUCCESS: All sources muted.")
        else:
            print(f"SUCCESS: {idx} source muted.")

    def do_unmute(self, arg):
        'Unmute a source: unmute idx[0:unmutes all]'
        arg = arg.split()
        if len(arg) != 1:
            print("Error: see usage (hint: help test_signal)")
            return

        try:
            idx = int(arg[0])
        except:
            print("Parse Error: Enter valid integer")
            return

        if idx > self.NUM_SOURCES:
            print(
                f"Error: source idx out of range. Must be in range [1..{self.NUM_SOURCES}]")

        if idx == 0:
            msg = oscbuildparse.OSCMessage(
                "/set-source/source/*/mute", ",i", [0])
            osc_send(msg, self.CLIENT)
        else:
            msg = oscbuildparse.OSCMessage(
                f"/set-source/source/{idx}/mute", ",i", [0])
            osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        if idx == 0:
            print("SUCCESS: All sources unmuted.")
        else:
            print(f"SUCCESS: {idx} source unmuted.")

    def do_playback(self, arg):
        'Playback commands from a file: playback expt.txt'
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    ############################
    ####    EXPTS           ####
    ############################

    def do_random_two_source(self, arg):
        'Run the random two source experiment: random_two_source runs lo hi sep dist'
        'Make sure test_signal is set.'
        'Make sure sources are unmuted'

        arg = arg.split()
        if len(arg) != 5:
            print("Error: see usage (hint: help test_signal)")
            return

        try:
            runs = int(arg[0])
            lo = float(arg[1])
            hi = float(arg[2])
            sep = float(arg[3])
            dist = float(arg[4])
        except:
            print("Parse Error: Enter valid values")
            return

        self.pos_queue.clear()
        self.input_queue.clear()
        p = preset_generator.PresetGenerator(self.NUM_SOURCES)

        if self.IPAD_AVAILABLE:
            expt = p.randomized_two_source(
                runs, lo, hi, sep, dist, input_type='ipad')
        else:
            expt = p.randomized_two_source(
                runs, lo, hi, sep, dist, input_type='keyboard')

        cmds = expt.splitlines()
        for _cmd in cmds:
            self.onecmd(_cmd)

        # Write Results to File
        assert(2 * len(self.input_queue) == len(self.pos_queue))

        file_name = input('Enter .txt filename to write results to: ')

        with open(file_name, 'w+'):
            pass

        results = {
            "Radial Distance": [],
            "Initial Angle": [],
            "Final Angle": [],
            "Direction": [],
            "Recorded Direction": [],
        }

        for i in range(len(self.input_queue)):

            recorded_dir = self.input_queue[i]
            initial_pos = self.pos_queue[2 * i]
            final_pos = self.pos_queue[2 * i + 1]
            distance = np.round(float(initial_pos.split('/')[0]), 2)
            init_angle = np.round(float(initial_pos.split('/')[-1]), 2)
            final_angle = np.round(float(final_pos.split('/')[-1]), 2)
            actual_dir = "right" if (
                final_angle - init_angle) >= 0 else "left"

            results['Radial Distance'].append(distance)
            results['Initial Angle'].append(init_angle)
            results['Final Angle'].append(final_angle)
            results['Direction'].append(actual_dir)
            results["Recorded Direction"].append(recorded_dir)

        df = pd.DataFrame(data=results)
        with open(file_name, 'a') as f:
            f.write(df.to_string())
            f.write('\n')

        acc = np.mean([1 if a == b else 0 for a,
                      b in zip(results["Recorded Direction"], results['Direction'])])

        with open(file_name, 'a') as f:
            f.write(f"Accuracy: {acc}\n")

        print(f"SUCCESS: Saved results in {file_name}")

        self.pos_queue = self.pos_queue[-1:]
        self.input_queue.clear()
        return

    def do_spaced_pair_lag(self, arg):
        'Run the experiment to validate centre position: spaced_pair_lag rec_dir'
        'Use wn_20.wav'

        arg = arg.split()
        if len(arg) != 1:
            print("Error: see usage (hint: help spaced_pair_lag)")
            return

        try:
            directory = arg[0]
        except:
            print("Parse Error: Enter valid values")
            return

        p = preset_generator.PresetGenerator(self.NUM_SOURCES)
        expt = p.spaced_pair_lag(self.NUM_SPEAKERS, directory)
        cmds = expt.splitlines()
        for _cmd in cmds:
            self.onecmd(_cmd)

        results = {
            'Speaker Pair': [],
            'Delta T': [],
        }

        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path) and file_path.split('.')[-1] == 'wav':
                results['Speaker Pair'].append(file.split('.')[0])
                results['Delta T'].append(cross_corr.cross_corr(file_path))

        mean_corr = np.mean(results['Delta T'])
        df = pd.DataFrame(data=results)
        string = df.to_string()
        string += '\n'
        string += f'Mean Correlation: {mean_corr}\n'
        print(string)
        return

    def do_doa_expt(self, arg):
        'Run the doa experiment: doa_expt lo_angle hi_angle lo_dist hi_dist angle_interval distance_interval rec_dur rec_dir'
        'Make sure test_signal is set.'
        'Make sure sources are unmuted'

        arg = arg.split()
        if len(arg) != 8:
            print("Error: see usage (hint: help doa)")
            return

        try:
            lo_angle = float(arg[0])
            hi_angle = float(arg[1])
            lo_dist = float(arg[2])
            hi_dist = float(arg[3])
            angle_interval = float(arg[4])
            distance_interval = float(arg[5])
            rec_dur = int(arg[6])
            rec_dir = arg[7]
        except:
            print("Parse Error: Enter valid values")
            return

        p = preset_generator.PresetGenerator(self.NUM_SOURCES)
        expt = p.doa_expt(lo_angle, hi_angle, lo_dist, hi_dist,
                          angle_interval, distance_interval, rec_dur, rec_dir)

        cmds = expt.splitlines()
        for _cmd in cmds:
            self.onecmd(_cmd)

        results = {
            "Radial Distance": [],
            "Wfs Angle": [],
            "Delta T": [],
            "Calculated Angle": [],
            "Error": [],
        }

        dis_mic = input('Enter distance between mics: ')
        dis_mic = float(dis_mic)

        C = input('Enter speed of sound: ')
        C = float(C)

        for file in os.listdir(rec_dir):
            file_path = os.path.join(rec_dir, file)
            if os.path.isfile(file_path) and file_path.split('.')[-1] == 'wav':
                f = file[:-4]
                wfs_angle = float(f.split('_')[1])
                radial_distance = float(f.split('_')[2])
                delta_t = cross_corr.cross_corr(file_path)
                calc_angle = doa.two_mic_doa(delta_t, dis_mic, C)

                results['Radial Distance'].append(radial_distance)
                results['Wfs Angle'].append(wfs_angle)
                results['Delta T'].append(delta_t)
                results['Calculated Angle'].append(calc_angle)
                results['Error'].append(abs(wfs_angle-calc_angle))

        file_name = input('Enter .txt filename to write results to: ')
        with open(file_name, 'w+'):
            pass

        df = pd.DataFrame(data=results)
        with open(file_name, 'a') as f:
            f.write(df.to_string())
        print(f"SUCCESS: Saved results in {file_name}")

        return

    def do_three_down_one_up(self, arg):
        'Run the three-down-one-up experiment: three_down_one_up runs lo_angle hi_angle distance start_separation step_size'
        arg = arg.split()

        if len(arg) != 6:
            print("Error: see usage (hint: help three_down_one_up)")
            return

        try:
            runs = int(arg[0])
            lo = float(arg[1])
            hi = float(arg[2])
            dist = float(arg[3])
            init_sep = float(arg[4])
            step_size = float(arg[5])
        except:
            print("Parse Error: Enter valid values")
            return

        results = {
            "Radial Distance": [],
            "Initial Angle": [],
            "Final Angle": [],
            "Separation": [],
            "Direction": [],
            "Recorded Direction": [],
        }

        p = preset_generator.PresetGenerator(self.NUM_SOURCES)
        correctInaRow = 0
        sep = init_sep
        for run in range(runs):

            self.pos_queue.clear()
            self.input_queue.clear()

            if self.IPAD_AVAILABLE:
                expt = p.randomized_two_source(
                    1, lo, hi, sep, dist, input_type='ipad')
            else:
                expt = p.randomized_two_source(
                    1, lo, hi, sep, dist, input_type='keyboard')

            cmds = expt.splitlines()
            for _cmd in cmds:
                self.onecmd(_cmd)

            assert(2 * len(self.input_queue) == len(self.pos_queue))

            recorded_dir = self.input_queue[0]
            initial_pos = self.pos_queue[0]
            final_pos = self.pos_queue[1]
            distance = np.round(float(initial_pos.split('/')[0]), 2)
            init_angle = np.round(float(initial_pos.split('/')[-1]), 2)
            final_angle = np.round(float(final_pos.split('/')[-1]), 2)
            actual_dir = "right" if (
                final_angle - init_angle) >= 0 else "left"

            results['Radial Distance'].append(distance)
            results['Initial Angle'].append(init_angle)
            results['Final Angle'].append(final_angle)
            results['Separation'].append(sep)
            results['Direction'].append(actual_dir)
            results["Recorded Direction"].append(recorded_dir)

            # Correct Response
            if recorded_dir == actual_dir:
                correctInaRow += 1
                if correctInaRow == 3:
                    sep -= step_size
                    sep = max(sep, 1.0)
                    correctInaRow = 0

            elif recorded_dir != actual_dir:  # Incorrect Response
                sep += step_size
                sep = min(sep, init_sep)
                correctInaRow = 0

        file_name = input('Enter .txt filename to write results to: ')
        with open(file_name, 'w+'):
            pass

        df = pd.DataFrame(data=results)
        with open(file_name, 'a') as f:
            f.write(df.to_string())
            f.write('\n')

        acc = np.mean([1 if a == b else 0 for a,
                      b in zip(results["Recorded Direction"], results['Direction'])])

        with open(file_name, 'a') as f:
            f.write(f"Accuracy: {acc}\n")

        print(f"SUCCESS: Saved results in {file_name}")

        self.pos_queue = self.pos_queue[-1:]
        self.input_queue.clear()
        return


if __name__ == '__main__':
    ExptShell().cmdloop()
