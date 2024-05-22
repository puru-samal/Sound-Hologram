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

    def play_wfs(self):
        cmd = "play_wfs\n"
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

        if self.num_sources < 2:
            print("Error: wfs initialized with < 2 sources. Reinit.")
            return

        rand_angles = np.random.uniform(low=lo, high=hi, size=runs)
        for angle in rand_angles:
            angle1 = angle
            angle2 = np.minimum(hi, np.maximum(angle1+sep, lo))
            angle2 = angle1 - sep if abs(angle1-angle2) != sep else angle2

            self.set_pos(1, angle1, dist)
            self.set_pos(2, angle2, dist)
            self.play_wfs()

        self.write("randomized_two_source.txt")
        return


# Usuage
# p = PresetGenerator(2)
# p.randomized_two_source(20, -60, 60, 5, 0.5)