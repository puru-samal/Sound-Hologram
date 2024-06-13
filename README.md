# Sound-Hologram
A repository of scripts and programs for the Sound-Hologram Project at CMU

# Files:
* calibration_gains.txt   
  - Collection of speaker gain values from latest calibration experiment

* config-init.txt   
  - Initial state of Spat5.wfs~
  
* config.txt           
  - Init state of Spat5.wfs~ extended with number of speakers and sources. 
  - Set with main.py
  
* config.py            
  - Helper file that uses config-init and creates config.txt at runtime.
  
* cross_corr.py            
  - Helper file to calculate cross-correlation between channels in a stereo audio file.
  - A parabolic interpolator is used to estimate true peak location.

* doa.py            
  - Helper file to run two mic DOA estimation and plot results.
  
* main.py              
  - The main experiment shell that handles client-server interaction with wfs.maxpat

* preset_generator.py
  - Script to generate text files with sequence of commands to run experiments. 
  
* speaker-calibrate.py 
  - An experiment shell that interfaces directly with the speakers.
  - Used to play-record test signals for speaker amplitude calibration.
  
* test_signal.py       
  - A helper file to generate test signals. 
  - Currenly supports LogSineSweeps and White Noise.
  
* wfs.maxpat           
  - The Max patch that implements wavefield synthesis.
  - Also implements simultaneous playback-recording.
  - Controlled by main.py.
  

# OSC Addresses
* `/playback-file`         | fmt: `,s`    | filename
* `/record-file`           | fmt: `,s`    | filename
* `/play`                  | fmt: `,i`    | state
* `/play-rec`              | fmt: `,i`    | state
* `/set-source/*`          | fmt: `,fff`  | angle elevation distance
* `/init-spat/preset/load` | fmt: `,s`    | filename
* `/max/conn`              | fmt: `,i`    | 1 or 0   
* `/speaker-ch`            | fmt: `,ii..` | List of ints representing active speakers
# Usage
## main.py
### Commands
  
* `init_conn`
  - Initializes the client-server connection between Max and Python.
  - Prompts to optionally set up iPad for input recording instead of keyboard.
  
* `init_wfs`
  - Initializes the state of the wfs system.
  
* `test_signal filename` 
  - Specifies the test_signal to be used for playback.
    - Arguments:
      - filename : The file to be used for playbacl
        - The audio file may be resampled to match Max's sampling rate
  
* `set_pos idx angle dist`
  - Sets the position of a source.
    - Arguments: 
      - idx     (int) : Index of the source position [1..Num Sources] 
      - angle (float) : Angle in degrees [-90...90]
      - dist  (float) : Ratio of the source. Is multiplied by YM

* `set_speaker speaker_idx0 speaker_idx1 ..`
  - Sets the active speakers. All other speakers will be muted.
  - Max must be in Speaker Out mode (patch includes a button to toggle between modes)! 
    - Arguments: 
      - idx(s) (int(s)) : Index of the speakers [0..Num Speakers-1] 
      
* `play`
  - Plays the test_signal in the current configuration.
  

* `play-rec filename duration`
  - Plays and records a signal.
  - Arguments: 
    - filename (str) : filename of recording
    - duration (int) : Duration (in ms) to record for
  
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
      - dist (float) : Distance of the source. Expressed as a ration of YM.
      
* `spaced_pair_lag rec_dir`
  - Runs the sequence of commands for the spaced_pair_lag expt.
  - Used to validate mic position to run the doa_expt.
    - Arguments: 
      - rec_dir   (str) : Directory to record the files to

* `doa_expt lo_angle hi_angle lo_dist hi_dist angle_interval distance_interval rec_dur rec_dir`
  - Runs the sequence of commands for the doa_expt.
    - Arguments: 
      - lo_angle       (float) : Lower angle range in degrees
      - hi_angle       (float) : Upper angle range in degrees
      - lo_dist        (float) : Lower distance range as ration of YM
      - hi_dist        (float) : Upper distance range as ratio of YM
      - angle_interval (float) : Angle increments
      - dist_interval  (float) : Distance increments
      - rec_dur          (int) : Duration (in ms) to record for
      - rec_dir          (str) : Directory to record the files to

* `three_down_one_up reversals lo_angle hi_angle dist start_separation`
  - Runs the sequence of commands for the three_down_one_up experiment.
    - Arguments: 
      - reversals           (int) : Number of reversals before termination
      - lo_angle          (float) : Lower angle range in degrees
      - hi_angle          (float) : Upper angle range in degrees
      - dist              (float) : Ratio of the source. Is multiplied by YM
      - start_separation  (float) : The initial separation between two sources
     
* `quit` 
  - Quits the shell


### Example usage (Make sure wfs.maxpat is open!)
```
init_conn 
init_spat
test_signal 0
unmute 0      # Unmute all sources, all sources are muted by default
set_pos 1 -90 0.3
play
set_pos 1 -60 0.6 
play
quit
```
### Example running commands stored in a .txt file (Make sure wfs.maxpat is open!)
```
init_conn 
init_spat
test_signal 0
unmute 0      # Unmute all sources, all sources are muted by default
playback filename.txt
```

### Example running the random_two_source experiment (Make sure wfs.maxpat is open!)
```
init_conn 
init_spat
test_signal 0
unmute 0      # Unmute all sources, all sources are muted by default
random_two_source 10 -30.0 30.0 5.0 0.5
```


