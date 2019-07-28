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
The Drum page allows users to sequence percusive sounds in the order they choose. You can have 8 unique drum sounds at once per measure.
There are four different measures that you can loop in any asscending combination. At any time you are able to modify and customize each
pattern to choose which percusive sound you would like to sequence.

## Drum Sequencer
![Drum sequencer](https://github.com/samuelbigio/DrumLooper/blob/master/Main/MISC/drumsequencer.png)

In a grid of (16x8) boxes this is where you choose the order your music will play. 


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
The Drum Kit sounds are the yellow circles on the left most side of the page. This allow users to preview the current
percusive sound in each row per pattern allowing the user to know what sound they are sequence. 

## Modify DrumKits
The Modify Drum page allows you to change sounds of each measure of your drum loop. Note that each measure has a different kit but they 
all start on a stock kit.
![ModDrums](https://github.com/samuelbigio/DrumLooper/blob/master/Main/MISC/ModDrums.png)

#### Drum Kits
Each Drum kit represents a folder in the game directory *Sounds*. The game takes each folder in that directory and allows
the user to pick different pre assembled kits. For example the Neptune Kit is a sound pack from the music group
[The Neptunes](https://en.wikipedia.org/wiki/The_Neptunes). 

#### Drum Kit Sounds
The Drum Kit sounds are buttons that represent a percusive sound in the respective drum kit.

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
In Music a adding a dot to a note elongates it by 1.5. [See Subdivision for the Theory](https://github.com/samuelbigio/DrumLooper/#subdivisions)

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
the in game time signature is in 4/4, what this means is that the quarter note gets the beat and there are four of them in a measure. An 
Eigth note requires eigth notes in a 4/4 time signautre to complete a measure. An eigth note is half of a quarter note. 1/8 of a meausre
instead of 1/4. In music each downbeat is a counted as a beat in a measure. For example, a measure with four quarter notes are counted as 1 2 3 4. If there are eigth notes in a whole measure these will be counted as "One and two and three and four and", finally the way
to subdivde 16th notes is by placing an "e" and an "a" sound in a measure. A measure with 16th notes is written in the following
>>1 e + a, 2 e + a, 3 e + a, 4 e + a  
![Subdivisions](https://github.com/samuelbigio/DrumLooper/blob/master/Main/MISC/subdivision.png)

#### Dotted Notes
Dotted notes allow music to add half the value of the note to the orginal value. For example a half note is worth 2 beats, *half of a 4 beat measure*, if you add a dot to a half note you will have 2 x 1.5 = 3 or 3 beats. 


#### Rest
Rest are to denote where music is not played. When counting subdivisions in music this is skipped so a quarter note on beat 1 of a measure with a dotted half measure (*3 rest*) will be only counted as 1. This is the same way a whole note will be counted but the whole note will be sustained for four beats opposed to the quarter note being *relased* at the end of beat 1. 

### BPM
BPM stands for beats per minute. A BPM of 60 means that there are 60 beats in a minute, or 1 beat per second. In a 4/4 time signature at 60 BPM one measure is 4 seconds. In a 144 BPM measure how many seconds are in a beat? 

>> 60/144 x 4 = 1.666 seconds in a measure. 

### Semitone
There are 12 different notes in western music 

>> C C# D D# E F F# G G# A A# B  

Each note has a distance of one semitone. The *#* in music are also known as accidentinals. These accidentals represent black keys on 
a normal piano. 

![Piano](https://github.com/samuelbigio/DrumLooper/blob/master/Main/MISC/piano.png)

Each time a C is repeated it is a new octave or 12 semitones apart. C4 is the fourth C in music. Each musical pitch is a different frequency. The faster a note cycles the higher pitch it will sound. The international music standard is having A4 at 440 Hz. In order to represent a semitone in music every note above middle C, *C4* is n  
>> 440 * 2<sup>(n-9)/12 </sup>  
There is a great wikipedia article on this [Scientific pitch notation](https://en.wikipedia.org/wiki/Scientific_pitch_notation)

### Octave
An octave is 12 semitones higher or lower than a given pitch. To raise an octave the frequency of a note is doubled and to lower an octave the frequency of a note is halved. 

### Intervals
In music the distance between notes are called intervals. The intervals are a ratio of the pitch, or frequency. For example an octave interval is the ratio 2:1, double the frequency. A *Perfect fith* is 3/2.  

|Name|Ratio|Number of Semitones|
|---|---|---|
|Perfect Unison |1:1 |0|
|Minor second | 16:15|1|
|Major Second|9:8 |2|
|Minor third|6:5 |3|
|Major third|5:4 |4|
|Perfect Fourth|4:3 |5|
|Augmented fourth|45:32 |6|
|Perfect Fifth|3:2 |7|
|Minor Sixth|8:5 |8|
|Major Sixth|5:3 |9|
|Minor Seventh|16:9 |10|
|Major Seventh|15:8 |11|
|Perfect Octave|2:1 |12|

  [Interval Music](https://en.wikipedia.org/wiki/Interval_(music))

### Scales
In music you can create scales with different steps between each note to form a pattern. A note asscending in one semitone is known as a *half* step while a note with two semitones is known as a *whole* step. A major scale has the pattern of
>> Whole, Whole Half, Whole, Whole, Whole, Half

Take for instance a C note as a root, (also known as tonic) of a scale. 
A whole step from a C or two semitones would Be C -> ~~D#~~ -> __D__  
You can do this with the whole scale to yeild all Natural notes, *notes without accidentals*,
>> C D E F G A B 
  This corresponds to all the white keys on a keyboard.

A scale starting at C# would yeild all accidetals
>> C# D# E F# G# A# B C
  A minor scale has the steps  
>> Whole Half Whole Whole Half Whole (*augmented*, 3 semitones), Half

>> C D D# F G G# A# C

If you drop a root two semitones down then you would yeild the relative minor. What this means is the key signature, how many accidentals in the scale, is the same. The relative minor to a C major scale is an A minor. An A minor is  

>> A B C D E F G A

All the white keys in a key signature but the intervals are not following the minor scale progression because of the root note.



# Installing
[Zip With .exe](https://drive.google.com/open?id=1FV62ySMou_qc5eepr1XvZnzHq8_OVCsl)


