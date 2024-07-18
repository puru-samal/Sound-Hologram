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
import socket
import psutil
from scipy.io import wavfile
import scipy.signal as sps
import utils

# Optional: A logger to monitor activity... and debug.
logging.basicConfig(format='%(asctime)s - %(threadName)s ø %(name)s - '
                    '%(levelname)s - %(message)s')
logger = None  # Comment and uncomment lines below to log OSC messages
# logger = logging.getLogger("osc")
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

        self.msg_queue.put(f'{addr}#{x}')

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

    def block_until_recieved(self, debug=False):
        item = self.msg_queue.get(block=True, timeout=None)
        if debug:
            print(item)
        return item

    def check_conn_max(self):
        # Install message methods
        osc_method("/max/*", self.max_conn, argscheme=osm.OSCARG_ADDRESS +
                   osm.OSCARG_DATA)
        osc_method("/ipad/*", self.ipad_conn,
                   argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)

        # Send Message to Max
        msg = oscbuildparse.OSCMessage("/max/conn", ",s", ["Sent"])
        osc_send(msg, self.CLIENT)

    def get_ip_addr(self, interface_name='en1'):
        try:
            addrs = psutil.net_if_addrs()

            if interface_name in addrs:
                for addr in addrs[interface_name]:
                    if addr.family == socket.AF_INET:
                        return addr.address
                    else:
                        return None
            else:
                print(f"{interface_name} not found.")
                return None

        except Exception as e:
            print(f'Error {e}')
            return None

    def get_separations(self, ranges, step_sizes):
        i = 0
        j = 1
        separations = [ranges[i]]
        while j < len(ranges):
            sep = separations[-1] - step_sizes[i]
            separations.append(sep)
            if sep <= ranges[j]:
                i += 1
                j += 1

        return separations

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

        key_state = ''
        while not (key_state ==',' or key_state == '.'):
            key_state = input("Enter (, | .): ")
            if key_state == ',':
                self.input_queue.append('left')
            elif key_state == '.':
                self.input_queue.append('right')
            else:
                print('Entered wrong key. Re-enter.')

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
                #hostname = socket.gethostname()
                #self.WIFI_SERVER_IP = socket.gethostbyname(hostname)
                self.WIFI_SERVER_IP = self.get_ip_addr(interface_name='en1')

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
                    print("FAIL: Connection timed out. Retry again.")
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
    
    def do_set_tracking(self, arg):
        'Activate/Deactivate motive tracking: set_tracking state[0/1]'
        '1 activates tracking, 0 deactivates it'
        arg = arg.split()
        try:
            tracker_state = int(arg[0])
        except:
            print("Parse Error: Invalid Arguments")
            return

        msg = oscbuildparse.OSCMessage(
            f"/set-tracking", ",i", [tracker_state])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        state = "activated" if tracker_state == 1 else "deactivated"
        print(f"SUCCESS: Tracking {state}.")
        return
    
    def do_query_tracker_pos(self, args):
        pass
    
    def do_set_offset_rel_tracker(self, arg):
        'Set radial and angular offset from tracker: set_offset_rel_tracker idx angle_offset radial_offset'
        'Tracking must be enabled'
        arg = arg.split()
        try:
            idx = int(arg[0])
            angle_offset = float(arg[1])
            radial_offset = float(arg[2])
        except:
            print("Parse Error: Invalid Arguments")
            return
        
        msg = oscbuildparse.OSCMessage(
            f"/set-offset-rel-tracker/source/{idx}/offset", ",ff", [angle_offset, self.YM*radial_offset])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        return

    def do_set_pos_rel_tracker(self, arg):
        'Set source position relatice to tracker: set_pos_rel_tracker index separation'
        'Tracking must be enabled'
        arg = arg.split()
        try:
            idx = int(arg[0])
            sep = float(arg[1])
        except:
            print("Parse Error: Invalid Arguments")
            return
        
        if len(self.pos_queue) > self.max_size:
            self.pos_queue.clear()

        msg = oscbuildparse.OSCMessage(
            f"/set-source-rel-tracker/source/{idx}/sep", ",f", [sep])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        self.pos_queue.append(f'trkr/{sep}')
        return

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
        if attr[0] == 'trkr':
            print(f"\tSource: Tracked with sep:{attr[-1]}")
        else:   
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
    
    def do_loop(self, arg):
        'Enables disables looping: loop state[0:noloop, 1:loop]'
        arg = arg.split()
        if len(arg) != 1:
            print("Error: see usage (hint: help loop)")
            return
        
        try:
            loop_state = int(arg[0])
        except:
            print("Parse Error: Enter valid integer")
            return
        
        if not (loop_state == 0 or loop_state == 1):
            print("Value Error: State must either be 0 or 1")
            return

        msg = oscbuildparse.OSCMessage("/loop", ",i", [loop_state])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        loop_state_str = "enabled" if loop_state == 1 else "disabled"
        print(f"SUCCESS: Looping is {loop_state_str}.")
        return

    def do_num_loop(self, arg):
        'Sets number of loops: num_loop int[1..]'
        arg = arg.split()
        if len(arg) != 1:
            print("Error: see usage (hint: help num_loop)")
            return
        try:
            num_loop = int(arg[0])
        except:
            print("Parse Error: Enter valid integer")
            return
        
        if num_loop < 1:
            print("Value Error: num_loop >= 1")
            return
        
        msg = oscbuildparse.OSCMessage("/num-loop", ",i", [num_loop])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        print(f"SUCCESS: Playback set to loop {num_loop} time/s.")
        return

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
            trial = p.randomized_two_source(
                runs, lo, hi, sep, dist, input_type='ipad')
        else:
            trial = p.randomized_two_source(
                runs, lo, hi, sep, dist, input_type='keyboard')

        cmds = trial.splitlines()
        for _cmd in cmds:
            self.onecmd(_cmd)

        # Write Results to File
        assert(2 * len(self.input_queue) == len(self.pos_queue))

        file_name = input('Enter .txt filename to write results to: ')

        with open(file_name, 'w+'):
            pass

        results = {
            "Radial_Distance": [],
            "Initial_Angle": [],
            "Final_Angle": [],
            "Direction": [],
            "Recorded_Direction": [],
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

            results['Radial_Distance'].append(distance)
            results['Initial_Angle'].append(init_angle)
            results['Final_Angle'].append(final_angle)
            results['Direction'].append(actual_dir)
            results["Recorded_Direction"].append(recorded_dir)

        df = pd.DataFrame(data=results)
        with open(file_name, 'a') as f:
            f.write(df.to_string())

        print(f"SUCCESS: Saved results in {file_name}")

        acc = np.mean([1 if a == b else 0 for a,
                      b in zip(results["Recorded_Direction"], results['Direction'])])
        print(f"Accuracy: {acc}\n")

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
            'Speaker_Pair': [],
            'Delta_T': [],
        }

        for file in sorted(os.listdir(directory), key=lambda x: int(x.split('_')[0])):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path) and file_path.split('.')[-1] == 'wav':
                results['Speaker_Pair'].append(file.split('.')[0])
                results['Delta_T'].append(utils.cross_corr(file_path))

        mean_corr = np.mean(results['Delta_T'])
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
            "Radial_Distance": [],
            "Wfs_Angle": [],
            "Delta_T": [],
            "Calculated_Angle": [],
            "Error": [],
        }

        dis_mic = input('Enter distance between mics: ')
        dis_mic = float(dis_mic)

        C = input('Enter speed of sound: ')
        C = float(C)

        for file in sorted(os.listdir(rec_dir), key=lambda x: (float(x.split('_')[1]), float(x.split('_')[2][:-4]))):
            file_path = os.path.join(rec_dir, file)
            if os.path.isfile(file_path) and file_path.split('.')[-1] == 'wav':
                f = file[:-4]
                wfs_angle = float(f.split('_')[1])
                radial_distance = float(f.split('_')[2])
                delta_t = utils.cross_corr(file_path)/self.SAMPLE_RATE
                calc_angle = utils.two_mic_doa(delta_t, dis_mic, C)

                results['Radial_Distance'].append(radial_distance)
                results['Wfs_Angle'].append(wfs_angle)
                results['Delta_T'].append(delta_t)
                results['Calculated_Angle'].append(calc_angle)
                results['Error'].append(abs(wfs_angle-calc_angle))

        file_name = input('Enter .txt filename to write results to: ')
        with open(file_name, 'w+'):
            pass

        df = pd.DataFrame(data=results)
        with open(file_name, 'a') as f:
            f.write(df.to_string())
        print(f"SUCCESS: Saved results in {file_name}")
        return

    def process_trial(self, trial, separations, track_state : dict, results : dict, offsets=[0.0, 0.0], tracking=False):
        '''Helper funtion to run a trial in a 3D1U track.'''
        # Do experiment
        cmds = trial.splitlines()
        for _cmd in cmds:
            self.onecmd(_cmd)

        # For every input there should be two stored positions in queue
        assert(2 * len(self.input_queue) == len(self.pos_queue))

        # Calculate entries
        recorded_dir = self.input_queue[0]
        initial_pos = self.pos_queue[0]
        final_pos = self.pos_queue[1]
        distance = (initial_pos.split('/')[0] + f'+{str(offsets[1])}') if tracking else (np.round(float(initial_pos.split('/')[0]), 2) + offsets[1])
        init_angle = offsets[0]+ np.round(float(initial_pos.split('/')[-1]), 2)
        final_angle = offsets[0]+ np.round(float(final_pos.split('/')[-1]), 2)
        actual_dir = "right" if (final_angle - init_angle) >= 0 else "left"

        # Store entries in a dict
        results['Radial_Distance'].append(distance)
        results['Initial_Angle'].append(init_angle if not tracking else f'trkr+{init_angle}')
        results['Final_Angle'].append(final_angle if not tracking else f'trkr+{final_angle}')
        results['Separation'].append(track_state['sep'])
        results['Direction'].append(actual_dir)
        results["Recorded_Direction"].append(recorded_dir)
        results["Reversal"].append('-')

        # If correct Response
        if recorded_dir == actual_dir:
            track_state['correctInaRow'] += 1

            if track_state['correctInaRow'] == 3:  # three down
                track_state['sep_idx'] = min(track_state['sep_idx'] + 1, (len(separations) - 1))
                track_state['sep'] = separations[track_state['sep_idx']]
                track_state['correctInaRow'] = 0

                # If state previously stored is not down
                # Update state
                # Update reversal
                if track_state['state'] != -1:
                    track_state['state'] = -1
                    track_state['curr_reversals'] += 1
                    results["Reversal"][-1] = '*'

        # If incorrect Response
        elif recorded_dir != actual_dir:  # one up
            track_state['sep_idx'] = max(track_state['sep_idx'] - 1, 0)
            track_state['sep'] = separations[track_state['sep_idx']]
            track_state['correctInaRow'] = 0

            # If state previously stored is not up
            # Update state
            # Update reversal
            if track_state['state'] != 1:
                track_state['state'] = 1
                track_state['curr_reversals'] += 1
                results["Reversal"][-1] = '*'
        
        track_state['curr_run'] += 1

    def process_results(self, results : dict):
        '''Helper funtion to process the results of a 3D1U track.'''
        # Write results to text file
        file_name = input('Enter .txt filename to write results to: ')
        with open(file_name, 'w+'):
            pass

        df = pd.DataFrame(data=results)
        with open(file_name, 'a') as f:
            f.write(df.to_string())

        print(f"SUCCESS: Saved results in {file_name}")

        acc = np.mean([1 if a == b else 0 for a,
                      b in zip(results["Recorded_Direction"], results['Direction'])])
        print(f"Accuracy: {acc}\n")
    
    def return_to_defaults(self):
        '''Helper function to return to default state'''
        self.pos_queue.clear()
        self.input_queue.clear()
        p = preset_generator.PresetGenerator(self.NUM_SOURCES)
        to_default_cmds = p.return_to_default()
        cmds = to_default_cmds.splitlines()
        for _cmd in cmds:
            self.onecmd(_cmd)
        return


    def do_3D1U_ST_Random(self, arg):
        'Run the three-down-one-up experiment: 3D1U_ST_Random reversals lo_angle hi_angle distance'
        arg = arg.split()
        if len(arg) != 4:
            print("Error: see usage (hint: help 3D1U_ST_Random)")
            return
        try:
            reversals = int(arg[0])
            lo = float(arg[1])
            hi = float(arg[2])
            dist = float(arg[3])
            ranges = input("Enter ranges: ")
            ranges = [float(elem) for elem in ranges.split()]
            step_sizes = input("Enter step sizes: ")
            step_sizes = [float(elem) for elem in step_sizes.split()]
            separations = self.get_separations(ranges, step_sizes)
            repeats1 = input("Enter repetions for interval1: ")
            repeats1 = int(repeats1)
            repeats2 = input("Enter repetions for interval2: ")
            repeats2 = int(repeats2)
        except Exception as e:
            print(str(e))
            return

        results = {
            "Radial_Distance": [],
            "Initial_Angle": [],
            "Final_Angle": [],
            "Separation": [],
            "Direction": [],
            "Recorded_Direction": [],
            "Reversal": [],
        }

        # State Variables
        track_state = {
            'correctInaRow' : 0,
            'curr_reversals': 0,
            'curr_run': 0,
            'state': -1,
            'sep_idx': 0,
            'sep': separations[0]
        }

        p = preset_generator.PresetGenerator(self.NUM_SOURCES)

        while track_state['curr_reversals'] != reversals:
            self.pos_queue.clear()
            self.input_queue.clear()

            # Generate experiment
            if self.IPAD_AVAILABLE:
                trial = p.randomized_two_source(1, lo, hi, track_state['sep'], dist, 
                                                input_type='ipad', repeat1=repeats1, repeat2=repeats1)
            else:
                trial = p.randomized_two_source(1, lo, hi, track_state['sep'], dist, 
                                                input_type='keyboard', repeat1=repeats1, repeat2=repeats1)

            self.process_trial(trial, separations, track_state, results)

        self.process_results(results)
        # Return to init state
        self.return_to_defaults()
        return
    
    def do_3D1U_ST_Fixed(self, arg):
        'Run a variant of three-down-one-up experiment: 3D1U_FT_Fixed reversals target_angle distance'
        'untracked version: 3D1U_FT_Fixed reversals target_angle distance'
        'tracked version: 3D1U_FT_Fixed reversals'
        arg = arg.split()
        if not (len(arg) == 3 or len(arg) == 1):
            print("Error: see usage (hint: help 3D1U_ST_Fixed)")
            return
        
        tracking = len(arg) == 1


        try:
            reversals = int(arg[0])
            target_angle = None if tracking else float(arg[1]) 
            dist =  None if tracking else float(arg[2]) 
            offsets = '0.0 0.0' if not tracking else input("Enter angle and (normalized)radial offsets wrt tracker: ")
            offsets = [float(elem) for elem in offsets.split()] 
            ranges = input("Enter ranges: ")
            ranges = [float(elem) for elem in ranges.split()]
            step_sizes = input("Enter step sizes: ")
            step_sizes = [float(elem) for elem in step_sizes.split()]
            separations = self.get_separations(ranges, step_sizes)
            repeats1 = input("Enter repetions for interval1: ")
            repeats1 = int(repeats1)
            repeats2 = input("Enter repetions for interval2: ")
            repeats2 = int(repeats2)
        except Exception as e:
            print(str(e))
            print("Parse Error: Enter valid values")
            return

        results = {
            "Radial_Distance": [],
            "Initial_Angle": [],
            "Final_Angle": [],
            "Separation": [],
            "Direction": [],
            "Recorded_Direction": [],
            "Reversal": [],
        }

        # State Variables
        track_state = {
            'correctInaRow' : 0,
            'curr_reversals': 0,
            'curr_run': 0,
            'state': -1,
            'sep_idx': 0,
            'sep': separations[0]
        }

        p = preset_generator.PresetGenerator(self.NUM_SOURCES)

        while track_state['curr_reversals'] != reversals:
            self.pos_queue.clear()
            self.input_queue.clear()

            # Generate experiment
            inp_type = 'ipad' if self.IPAD_AVAILABLE else 'keyboard'
            trial = p.deterministic_two_source(1, target_angle, track_state['sep'], dist, 
                                               offsets=offsets, input_type=inp_type, repeat1=repeats1, repeat2=repeats2)

            self.process_trial(trial, separations, track_state, results, offsets=offsets, tracking=tracking)

        # Write results to text file
        self.process_results(results)
        # Return to init state
        self.return_to_defaults()
        return
    
    def do_3D1U_FT_Random(self, arg):
        'Run the three-down-one-up experiment: 3D1U_FT_Random runs lo_angle hi_angle distance'
        arg = arg.split()
        if len(arg) != 4:
            print("Error: see usage (hint: help 3D1U_FT_Random)")
            return

        try:
            runs = int(arg[0])
            lo = float(arg[1])
            hi = float(arg[2])
            dist = float(arg[3])
            ranges = input("Enter ranges: ")
            ranges = [float(elem) for elem in ranges.split()]
            step_sizes = input("Enter step sizes: ")
            step_sizes = [float(elem) for elem in step_sizes.split()]
            separations = self.get_separations(ranges, step_sizes)
            repeats1 = input("Enter repetions for interval1: ")
            repeats1 = int(repeats1)
            repeats2 = input("Enter repetions for interval2: ")
            repeats2 = int(repeats2)
        except Exception as e:
            print(str(e))
            print("Parse Error: Enter valid values")
            return

        results = {
            "Radial_Distance": [],
            "Initial_Angle": [],
            "Final_Angle": [],
            "Separation": [],
            "Direction": [],
            "Recorded_Direction": [],
            "Reversal": [],
        }

        # State Variables
        track_state = {
            'correctInaRow' : 0,
            'curr_reversals': 0,
            'curr_run': 0,
            'state': -1,
            'sep_idx': 0,
            'sep': separations[0]
        }

        p = preset_generator.PresetGenerator(self.NUM_SOURCES)

        while track_state['curr_run'] != runs:
            self.pos_queue.clear()
            self.input_queue.clear()

            # Generate experiment
            inp_type = 'ipad' if self.IPAD_AVAILABLE else 'keyboard'
            trial = p.randomized_two_source(1, lo, hi, track_state['sep'], dist, 
                                            input_type=inp_type, repeat1=repeats1, repeat2=repeats2)

            self.process_trial(trial, separations, track_state, results)

        # Write results to text file
        self.process_results(results)
        # Return to init state
        self.return_to_defaults()
        return

    def do_3D1U_FT_Fixed(self, arg):
        '''
        Run a variant of three-down-one-up experiment:\n
        \tuntracked version: 3D1U_FT_Fixed runs target_angle distance\n
        \ttracked version: 3D1U_FT_Fixed runs\n
        '''
        
        arg = arg.split()
        if not (len(arg) == 3 or len(arg) == 1):
            print("Error: see usage (hint: help 3D1U_FT_Fixed)")
            return
        
        tracking = len(arg) == 1

        try:
            runs = int(arg[0]) 
            target_angle = None if tracking else float(arg[1]) 
            dist =  None if tracking else float(arg[2])
            offsets = '0.0 0.0' if not tracking else input("Enter angle and (normalized)radial offsets wrt tracker: ")
            offsets = [float(elem) for elem in offsets.split()] 
            ranges = input("Enter ranges: ")
            ranges = [float(elem) for elem in ranges.split()]
            step_sizes = input("Enter step sizes: ")
            step_sizes = [float(elem) for elem in step_sizes.split()]
            separations = self.get_separations(ranges, step_sizes)
            repeats1 = input("Enter repetions for interval1: ")
            repeats1 = int(repeats1)
            repeats2 = input("Enter repetions for interval2: ")
            repeats2 = int(repeats2)
        except Exception as e:
            print(str(e))
            print("Parse Error: Enter valid values")
            return

        results = {
            "Radial_Distance": [],
            "Initial_Angle": [],
            "Final_Angle": [],
            "Separation": [],
            "Direction": [],
            "Recorded_Direction": [],
            "Reversal": [],
        }

        # State Variables
        track_state = {
            'correctInaRow' : 0,
            'curr_reversals': 0,
            'curr_run': 0,
            'state': -1,
            'sep_idx': 0,
            'sep': separations[0]
        }

        p = preset_generator.PresetGenerator(self.NUM_SOURCES)

        while track_state['curr_run'] != runs:
            self.pos_queue.clear()
            self.input_queue.clear()

            # Generate experiment
            inp_type = 'ipad' if self.IPAD_AVAILABLE else 'keyboard'
            trial = p.deterministic_two_source(1, target_angle, track_state['sep'], dist, 
                                               offsets=offsets, input_type=inp_type, repeat1=repeats1, repeat2=repeats2)

            self.process_trial(trial, separations, track_state, results, offsets=offsets, tracking=tracking)

        # Write results to text file
        self.process_results(results)

        # Return to init state
        self.return_to_defaults()
        return

    def do_3D1U_Interleaved(self, arg):
        'Run the interleaved three-down-one-up experiment: 3D1U_Interleaved runs soundfile0 soundfile1 ...'

        arg = arg.split()
        if len(arg) < 3:
            print("Error: see usage (hint: help 3D1U_Interleaved)")
            return
        try:
            runs = int(arg[0])
            soundfiles = arg[1:]
        except:
            print("Parse Error: Enter valid values")
            return

        state_dict = {}
        for sf in soundfiles:
            state_dict[sf] = {}
            params = input(
                f'Press enter if tracking else enter target_angle(f) distance(f) for {sf}: ')
            params = params.split()

            if not (len(params) == 2 or len(params) == 0):
                print("Error: see usage (hint: help 3D1U_Interleaved)")
                return
        
            state_dict[sf]['tracking'] = len(params) == 0

            try: 
                state_dict[sf]['target_angle'] = None if state_dict[sf]['tracking'] else float(params[0])
                state_dict[sf]['dist'] = None if state_dict[sf]['tracking'] else float(params[1])
                offsets = '0.0 0.0' if not state_dict[sf]['tracking'] else input(f"Enter angle and (normalized)radial offsets wrt tracker for {sf}: ")
                state_dict[sf]['offsets'] = [float(elem) for elem in offsets.split()] 
                ranges = input(f"Enter ranges for {sf}: ")
                ranges = [float(elem) for elem in ranges.split()]
                step_sizes = input(f"Enter step sizes for {sf}: ")
                step_sizes = [float(elem) for elem in step_sizes.split()]
                state_dict[sf]['separations'] = self.get_separations(ranges, step_sizes)
                repeats1 = input("Enter repetions for interval1: ")
                state_dict[sf]['repeats1'] = int(repeats1)
                repeats2 = input("Enter repetions for interval2: ")
                state_dict[sf]['repeats2'] = int(repeats2)
                
                state_dict[sf]['results'] = {
                    "Radial_Distance": [],
                    "Initial_Angle": [],
                    "Final_Angle": [],
                    "Separation": [],
                    "Direction": [],
                    "Recorded_Direction": [],
                    "Reversal": [],
                }

                state_dict[sf]['track_state'] = {
                    'correctInaRow' : 0,
                    'curr_reversals': 0,
                    'curr_run': 0,
                    'state': -1,
                    'sep_idx': 0,
                    'sep': state_dict[sf]['separations'][0]
                }
            except Exception as e:
                print(str(e))
                print("Parse Error: Enter valid values")
                return

        p = preset_generator.PresetGenerator(self.NUM_SOURCES)

        curr_run = 0
        while curr_run != runs:
            for sf in state_dict.keys():

                self.pos_queue.clear()
                self.input_queue.clear()

                # Generate experiment
                inp_type = 'ipad' if self.IPAD_AVAILABLE else 'keyboard'
                trial = p.deterministic_two_source(1, state_dict[sf]['target_angle'], 
                                                       state_dict[sf]['track_state']['sep'], 
                                                       state_dict[sf]['dist'], 
                                                       input_type=inp_type, filename=sf,
                                                       offsets=state_dict[sf]['offsets'],
                                                       repeat1=state_dict[sf]['repeats1'], 
                                                       repeat2=state_dict[sf]['repeats2'])

               

                self.process_trial(trial, state_dict[sf]['separations'], state_dict[sf]['track_state'], state_dict[sf]['results'],
                                   offsets=state_dict[sf]['offsets'], tracking=state_dict[sf]['tracking'])
            curr_run += 1

        for sf in state_dict.keys():
            # Write results to text file
            print(f"Processing {sf}...")
            self.process_results(state_dict[sf]['results'])

        # Return to init state
        self.return_to_defaults()
        return


if __name__ == '__main__':
    ExptShell().cmdloop()
