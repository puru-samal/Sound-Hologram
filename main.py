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

# Optional: A logger to monitor activity... and debug.
logging.basicConfig(format='%(asctime)s - %(threadName)s ø %(name)s - '
                    '%(levelname)s - %(message)s')
logger = logging.getLogger("osc")
logger.setLevel(logging.DEBUG)
logger = None

# Message handler for server connection test

MSG_SUCCESS = False


def conn_test(*args):
    global MSG_SUCCESS
    if logger and logger.isEnabledFor(logging.INFO):

        MSG_SUCCESS = True
        logger.info("##### %d handler function called with: %r",
                    1, args)

    else:
        MSG_SUCCESS = True
        #print("SUCCESS: Message recieved.")


class ExptShell(cmd.Cmd):

    intro = 'Experiment shell for Sound Hologram. Type help or ? to list commands.'
    prompt = '> '
    IP = "127.0.0.1"  # Local Server
    CLIENT_PORT = 1338
    CLIENT = "PyToMax"
    SERVER_PORT = 1339
    SERVER = "MaxToPy"
    NUM_SPEAKERS = 64
    YM = 3.617   # Horizontal Distance of 32-SPeaker from origin (Make Input)
    SP = 0.0587  # SPacing between SPeakers (Make Input)
    XPOS = np.arange(SP * -(NUM_SPEAKERS/2 - 1.0),
                     (NUM_SPEAKERS/2 + 1.0) * SP, SP)
    NUM_SOURCES = 2
    SAMPLE_RATE = 48000  # Make sure Max is set to the same
    TEST_SIG_FILENAME = "test_signal.wav"
    SOURCE_POS_DICT = {}

    # HELPERS

    def close(self):
        osc_terminate()
        p = subprocess.run(['pkill', '-x', 'Max'])

    def block_until_recieved(self):
        print("Waiting...", sep="")
        global MSG_SUCCESS
        while not MSG_SUCCESS:
            # TODO: Add timeout (w/ SIGALARM maybe?)
            continue

        MSG_SUCCESS = False

    def check_conn(self):
        osc_method("*", conn_test, argscheme=osm.OSCARG_DATAUNPACK)
        # Send Message to Max
        msg = oscbuildparse.OSCMessage("/test/conn", ",s", ["Hello"])
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
            self.check_conn()
            self.block_until_recieved()
            print("SUCCESS: Connection established.")

        except:
            print("Error initializing")
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
            self.SOURCE_POS_DICT[i+1] = [angles[i], 0, self.YM/2]

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
        self.block_until_recieved()
        print("SUCCESS: spat5.wfs~ initialized.")
        return

    def do_test_signal(self, arg):
        'Generate Test Signal: test_signal num[0:test_signal.wav 1:sine_sweep, 2:white_noise]'

        arg = arg.split()

        if len(arg) != 1:
            print("Error: see usage (hint: help test_signal)")
            return

        try:
            sig_type = int(arg[0])
        except:
            print("Parse Error: Enter valid integer")
            return

        if not (sig_type == 0 or sig_type == 1 or sig_type == 2):
            print("Error: signal type not supported. see usage (hint: help test_signal)")
            return

        # TODO: Add support for custom test signal via filename
        if sig_type == 1 or sig_type == 2:
            params = input(
                "Enter test signal dur, amp, zero-padding and repititions: ")
            params = params.split()

            if sig_type == 1:
                Test = T.LogSineSweep(sample_rate=self.SAMPLE_RATE)
            else:
                Test = T.WhiteNoise(sample_rate=self.SAMPLE_RATE)

            try:
                Test.generate(dur=float(params[0]),
                              amp=float(params[1]),
                              zero_pad=float(params[2]),
                              repititions=int(params[3]))
            except:
                print("Error.")
                return

            # Write to file
            Test.write(self.TEST_SIG_FILENAME)

        msg = oscbuildparse.OSCMessage(
            "/playfile/open", ",s", [self.TEST_SIG_FILENAME])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        print("SUCCESS: test signal set.")

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

        msg = oscbuildparse.OSCMessage(
            f"/set-source/source/{idx}/aed", ",fff", [angle, 0, dist*self.YM])
        osc_send(msg, self.CLIENT)
        self.block_until_recieved()
        self.SOURCE_POS_DICT[idx][0] = angle
        self.SOURCE_POS_DICT[idx][-1] = dist

    def do_play_wfs(self, arg):
        'Plays all unmuted sources: play'

        print("Playing...")
        for k, v in self.SOURCE_POS_DICT.items():
            print(f"\tSource{k}: Angle:{v[0]} | Dist:{v[-1]}")

        # Playback
        msg = oscbuildparse.OSCMessage(
            "/playback", ",i", [1])
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

        mute = 1

        if idx == 0:
            msg = oscbuildparse.OSCMessage(
                "/set-source/source/*/mute", ",i", [mute])
            osc_send(msg, self.CLIENT)
        else:
            msg = oscbuildparse.OSCMessage(
                f"/set-source/source/{idx}/mute", ",i", [mute])
            osc_send(msg, self.CLIENT)

        self.block_until_recieved()

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

        self.block_until_recieved()

    def do_playback(self, arg):
        'Playback commands from a file: playback expt.txt'
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def do_random_two_source(self, arg):
        'Run the random two source experiment: random_two_source runs lo hi sep dist'

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

        p = preset_generator.PresetGenerator(self.NUM_SOURCES)
        p.randomized_two_source(runs, lo, hi, sep, dist)
        self.do_playback("randomized_two_source.txt")


if __name__ == '__main__':
    ExptShell().cmdloop()
