from music21 import *
import matplotlib.pyplot as plt

def process_midi(file_path):
    try:
        # Load the MIDI file
        midi_file = converter.parse(file_path)
        print(f"Successfully loaded: {file_path}")

        # Initialize data containers
        pitches = []  # MIDI pitch numbers
        note_names = []  # Note names
        durations = []  # Durations of notes
        offsets = []  # Timing information

        # Extract relevant data from the MIDI file
        for element in midi_file.flat.notes:
            if isinstance(element, note.Note):
                pitches.append(element.pitch.midi)  # MIDI pitch value
                note_names.append(str(element.nameWithOctave))  # Note name and octave
                durations.append(element.quarterLength)  # Duration in quarter lengths
                offsets.append(element.offset)  # Time offset in quarter lengths

        # Check if we have data
        if not pitches:
            print("No notes found in the MIDI file.")
            return

        # Create plots
        create_plots(pitches, note_names, durations, offsets)

    except Exception as e:
        print(f"Error processing MIDI file: {e}")

def create_plots(pitches, note_names, durations, offsets):
    # Plot 1: Pitch Histogram
    # plt.figure(figsize=(10, 5))
    # plt.hist(pitches, bins=range(min(pitches), max(pitches) + 2), color='skyblue', edgecolor='black')
    # plt.xlabel("MIDI Pitch Number")
    # plt.ylabel("Frequency")
    # plt.title("Pitch Histogram")
    # plt.grid(axis='y', linestyle='--', alpha=0.7)
    # plt.show()

    # Plot 2: Note Durations Bar Chart
    # plt.figure(figsize=(12, 5))
    # plt.bar(note_names, durations, color='coral', edgecolor='black')
    # plt.xlabel("Notes")
    # plt.ylabel("Duration (quarter lengths)")
    # plt.title("Note Durations")
    # plt.xticks(rotation=45, ha='right')
    # plt.grid(axis='y', linestyle='--', alpha=0.7)
    # plt.tight_layout()
    # plt.show()

    # Plot 3: Melody Line Graph
    plt.figure(figsize=(12, 5))
    plt.plot(offsets, pitches, marker='o', linestyle='-', color='purple')
    plt.xlabel("Time (quarter lengths)")
    plt.ylabel("Pitch (MIDI number)")
    plt.title("Melody Line Graph")
    plt.grid()
    plt.show()

# File path to the MIDI file
file_path = "music1.mid"

# Run the processing and plotting function
process_midi(file_path)
