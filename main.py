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

# Optional: A logger to monitor activity... and debug.
logging.basicConfig(format='%(asctime)s - %(threadName)s ø %(name)s - '
                    '%(levelname)s - %(message)s')
logger = logging.getLogger("osc")
logger.setLevel(logging.DEBUG)
logger = None


class ExptShell(cmd.Cmd):

    intro = 'Experiment shell for Sound Hologram. Type help or ? to list commands.'
    prompt = '> '

    IP = "127.0.0.1"   # Local Server
    CLIENT_PORT = 1338  # Sending Port
    SERVER_PORT = 1339  # Listening Port
    CLIENT = "PyToMax"
    SERVER = "MaxToPy"

    WIFI_CLIENT_IP = "10.0.0.65"  # Ipad's IP
    WIFI_CLIENT_PORT = 1340
    WIFI_SERVER_IP = "10.0.0.16"  # Computers IP
    WIFI_SERVER_PORT = 1341
    WIFI_CLIENT = "PyToIpad"
    WIFI_SERVER = "IpadToPy"

    NUM_SPEAKERS = 64
    YM = 3.617   # Horizontal Distance of 32-SPeaker from origin (Make Input)
    SP = 0.0587  # SPacing between SPeakers (Make Input)
    XPOS = np.arange(SP * -(NUM_SPEAKERS/2 - 1.0),
                     (NUM_SPEAKERS/2 + 1.0) * SP, SP)
    NUM_SOURCES = 1
    SAMPLE_RATE = 48000  # Make sure Max is set to the same
    TEST_SIG_FILENAME = "test_signal.wav"

    # State
    MAX_SUCCESS = False
    IPAD_SUCCESS = False
    IPAD_STATE = 'none'

    max_size = 500
    pos_queue = []
    input_queue = []

    def max_conn(self, *args):
        if logger and logger.isEnabledFor(logging.INFO):

            logger.info("##### %d handler function called with: %r",
                        1, args)
            self.MAX_SUCCESS = True

        else:
            self.MAX_SUCCESS = True

    def ipad_conn(self, addr, x):
        st = addr.split("/")[-1]
        if addr != 'centre':
            assert(int(x) == 1)
            self.IPAD_STATE = st

        if logger and logger.isEnabledFor(logging.INFO):

            logger.info("##### %d handler function called with: %r",
                        1, x)
            self.IPAD_SUCCESS = True

        else:
            self.IPAD_SUCCESS = True

    # HELPERS

    def close(self):
        osc_terminate()
        p = subprocess.run(['pkill', '-x', 'Max'])

    def block_until_recieved(self, dest):
        print("...", sep="")
        if dest == "max":
            while not self.MAX_SUCCESS:
                continue
            self.MAX_SUCCESS = False
            return

        elif dest == "ipad":
            while not self.IPAD_SUCCESS:
                continue
            self.IPAD_SUCCESS = False
            return
        else:
            print("Invalid Destination!")

    def check_conn(self):

        # Install message methods
        osc_method("/max/conn", self.max_conn, argscheme=osm.OSCARG_ADDRESS +
                   osm.OSCARG_DATAUNPACK)
        osc_method("/ipad/*", self.ipad_conn,
                   argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)

        # Send Message to Max
        msg = oscbuildparse.OSCMessage("/max/conn", ",s", ["Sent"])
        osc_send(msg, self.CLIENT)

    # SHELL CMDs

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
            self.block_until_recieved("max")
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

        # TODO: Handle error if config_init doesnot exist

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
        self.block_until_recieved("max")
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
                "/playback-file/open", ",s", [self.TEST_SIG_FILENAME])
            osc_send(msg, self.CLIENT)
            self.block_until_recieved("max")
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
        self.block_until_recieved("max")
        self.pos_queue.append(f'{dist}/{angle}')

    def do_play_wfs(self, arg):
        'Plays all unmuted sources: play'

        print("Playing...")
        attr = self.pos_queue[-1].split('-')
        print(f"\tSource: Dist:{attr[0]} | Angle:{attr[-1]}")

        # Playback
        msg = oscbuildparse.OSCMessage(
            "/play", ",i", [1])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved("max")

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

        mute = 1

        if idx == 0:
            msg = oscbuildparse.OSCMessage(
                "/set-source/source/*/mute", ",i", [mute])
            osc_send(msg, self.CLIENT)
        else:
            msg = oscbuildparse.OSCMessage(
                f"/set-source/source/{idx}/mute", ",i", [mute])
            osc_send(msg, self.CLIENT)

        self.block_until_recieved("max")

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

        mute = 0

        if idx == 0:
            msg = oscbuildparse.OSCMessage(
                "/set-source/source/*/mute", ",i", [mute])
            osc_send(msg, self.CLIENT)
        else:
            msg = oscbuildparse.OSCMessage(
                f"/set-source/source/{idx}/mute", ",i", [mute])
            osc_send(msg, self.CLIENT)

        self.block_until_recieved("max")

    def do_playback(self, arg):
        'Playback commands from a file: playback expt.txt'
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def do_user_input(self, arg):
        if len(self.input_queue) > self.max_size // 2:
            self.input_queue.clear()
        msg = oscbuildparse.OSCMessage(
            "/ipad/centre/", ",f", [1.0])
        osc_send(msg, self.WIFI_CLIENT)
        self.block_until_recieved("ipad")
        msg1 = oscbuildparse.OSCMessage(
            f"/ipad/{self.IPAD_STATE}/", ",f", [0.0])
        msg2 = oscbuildparse.OSCMessage(
            "/ipad/centre/", ",f", [0.0])
        bun = oscbuildparse.OSCBundle(oscbuildparse.OSC_IMMEDIATELY,
                                      [msg1, msg2])
        osc_send(bun, self.WIFI_CLIENT)
        self.input_queue.append(self.IPAD_STATE)
        return

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
