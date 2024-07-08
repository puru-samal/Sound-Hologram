# Sound-Hologram

A repository of scripts and programs for the Sound-Hologram Project at CMU

# Files:

- calibration_gains.txt

  - Collection of speaker gain values from latest calibration experiment

- config-init.txt
  - Initial state of Spat5.wfs~
- config.txt
  - Init state of Spat5.wfs~ extended with number of speakers and sources.
  - Set with main.py
- config.py
  - Helper file that uses config-init and creates config.txt at runtime.
- utils.py

  - Collection of helper functions.

- main.py

  - The main experiment shell that handles client-server interaction with wfs.maxpat

- preset_generator.py
  - Script to generate text files with sequence of commands to run experiments.
- test_signal.py
  - A helper file to generate test signals.
  - Currenly supports LogSineSweeps and White Noise.
- wfs.maxpat
  - The Max patch that implements wavefield synthesis.
  - Also implements simultaneous playback-recording.
  - Controlled by main.py.

# OSC Addresses

- `/playback-file` | fmt: `,s` | filename
- `/record-file` | fmt: `,s` | filename
- `/play` | fmt: `,i` | state
- `/play-rec` | fmt: `,i` | state
- `/set-source/*` | fmt: `,fff` | angle elevation distance
- `/init-spat/preset/load` | fmt: `,s` | filename
- `/max/conn` | fmt: `,i` | 1 or 0
- `/speaker-ch` | fmt: `,ii..` | List of ints representing active speakers

# Usage

## main.py

### Commands

- `init_conn`
  - Initializes the client-server connection between Max and Python.
  - Prompts to optionally set up iPad for input recording instead of keyboard.
- `init_wfs`
  - Initializes the state of the wfs system.
- `test_signal filename`
  - Specifies the test_signal to be used for playback.
    - Arguments:
      - filename : The file to be used for playbacl
        - The audio file may be resampled to match Max's sampling rate
- `set_pos idx angle dist`

  - Sets the position of a source.
    - Arguments:
      - idx (int) : Index of the source position [1..Num Sources]
      - angle (float) : Angle in degrees [-90...90]
      - dist (float) : Ratio of the source. Is multiplied by YM

- `set_speaker speaker_idx0 speaker_idx1 ..`
  - Sets the active speakers. All other speakers will be muted.
  - Max must be in Speaker Out mode (patch includes a button to toggle between modes)!
    - Arguments:
      - idx(s) (int(s)) : Index of the speakers [0..Num Speakers-1]
- `play`

  - Plays the test_signal in the current configuration.

- `play-rec filename duration`
  - Plays and records a signal.
  - Arguments:
    - filename (str) : filename of recording
    - duration (int) : Duration (in ms) to record for
- `mute idx`
  - Mutes a source.
    - Arguments:
      - idx (int) : Index of the source position [1..Num Sources]
- `unmute idx`
  - Unmutes a source.
    - Arguments:
      - idx (int) : Index of the source position [1..Num Sources]
- `plaback filename`
  - Plays back a .txt file containing a sequence of commands.
    - Arguments:
      - filename : A text file with a sequence of commands.
- `random_two_source runs lo hi sep dist`
  - Runs the sequence of commands for the random_two_source experiment.
    - Arguments:
      - runs (int) : Number of iterations
      - lo (float) : Lower angle range in degrees
      - hi (float) : Upper angle range in degrees
      - sep (float) : The separation between two sources
      - dist (float) : Distance of the source. Expressed as a ration of YM.
- `spaced_pair_lag rec_dir`

  - Runs the sequence of commands for the spaced_pair_lag expt.
  - Used to validate mic position to run the doa_expt.
    - Arguments:
      - rec_dir (str) : Directory to record the files to

- `doa_expt lo_angle hi_angle lo_dist hi_dist angle_interval distance_interval rec_dur rec_dir`

  - Runs the sequence of commands for the doa_expt.
    - Arguments:
      - lo_angle (float) : Lower angle range in degrees
      - hi_angle (float) : Upper angle range in degrees
      - lo_dist (float) : Lower distance range as ration of YM
      - hi_dist (float) : Upper distance range as ratio of YM
      - angle_interval (float) : Angle increments
      - dist_interval (float) : Distance increments
      - rec_dur (int) : Duration (in ms) to record for
      - rec_dir (str) : Directory to record the files to

- `3D1U_ST_Random reversals lo_angle hi_angle dist`

  - Runs the sequence of commands for a variant of the three_down_one_up experiment.
  - Will prompt for ranges and step-sizes to support variable step-sizes.
    - Arguments:
      - reversals (int) : Number of reversals before termination
      - lo_angle (float) : Lower angle range in degrees
      - hi_angle (float) : Upper angle range in degrees
      - dist (float) : Ratio of the source. Is multiplied by YM
      - start_separation (float) : The initial separation between two sources

- `3D1U_FT_Random runs lo_angle hi_angle dist`

  - Runs the sequence of commands for a variant of the three_down_one_up experiment.
  - Will prompt for ranges and step-sizes to support variable step-sizes.
    - Arguments:
      - runs (int) : Number of runs before termination
      - lo_angle (float) : Lower angle range in degrees
      - hi_angle (float) : Upper angle range in degrees
      - dist (float) : Ratio of the source. Is multiplied by YM

- `3D1U_ST_Fixed reversals target_angle dist`

  - Runs the sequence of commands for a variant of the three_down_one_up experiment.
  - Will prompt for ranges and step-sizes to support variable step-sizes.
    - Arguments:
      - reversals (int) : Number of reversals before termination
      - target_angle (float) : Angle around which the two sources will be separated around.
      - dist (float) : Ratio of the source. Is multiplied by YM

- `3D1U_FT_Fixed runs target_angle dist`

  - Runs the sequence of commands for a variant of the three_down_one_up experiment
  - Will prompt for ranges and step-sizes to support variable step-sizes.
    - Arguments:
      - runs (int) : Number of runs before termination
      - target_angle (float) : Angle around which the two sources will be separated around.
      - dist (float) : Ratio of the source. Is multiplied by YM

- `3D1U_Interleaved runs soundfile0 soundfile1 ..`
  - Runs the sequence of commands for a variant of the three_down_one_up experiment.
    - Arguments:
      - runs (int) : Number of runs before termination
      - list of soundfiles (str) : Space separated list of soundfiles
- `quit`
  - Quits the shell

### 3D1U Variants

- Self-Terminating (ST) refers to when a track terminates after a user-specified number of reversals.
- Fixed-Trial refers to when a track terminates after a user-specified number of trials.
- Random-interval refers to when the two source locations in a trial are sampled randomly
  within the user-specified interval. The separation is determined by their performance in 3D1U.
  The order of playback (right-left, left-right) is random.
- Fixed-interval refers to when the target angle is user-specified and fixed throughout the
  duration of a track. The two source locations in a trial are separated around the target angle.
  The separation is determined by their performance in 3D1U.
  The order of playback (right-left, left-right) is random.
- All variants will prompt for input to generate variable step sizes. User will be prompted to enter ranges and step-sizes for each range. Eg. range: '20 10 4 1', steps: '5 3 1' generates separations '20 15 10 7 4 3 2 1'.

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
