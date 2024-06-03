#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:22:12 2024

@author: puruboii
"""

import numpy as np
from queue import Queue


class PresetGenerator:

    def __init__(self, num_sources):
        self.cmdqueue = Queue(maxsize=0)
        self.num_sources = num_sources

    def set_pos(self, index, angle, distance):
        cmd = f"set_pos {index} {angle} {distance}\n"
        self.cmdqueue.put(cmd)

    def ipad_user_input(self):
        cmd = "ipad_user_input\n"
        self.cmdqueue.put(cmd)

    def key_user_input(self):
        cmd = "key_user_input\n"
        self.cmdqueue.put(cmd)

    def play(self):
        cmd = "play\n"
        self.cmdqueue.put(cmd)

    def unmute(self, index):
        cmd = f"unmute {index}\n"
        self.cmdqueue.put(cmd)

    def mute(self, index):
        cmd = f"unmute {index}\n"
        self.cmdqueue.put(cmd)

    def write(self, filename):
        with open(filename, "w+") as f:
            while not self.cmdqueue.empty():
                cmd = self.cmdqueue.get()
                f.write(cmd)

    def randomized_two_source(self, runs, lo, hi, sep, dist):

        input_fn = self.key_user_input
        #input_fn = self.ipad_user_input

        rand_angles = np.random.uniform(low=lo, high=hi, size=runs)
        for angle in rand_angles:
            angle1 = angle
            choice = np.random.choice([-1, 1])
            angle2 = angle1 + choice * sep
            angle2 = np.minimum(hi, np.maximum(angle2, lo))
            angle2 = angle1 - choice * \
                sep if abs(angle1-angle2) != sep else angle2

            self.set_pos(1, angle1, dist)
            self.play()
            self.set_pos(1, angle2, dist)
            self.play()
            input_fn()

        self.write("randomized_two_source.txt")
        return


# Usuage
# p = PresetGenerator(2)
# p.randomized_two_source(20, -60, 60, 5, 0.5)
