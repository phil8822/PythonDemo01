# Script: MidiExample.py
# Author: Grok (created on 06/01/2025)
# Description: Generates a C major scale (C4 to C5) in MIDI format and plays it directly using the system's synthesizer.
# Dependencies: mido (for MIDI file creation), python-rtmidi (for MIDI playback)
# Usage: Run the script to create 'c_major_scale.mid' and play the scale through the default MIDI output port.

from mido import MidiFile, MidiTrack, Message, open_output
import time

# Record start time to measure computation duration (excludes playback)
start_time = time.time()

# Initialize a MIDI file with one track for the C major scale
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Define MIDI note numbers for the C major scale (C4=60, D4=62, ..., C5=72)
c_major = [60, 62, 64, 65, 67, 69, 71, 72]

# Add each note to the track as a quarter note (480 ticks at 120 BPM)
for midi_note in c_major:
    # Send note-on message (velocity 64 = medium loudness, time 0 = immediate start)
    track.append(Message("note_on", note=midi_note, velocity=64, time=0))
    # Send note-off message after 480 ticks (1 beat duration for a quarter note)
    track.append(Message("note_off", note=midi_note, velocity=64, time=480))

# Save the MIDI file to disk for reference (optional step)
mid.save("c_major_scale.mid")

# Calculate computation time (excludes playback duration)
end_time = time.time()
computation_time = end_time - start_time

# Play the MIDI file directly using the system's default MIDI output port
with open_output() as outport:
    for msg in mid.play():
        outport.send(msg)

# Display the computation time (in seconds, 8 decimal places) and a confirmation message
print(f"Computation time: {computation_time:.8f} seconds")
print("C major scale played directly! Check 'c_major_scale.mid' for reference.")
