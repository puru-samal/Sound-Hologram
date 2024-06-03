#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:03:44 2024

@author: puruboii
"""

import numpy as np
import test_signal as T
import cmd
import sys
import shutil
import os
import time
import config
from osc4py3.as_allthreads import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
import logging
import subprocess
import preset_generator
from pathlib import Path
import pandas as pd
import queue

# Optional: A logger to monitor activity... and debug.
logging.basicConfig(format='%(asctime)s - %(threadName)s ø %(name)s - '
                    '%(levelname)s - %(message)s')
logger = logging.getLogger("osc")
logger.setLevel(logging.DEBUG)
logger = None


class ExptShell(cmd.Cmd):

    intro = 'Experiment shell for Sound Hologram. Type help or ? to list commands.'
    prompt = '> '

    IP = "127.0.0.1"    # Local Server
    CLIENT_PORT = 1338  # Sending Port
    SERVER_PORT = 1339  # Listening Port
    CLIENT = "PyToMax"
    SERVER = "MaxToPy"

    WIFI_CLIENT_IP = "10.0.0.65"  # Ipad's IP
    WIFI_SERVER_IP = "10.0.0.16"  # Computers IP
    WIFI_CLIENT_PORT = 1340       # Sending Port
    WIFI_SERVER_PORT = 1341       # Listening Port
    WIFI_CLIENT = "PyToIpad"
    WIFI_SERVER = "IpadToPy"

    NUM_SPEAKERS = 64
    YM = 3.617   # Horizontal Distance of 32-SPeaker from origin (Make Input)
    SP = 0.0587  # SPacing between SPeakers (Make Input)
    XPOS = np.arange(SP * -(NUM_SPEAKERS/2 - 1.0),
                     (NUM_SPEAKERS/2 + 1.0) * SP, SP)
    NUM_SOURCES = 1
    SAMPLE_RATE = 44100  # Make sure Max is set to the same

    # State
    IPAD_STATE = 'none'
    ACCEPT_IPAD_INPUT = False
    RECORD_FILE = None

    max_size = 500
    pos_queue = []
    input_queue = []
    msg_queue = queue.Queue()

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
        # p = subprocess.run(['pkill', '-x', 'Max'])

    def block_until_recieved(self):
        item = self.msg_queue.get()
        return item

    def check_conn(self):
        # Install message methods
        osc_method("/max/conn", self.max_conn, argscheme=osm.OSCARG_ADDRESS +
                   osm.OSCARG_DATAUNPACK)
        osc_method("/ipad/*", self.ipad_conn,
                   argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)

        # Send Message to Max
        msg = oscbuildparse.OSCMessage("/max/conn", ",s", ["Sent"])
        osc_send(msg, self.CLIENT)

    ############################
    ####    SHELL CMDs      ####
    ############################

    def do_quit(self, arg):
        'Exit the shell:  quit'
        print('Thank you!')
        self.close()
        return True

    def do_open_max(self, arg):
        'Open Max/MSP: open_max'
        p = subprocess.run(['open', 'wfs.maxpat'])

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

            # Initialize Client
            osc_udp_client(self.WIFI_CLIENT_IP, self.WIFI_CLIENT_PORT,
                           self.WIFI_CLIENT)
            # Initialize Server
            osc_udp_server(self.WIFI_SERVER_IP, self.WIFI_SERVER_PORT,
                           self.WIFI_SERVER)

            self.check_conn()
            self.block_until_recieved()
            print("SUCCESS: Connection established.")
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
        if test_file.is_file():
            msg = oscbuildparse.OSCMessage(
                "/playback-file/open", ",s", [arg[0]])
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

    def do_set_record_file(self, arg):
        'Set filepath to record: set_record_file filepath'
        arg = arg.split()
        if len(arg) != 1:
            print("Error: see usage (hint: help test_signal)")
            return

        filename = os.path.join(os.getcwd(), arg[0])

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
        self.RECORD_FILE = arg[0]
        return

    def do_play_rec(self, arg):
        'Play/Record: play_rec filename duration(ms)'
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

        self.do_set_record_file(filename)

        print("Play/Recording...")
        attr = self.pos_queue[-1].split('/')
        print(f"\tSource     : Dist:{attr[0]} | Angle:{attr[-1]}")
        print(f"\tRecord File: {self.RECORD_FILE}")

        # Playback
        msg = oscbuildparse.OSCMessage(
            "/play-rec/record", ",i", [rec_dur])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
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

    def do_ipad_user_input(self, arg):
        if len(self.input_queue) > self.max_size // 2:
            self.input_queue.clear()

        self.ACCEPT_IPAD_INPUT = True
        msg = oscbuildparse.OSCMessage(
            "/ipad/centre/", ",f", [1.0])
        osc_send(msg, self.WIFI_CLIENT)

        ipad_state = self.block_until_recieved().split('/')[-1]
        self.input_queue.append(ipad_state)

        msg = oscbuildparse.OSCMessage(
            "/ipad/centre/", ",f", [0.0])
        osc_send(msg, self.WIFI_CLIENT)
        self.ACCEPT_IPAD_INPUT = False
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
                continue

    def do_write(self, arg):
        'Write result of experiment to file: playback filename'

        arg = arg.split()

        if len(arg) != 1:
            print("Error: see usage (hint: help write)")
            return

        assert(2 * len(self.input_queue) == len(self.pos_queue))

        file_name = arg[0]

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

        self.pos_queue.clear()
        self.input_queue.clear()
        return

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
        p.randomized_two_source(runs, lo, hi, sep, dist)
        self.do_playback("randomized_two_source.txt")
        return


if __name__ == '__main__':
    ExptShell().cmdloop()
