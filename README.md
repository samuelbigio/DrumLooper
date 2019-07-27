# DrumLooper

By Samuel Bigio


Table of Contents
==================
[Installing](https://github.com/samuelbigio/DrumLooper/#installing)  
[Drum Page](https://github.com/samuelbigio/DrumLooper/#drum)  
[Synth Page](https://github.com/samuelbigio/DrumLooper/#synth)  
[Play Both](https://github.com/samuelbigio/DrumLooper/#playboth)  
[Learning](https://github.com/samuelbigio/DrumLooper/#learning)  

# Drums
## Drum Sequencer
![Drum sequencer](https://github.com/samuelbigio/DrumLooper/blob/master/Main/MISC/drumsequencer.png)



#### Grid
Each Row in the grid represents a different instrument and each column is a subdivision of that measure.
See [Subdivisions](https://github.com/samuelbigio/DrumLooper/#Subdivisions) to understand what this means musically.
The Grid allows you to pick which sounds you would like to play and when you would like to sequence them. 
Note that each column is played at once. 

#### Play (n)
The Play (n) Button takes the current Measure and captures the state of the (16 x 8) grid sequence and plays the created beat

#### Play 
The Play button plays every measure that is toggled *on*. For example the first measure and the fourth measure could have a green toggle
so the Play button would skip the second and third measure. Note that if there isn't any measures toggled on then the
first measure will play by default.

#### Copy
The Copy Button allows a user to copy the states of the grid.
#### Paste
The Paste Button allows a user to paste a previously copied measure into the current measure.
#### Clear
The Clear button sets all the states to off in the respective measure and turns the measure toggle to *off*.
#### Measures
The Measure button represents a musical measure. Each different measure can have a seperate pattern.
The paterns are played in ascending order. If more than one measure toggle button is on than the Play (n) button will loop the respective
measures.

#### BPM Dial
The BPM Dial stands for Beats Per Minute. You can increase the dial or decrease it to have a slower or faster song. 
See [BPM Dial In Learning](https://github.com/samuelbigio/DrumLooper/#bpm) to understand the theory behind this.

#### Play Sound button
The eight circles on the left of the grid repesents each different instrument. You can test the sound in each of them if they are pressed.

## Modify DrumKits
The Modify Drum page allows you to change sounds of each measure of your drum loop. Note that each measure has a different kit but they 
all start on a stock kit.
![ModDrums](https://github.com/samuelbigio/DrumLooper/blob/master/Main/MISC/ModDrums.png)

#### Drum Kits
Each Drum kit represents a folder in the game directory *Sounds*. The game takes each folder in that directory and allows
the user to pick different pre assembled kits. For example the Neptune Kit is a sound pack from the music group
[The Neptunes](https://en.wikipedia.org/wiki/The_Neptunes). 

#### Drum Kit Sounds
The Drum Kit sounds are buttons that represent a sound in the respective drum kit.

#### Load
When the Load button is pressed this sound is loaded in the respective measures sound. This represent a sound in the row of the current
measures grid. For example the *LoConga* Sound can be loaded off of the *808* Drum kit in measure 3 of row 1. Whenever a button
in row 1 is played it will play the *LoConga* sound only if the measure 3 is selected.
#### Save Kit
Save Kit allows a user to save the current measures kit into 8 different slots. The first and the last kit start as stock but can
be overwritten. This allows a user to make a kit in pattern 1 and save the kit to load it into a different pattern without having to 
remake it. This allows users to customize different ktis in different patterns. 

#### SetAll
The SetAll button takes the current loaded instruments in the current measure and sets those instruments to all the measures. 
This is used if a user creates a kit and wants to use it for the other measures without recreating it again, or without
saving the kit in *Saved Kits* and reloading it in each pattern.

#### Saved Kits
This is a list of 8 different slots for a user to save a kit they created

#### Load Preset Kit (k) to (n)
When a saved Kit is selected the load Preset Kit (k) will allow you to load a kit to the respective measure.
This allows the user to load a created kit into a different measure if they want or reload the stock kit into the current measure n. 


# Synth
![Synth Page](https://github.com/samuelbigio/DrumLooper/blob/master/Main/MISC/Synth.png)


### Scale
The Scale button allows a user to have a guide on what notes are in a respective scale. For example if the root is set to C and the Major scale
is selected a user will see what notes fall into a C Major scale. This is a guide to help the users create a melody without needing
knowledge of key signatures and the theory behind the scales. This is also another way to help users understand how key signatures are made.


### Root *(note)*

The Root button allows you to set the root of the scale. So if the Major scale button is pressed the user can see the notes in 
a C major Scale, but if the user wants to see the notes in a C# major Scale then the user needs to set the Root to C#.


### Octaves
[see Octave In Learning for the Theory](https://github.com/samuelbigio/DrumLooper/#octave)


### Rythms
The set Rythms in this game are Whole Notes, Half Notes, Quarter Notes, Eigth Notes, and Sixteenth Notes. 
[See Subdivision for the Theory](https://github.com/samuelbigio/DrumLooper/#subdivisions)


#### Dotted Notes
In Music a adding a dot to a note elongates it by 1.5.[See Subdivision for the Theory](https://github.com/samuelbigio/DrumLooper/#subdivisions)

#### Rest
The Rest button allows a user to toggle between adding a note of the respective duration or a rest for that duration.

### Grid
Contrary to the [Drum Sequencer](https://github.com/samuelbigio/DrumLooper/#drum) grid, the columns in this grid are 
not played simultaneously. The grid is subdivided into 16 rows and the columns represent a different measure, this layout
is similar to how sheet music is read. 

### Insert

If a user hovers over the respective measure 16 white boxes will appear to represent place in the measure. A user can then select 
a rythm and insert that in any place. If the user inserts a note in between an existing note the existing note will be truncated. If the 
existing note was longer than the note inserted is going to last then the existing note will resume after the insert note is completed.
In other words if there is a Whole note that is inserted and the user inserts a quarter note in the second beat of the measure then the
new state will be a quarter note that was truncated into the second measure since the quarter note only last one beat the remaining two
beats will the old note that was there which in this case will be a half note because two beats are left. If you are new to music
this concept may be challenging but the program is created to give you a visual representation. If you insert a note the state before 
the insertion is capturted and the user will be able to click undo. After the Undo button is pressed the user can choose to redo.

### Keyboard HotKeys
The Synth page has hotkeys added to create a better user experience.  
  <kbd>tab</kbd> -> Switch to the next scale  
  <kbd>a</kbd> -> Move left on the selected rythm  
  
  <kbd>d</kbd> -> Move right on the selected rythm
  
  <kbd>w</kbd> -> Move upwards on the selected note. Keep in mind if a scale is selected
  the next note that is selected will be the next note in the scale.
  
  <kbd>s</kbd> -> Move Downwards on the selected note. See above 
  
  
  
  <kbd>0</kbd> -> <kbd>8</kbd> Change between respective octave
  
  <kbd>r</kbd> -> Toggle between *rest* and *note*
  
  
  <kbd>.</kbd> -> Toggle between *Dotted note/rest* and *Not Dotted note/rest*

### Play 
The Play Button Plays the notes dictated by the user in the grid



# PlayBoth
![Play Both](https://github.com/samuelbigio/DrumLooper/blob/master/Main/MISC/PlayBoth.png)
Once the Synth Page is opened then the user can see a new window on the main menu.
When this is selected the user can hit the play button and hear the created drum patterns and synth melody
simultaneously. Note that if the user had empty measures that were toggled in the drum sequencer page these will play regardless.

### Design
A design will be shown when the play button is selected. This design is very quick and the user has the ability to turn this off. 
Also, the user is prompted if they are epileptic and if they choose that they are the desing will not come.


# Learning
### Subdivisions
There are 16 horizontal buttons in the grid so the measure is divided in 16th notes. 
Every four beats is a quarter of the measure, or a quarter note. The quarter note is the downbeat for this grid because
the music is in 4/4, what this means is that the quarter note gets the beat and there are four of them in a measure.
In music this is known as a time signature and 4/4 is known as common time.  

#### Dotted Notes
#### Rest


### BPM

### Octave

# Installing
[Zip With .exe](https://drive.google.com/open?id=1FV62ySMou_qc5eepr1XvZnzHq8_OVCsl)
