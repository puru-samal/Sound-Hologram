# Sound-Hologram
A repository of scripts and programs for the Sound-Hologram Project at CMU

# Files:
* config-init.txt   
  - Initial state of Spat5.wfs~
  
* config.txt           
  - Init state of Spat5.wfs~ extended with number of speakers and sources. 
  - Set with main.py
  
* config.py            
  - Helper file that uses config-init and creates config.txt at runtime.
  
* main.py              
  - The main experiment shell that handles client-server interaction with wfs.maxpat
  
* speaker-calibrate.py 
  - An experiment shell that interfaces directly with the speakers.
  - Used to play-record test signals for speaker amplitude calibration.
  
* test_signal.py       
  - A helper file to generate test signals. 
  - Currenly supports LogSineSweeps and White Noise.
  
* test_expt.txt        
  - A sequence of commands to main.py can be 'played back' using valid .txt files.
  - This file provides an example of one such use.
  
* wfs.maxpat           
  - The Max patch that implements wavefield synthesis.
  - Also implements simultaneous playback-recording.
  - Controlled by main.py.
  
* preset_generator.py
  - Script to generate text files with sequence of commands to run experiments. 
                       

# OSC Addresses
* `/playback-file`         | fmt: `,s` | filename :
* `/play`                  | fmt: `,i` | state :
* `/play-rec`              | fmt: `,i` | state :
* `/set-source/*`          | fmt:      |
* `/init-spat/preset/load` | fmt:`,s`  | filename : 
* `/max/conn`              | fmt:        

# Usage
## main.py
### Commands

* `open_max`
  - Opens wfs.maxpat. Dependencies must be installed for its proper operation.
  
* `init_conn`
  - Initializes the client-server connection between Max and Python.
  
* `init_wfs`
  - Initializes the state of the wfs system.
  
* `test_signal num` 
  - Specifies the test_signal to be used for playback.
    - Arguments:
      - num : Specifies the test signal to be used.
        - 0 : Uses test_signal.wav present in the parent directory
        - 1 : Generates a user-specified LogSineSweep signal 
        - 2 : Generates a user-specified WhiteNoise signal 
        - For the user-specified signal, user's will have to specify
          - dur         (float) : duration of the signal (in seconds)
          - amp         (float) : amplitude of the signal
          - zero_pad    (float) : duration of padding applied to front/back (in seconds) 
          - repititions   (int) : number of repititions of the signal
  
* `set_pos idx angle dist`
  - Sets the position of a source.
    - Arguments: 
      - idx     (int) : Index of the source position [1..Num Sources] 
      - angle (float) : Angle in degrees [-90...90]
      - dist  (float) : Ratio of the source. Is multiplied by YM
      
* `play`
  - Plays the test_signal in the current configuration.
  
* `mute idx`
  - Mutes a source.
    - Arguments: 
      - idx (int) : Index of the source position [1..Num Sources]
  
* `unmute idx`
  - Unmutes a source.
    - Arguments: 
      - idx (int) : Index of the source position [1..Num Sources]
  
* `plaback filename`
  - Plays back a .txt file containing a sequence of commands.
    - Arguments: 
      - filename : A text file with a sequence of commands.
  
* `random_two_source runs lo hi sep dist`
  - Runs the sequence of commands for the random_two_source experiment.
    - Arguments: 
      - runs   (int) : Number of iterations
      - lo   (float) : Lower angle range in degrees
      - hi   (float) : Upper angle range in degrees
      - sep  (float) : The separation between two sources
      - dist (float) : Ratio of the source. Is multiplied by YM

* `quit` 
  - Quits the shell


### Example usage w/ 2 sources
```
open_max       # Wait for Max to open
init_conn 
init_spat
test_signal 0
unmute 0      # Unmute all sources, all sources are muted by default
set_pos 1 -90 0.3
set_pos 2 90 0.3
play_wfs
set_pos 1 -60 0.6 
set_pos 2 60 0.6
play_wfs
quit
```
### Example running commands stored in a .txt file
```
open_max       # Wait for Max to open
init_conn 
init_spat
test_signal 0
unmute 0      # Unmute all sources, all sources are muted by default
playback filename.txt
```

### Example running the random_two_source experiment with ipad input
```
open_max       # Wait for Max to open
init_conn 
init_spat
test_signal 0
unmute 0      # Unmute all sources, all sources are muted by default
random_two_source 10 -30.0 30.0 5.0 0.5
```


