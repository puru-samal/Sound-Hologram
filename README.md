# Sound-Hologram
A repository of scripts and programs for the Sound-Hologram Project at CMU

Files:
config-init.txt      - Initial state of Spat5.wfs~
config.txt           - Init state of Spat5.wfs~ extended with number of speakers and sources. 
                       Set with main.py
config.py            - Helper file that uses config-init and creates config.txt at runtime.
main.py              - The main experiment shell that handles client-server interaction with wfs.maxpat
speaker-calibrate.py - An experiment shell that interfaces directly with the speakers.
                       Used to play-record test signals for speaker amplitude calibration.
test_signal.py       - A helper file to generate test signals. 
                       Currenly supports LogSineSweeps and White Noise.
test_expt.txt        - A sequence of commands to main.py can be 'played back' using valid .txt files.
                       This file provides an example of one such use.
test_signal.wav      - The file that will be played by wfs.maxpat. Can be replaced with any file.
                       As long as the name used is same, Max will play it. 
wfs.maxpat           - The Max patch that implements wavefield synthesis.
                       Also implements simultaneous playback-recording.
                       Controlled by main.py.
                       






 

