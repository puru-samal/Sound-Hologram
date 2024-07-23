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
    
    def set_offset_rel_tracker(self, index, angle_offset, radial_offset):
        cmd = f"set_offset_rel_tracker {index} {angle_offset} {radial_offset}\n"
        self.cmdqueue.put(cmd)

    def set_pos_rel_tracker(self, index, separation):
        cmd = f"set_pos_rel_tracker {index} {separation}\n"
        self.cmdqueue.put(cmd)
    
    def set_tracking(self, tracker_state):
        cmd = f"set_tracking {tracker_state}\n"
        self.cmdqueue.put(cmd)

    def ipad_user_input(self):
        cmd = "ipad_user_input\n"
        self.cmdqueue.put(cmd)

    def set_ipad_tab(self, page):
        cmd = f"set_ipad_tab {page}\n"
        self.cmdqueue.put(cmd)

    def key_user_input(self):
        cmd = "key_user_input\n"
        self.cmdqueue.put(cmd)

    def test_signal(self, filename):
        cmd = f"test_signal {filename}\n"
        self.cmdqueue.put(cmd)

    def play(self):
        cmd = "play\n"
        self.cmdqueue.put(cmd)

    def play_rec(self, filename, dur):
        cmd = f"play_rec {filename} {dur}\n"
        self.cmdqueue.put(cmd)

    def unmute(self, index):
        cmd = f"unmute {index}\n"
        self.cmdqueue.put(cmd)

    def mute(self, index):
        cmd = f"unmute {index}\n"
        self.cmdqueue.put(cmd)
    
    def loop(self, loop_state):
        cmd = f"loop {loop_state}\n"
        self.cmdqueue.put(cmd)

    def num_loop(self, numreps):
        cmd = f"num_loop {numreps}\n"
        self.cmdqueue.put(cmd)

    def set_two_speaker(self, idx1, idx2):
        cmd = f"set_speaker {idx1} {idx2}\n"
        self.cmdqueue.put(cmd)

    def write_random_two_source(self):
        cmd = "write_random_two_source\n"
        self.cmdqueue.put(cmd)

    def process_cross_corr(self, directory):
        cmd = f"process_cross_corr {directory}\n"
        self.cmdqueue.put(cmd)

    def write_to_str(self):
        string = ''
        while not self.cmdqueue.empty():
            cmd = self.cmdqueue.get()
            string += cmd
        return string
    
    def return_to_default(self):
        self.set_tracking(0)
        self.set_pos(1, 0.0, 0.5)
        self.set_ipad_tab(0)
        return self.write_to_str()
        
    def randomized_two_source(self, runs, lo, hi, sep, dist, repeat1 = 0, repeat2= 0, input_type='keyboard', filename=None):
        if input_type == 'keyboard':
            input_fn = self.key_user_input
        elif input_type == 'ipad':
            input_fn = self.ipad_user_input

        rand_angles = np.random.uniform(low=lo, high=hi, size=runs)
        for angle in rand_angles:
            angle1 = angle
            choice = np.random.choice([-1, 1])
            angle2 = angle1 + choice * sep
            angle2 = np.minimum(hi, np.maximum(angle2, lo))
            angle2 = angle1 - choice * \
                sep if abs(angle1-angle2) != sep else angle2

            if filename is not None:
                self.test_signal(filename)

            self.set_pos(1, angle1, dist)
            if repeat1 > 0:
                self.num_loop(repeat1)
                self.loop(1)     
            self.play()
            self.set_pos(1, angle2, dist)
            if repeat2 > 0:
                self.num_loop(repeat2)
                self.loop(1)    
            self.play()
            input_fn()

        return self.write_to_str()

    def deterministic_two_source(self, runs, target_angle, sep, dist, repeat1=0, repeat2=0, offsets=[0.0, 0.0], input_type='keyboard', filename=None, tab=None):
        if input_type == 'keyboard':
            input_fn = self.key_user_input
        elif input_type == 'ipad':
            input_fn = self.ipad_user_input

        tracking = target_angle is None and dist is None

        if tab is not None:
            self.set_ipad_tab(tab)
        
        if tracking:
            self.set_tracking(1)

        for run in range(runs):
            rand = -1 if np.random.randint(2) == 0 else 1  # 1 or -1
            sep1 = rand * (sep / 2)
            sep2 = -sep1
            angle1 = None if tracking else target_angle + sep1
            angle2 = None if tracking else target_angle + sep2

            if filename is not None:
                self.test_signal(filename)
            
            if not tracking:
                self.set_pos(1, angle1, dist)
            else:
                self.set_offset_rel_tracker(1, *offsets)
                self.set_pos_rel_tracker(1, sep1)

            if repeat1 > 0:
                self.num_loop(repeat1)
                self.loop(1)     
            self.play()
            
            if not tracking:
                self.set_pos(1, angle2, dist)
            else:
                self.set_pos_rel_tracker(1, sep2)
            
            if repeat2 > 0:
                self.num_loop(repeat2)
                self.loop(1)    
            self.play()
            
            input_fn()

        return self.write_to_str()

    def doa_expt(self, lo_angle, hi_angle, lo_dist, hi_dist, angle_interval, distance_interval, rec_dur, rec_dir):

        angles = np.linspace(lo_angle, hi_angle,
                             int((hi_angle-lo_angle)/angle_interval + 1),
                             endpoint=True)

        distances = np.linspace(lo_dist, hi_dist,
                                int((hi_dist-lo_dist)/distance_interval + 1),
                                endpoint=True)

        for dist in distances:
            for angle in angles:
                self.set_pos(1, angle, dist)
                self.play_rec(f'{rec_dir}/doa_{angle}_{dist}.wav', rec_dur)

        return self.write_to_str()

    def spaced_pair_lag(self, num_speakers, rec_dir):

        for sp in range(num_speakers//2):
            self.set_two_speaker(sp, (num_speakers-1) - sp)
            self.play_rec(
                f'{rec_dir}/{sp}_{(num_speakers-1) - sp}.wav', 1000)

        return self.write_to_str()


# Usuage
# p = PresetGenerator(2)
# p.randomized_two_source(20, -60, 60, 5, 0.5)
