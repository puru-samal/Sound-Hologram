#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:48:55 2024

@author: puruboii
"""

import numpy as np


class Speakers:

    def __init__(self, num_speakers):

        self.num_speakers = num_speakers
        self.config = None
        self.tag = "/speaker"

        self.init_config()

    def __len__(self):
        return self.num_speakers

    def init_config(self):
        self.config = {}
        self.config[f'{self.tag}/number'] = {'type': ",i",
                                             "value": [self.num_speakers]}

        self.config[f'{self.tag}/*/visible'] = {'type': ",i", "value": [1]}
        self.config[f'{self.tag}/*/editable'] = {'type': ",i", "value": [0]}
        self.config[f'{self.tag}/*/label/visible'] = {'type': ",i", "value": [1]}
        self.config[f'{self.tag}/*/proportion'] = {'type': ",f",
                                                   "value": [1.0]}

    def set_speaker_pos(self, idx, xyz):

        if idx < 1 or idx > self.num_speakers:
            raise Exception(
                f'Invalid argument. Valid range: 1 <= idx <= {self.num_speakers}')

        if not isinstance(xyz, list) or len(xyz) != 3:
            raise Exception("Invalid argument. Format: [x, y, z]")

        self.config[f'{self.tag}/{idx}/xyz'] = {'type': ",fff", "value": xyz}

    def toStrList(self):

        L = []

        for addr, v in self.config.items():
            valList = v['value']
            string = f'{addr} {" ".join(str(i) for i in valList)}\n'
            L.append(string)

        return L


class Sources:

    def __init__(self, num_sources):

        self.num_sources = num_sources
        self.config = None
        self.tag = "/source"
        self.init_config()

    def __len__(self):
        return self.num_sources

    def init_config(self):
        self.config = {}
        self.config[f'{self.tag}/number'] = {'type': ",i",
                                             "value": [self.num_sources]}

        self.config[f'{self.tag}/*/visible'] = {'type': ",i", "value": [1]}
        self.config[f'{self.tag}/*/editable'] = {'type': ",i", "value": [1]}
        self.config[f'{self.tag}/*/coordinates/visible'] = {'type': ",i", "value": [1]}
        self.config[f'{self.tag}/*/label/visible'] = {'type': ",i", "value": [1]}
        self.config[f'{self.tag}/*/mute'] = {'type': ",i", "value": [1]}

    def set_source_pos(self, idx, aed):

        if idx < 1 or idx > self.num_sources:
            raise Exception(
                f'Invalid argument. Valid range: 1 <= idx <= {self.num_speakers}')

        if not isinstance(aed, list) or len(aed) != 3:
            raise Exception("Invalid argument. Format: [a, e, d]")

        self.config[f'{self.tag}/{idx}/aed'] = {'type': ",fff", "value": aed}

    def toStrList(self):

        L = []

        for addr, v in self.config.items():
            valList = v['value']
            string = f'{addr} {" ".join(str(i) for i in valList)}\n'
            L.append(string)

        return L


'''
num_speakers = 64
speakers = Speakers(num_speakers)
yM = 10.0  # Horizontal Distance of first-speaker from origin (Make Input)
sp = 2.0  # Spacing between speakers (Make Input)

xpos = np.arange(sp * -(num_speakers/2 - 1.0), (num_speakers/2 + 1.0) * sp, sp)
for i in range(speakers.num_speakers):
    speakers.set_speaker_pos(i+1, [xpos[i], 10.0, 0.0])

List = speakers.toStrList()
'''
