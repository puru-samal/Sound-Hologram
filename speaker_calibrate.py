# -*- coding: utf-8 -*-

import numpy as np
import scipy
import sounddevice as sd
import matplotlib.pyplot as plt
import test_signal as T
import cmd
import sys
import shutil
import os


class ExptShell(cmd.Cmd):
    intro = 'Experiment shell for Sound Hologram. Type help or ? to list commands.'
    prompt = '> '
    file = None
    Test = None
    sd.default.reset()
    sd.default.samplerate = 44100
    Test = T.LogSineSweep(sample_rate=sd.default.samplerate)
    Test.generate(dur=1.0, amp=0.1, zero_pad=0.0, repititions=1)
    gain_arr = None

    def do_quit(self, arg):
        'Exit the shell:  quit'
        #print('Thank you for using Turtle')
        self.close()
        return True

    def do_setIO(self, arg):
        """
        fmt: setIO input_index output_index sample_rate
        Set input/output devices. Do getIO if you are not sure about indexes
        """
        arg = arg.split()
        if len(arg) != 3:
            print("Error: missing args")
            return
        
        input_idx = int(arg[0])
        output_idx = int(arg[1])
        sample_rate = float(arg[2])
        try:
            self.set_IO(input_idx, output_idx, sample_rate)
        except:
            print("Unexpected Error: Retry")

    def do_getIO(self, arg):
        """
        fmt: getIO
        List available devices [> Input Device | < Output Device]
        """
        print('\n')
        print(sd.query_devices())
        print('\n')
        print(f"\tSample Rate: {sd.default.samplerate}")
        print('\n')
        print(f"\tDefault Test Signal: LogSineSweep dur=1.0 amp=1.0")

    def do_gen(self, arg):
        """
        fmt: gen dur amp zero_pad repititions 
        Generates a log sine sweep test signal with the given parameters.
        The default sample rate will be used.
        """
        if sd.default.samplerate == None:
            print("IO not set. Run setIO first!")
            return
        if self.Test != None:
            self.Test = None
        arg = arg.split()
        try:
            dur = float(arg[0])
            amp = float(arg[1])
            zpad = float(arg[2])
            reps = int(arg[3])
        except:
            print("Parse Error: Invalid arguments")
        self.Test = T.LogSineSweep(sample_rate=sd.default.samplerate)
        self.Test.generate(dur=dur, amp=amp, zero_pad=zpad, repititions=reps)

    def do_play(self, arg):
        """
        fmt: play [-c chan]
        Plays a generated test signal. gen must be run first.
        c -> [1....out_channels]
        Hint: help play
        """
        args = arg.split()
        channel_mapping = None
        if self.Test == None:
            print("Generate test signal first by running gTSig.")
        elif len(args) == 2 and args[0].lower() == '-c':
            channel_mapping = np.array([int(args[1])])
        else:
            out_channels = sd.query_devices(device=sd.default.device[1])[
                'max_output_channels']
            channel_mapping = np.arange(1, out_channels+1)

        sd.play(self.Test.signal, samplerate=sd.default.samplerate, mapping=channel_mapping,
                loop=False, blocking=True)

    def do_expt1(self, arg):
        """
        fmt: expt1 repititions
        Runs expt1
        """
        reps = int(arg)
        self.expt1(reps=reps)

    def set_IO(self, input_idx, output_idx, sample_rate):
        sd.default.device[0] = input_idx
        sd.default.device[1] = output_idx
        sd.default.samplerate = sample_rate

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def expt1(self, reps=6, amp_arr=None):

        # Make Directory and save Test Signal
        path = "expt1"
        path = os.path.join(os.getcwd(), path)
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)

        ##test_path = os.path.join(path, "Test.npy")
        ##np.save(test_path, self.Test.signal)

        in_channels = sd.query_devices(device=sd.default.device[0])[
            'max_input_channels']
        out_channels = sd.query_devices(device=sd.default.device[1])[
            'max_output_channels']
        in_channel_mapping = np.arange(1, in_channels+1)
        out_channel_mapping = np.arange(1, out_channels+1)
        
        out_channel_mapping = np.array([out_channel_mapping[54]])
        #gain = np.ones(out_channels+1) if gain_arr == None else gain_arr
        #gain_dict = {}
        for chans in out_channel_mapping:
            inp = input("Continue? (y/n): ")

            if inp.lower() == 'y':
                ch = np.array([chans])
                recordings = []
                for i in range(reps):
                    rec = sd.playrec(self.Test.signal, samplerate=sd.default.samplerate,
                                     input_mapping=in_channel_mapping,
                                     output_mapping=ch,
                                     blocking=True)
                    #rec /= np.max(np.abs(rec)) # -1.0 to 1.0
                    #avg_amp = np.mean(np.abs(rec))
                    wav_path = os.path.join(path, f"Rec-{ch[0]}-rep-{i}.wav")
                    scipy.io.wavfile.write(wav_path, int(sd.default.samplerate), rec)
                    recordings.append(rec)
        
                #avg_amp = np.mean(recordings)
                #gain_dict[chans] = avg_amp
                rec_path = os.path.join(path, f"Rec-{ch[0]}.npy")
                np.save(rec_path, np.array(recordings))
            elif inp.lower() == "n":
                return
            else:
                print("Invalid Input")
                continue

        # with open("calibrate.txt", 'w+') as f:
        #    for k, v in gain_dict.items():
        #       f.write(str(k) + ' >>> ' + str(v) + '\n\n')


if __name__ == '__main__':
    ExptShell().cmdloop()
