from music21 import *  # Import the music21 library for music composition


def height_to_frequency(height_ratio, base_freq=261.63):
    """
    Convert height ratio to a frequency.
    The default base frequency corresponds to middle C (C4 ~ 261.63 Hz).
    """
    freq = base_freq * height_ratio
    return freq


def frequency_to_nearest_chromatic_note(freq):
    """
    Find the nearest chromatic note for a given frequency.
    Maps the frequency to the closest pitch in the standard chromatic scale.
    """
    chromatic_notes = {
        'C': 261.63, 'C#': 277.18, 'D': 293.66, 'D#': 311.13, 'E': 329.63,
        'F': 349.23, 'F#': 369.99, 'G': 392.00, 'G#': 415.30, 'A': 440.00,
        'A#': 466.16, 'B': 493.88
    }

    # Find the closest note by comparing frequency differences
    closest_note = min(chromatic_notes, key=lambda note: abs(chromatic_notes[note] - freq))
    return closest_note


def architecture_to_music():
    """
    Converts architectural properties into music.
    Uses the ratios of arch heights and building width to determine pitch and tempo.
    """
    print("Welcome to the Architecture-to-Music Composer!")

    # Step 1: Collect user input for architecture properties
    try:
        num_arches = int(input("Enter the number of arches: "))
        arch_width = float(input("Enter the width of each arch (in meters): "))
        building_width = float(input("Enter the width of the building (in meters): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Step 2: Validate user input
    if num_arches <= 0 or arch_width <= 0 or building_width <= 0:
        print("All inputs must be positive numbers.")
        return

    # Step 3: Calculate the arches-to-building width ratio
    arches_to_building_ratio = arch_width / building_width
    print(f"Arches to Building Width Ratio: {arches_to_building_ratio:.2f}")

    # Step 4: Adjust tempo based on the width ratio
    default_tempo = 120  # Default tempo in beats per minute
    target_ratio = 0.1  # Reference ratio for ideal adjustment
    scale = 3  # Amplification factor for tempo changes

    if arches_to_building_ratio != target_ratio:
        # Adjust tempo based on deviation from the target ratio
        tempo_multiplier = 1 + (target_ratio - arches_to_building_ratio) * scale
        adjusted_tempo = int(default_tempo * tempo_multiplier)
        adjusted_tempo = max(60, min(adjusted_tempo, 200))  # Clamp tempo between 60 and 200 bpm
    else:
        adjusted_tempo = default_tempo

    print(f"Adjusted Tempo: {adjusted_tempo} bpm")

    # Step 5: Create a new music composition
    composition = stream.Stream()
    composition.append(meter.TimeSignature('4/4'))  # Add a 4/4 time signature
    composition.append(tempo.MetronomeMark(number=adjusted_tempo))  # Add the adjusted tempo

    # Step 6: Collect arch heights from the user
    arch_heights = []
    for i in range(num_arches):
        try:
            height = float(input(f"Enter the height of arch {i + 1} (in meters): "))
            arch_heights.append(height)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

    # Step 7: Define a helper function to calculate pitch from height ratio
    def calculate_pitch(height_ratio):
        freq = height_to_frequency(height_ratio)
        pitch = frequency_to_nearest_chromatic_note(freq)
        return pitch

    # Step 8: Generate musical notes for each arch
    for i, height in enumerate(arch_heights):
        # Calculate the height ratio relative to the first arch
        height_ratio = height / arch_heights[0]
        pitch = calculate_pitch(height_ratio)

        # Create a new note with the calculated pitch
        new_note = note.Note(pitch)
        new_note.quarterLength = 1  # Set note duration to 1 beat
        composition.append(new_note)

    # Step 9: Display and play the generated music
    print("Generated Music:")
    composition.show('text')  # Display the notes as text
    composition.show('midi')  # Play the composition as MIDI

    # Step 10: Save the composition to a MIDI file
    file_name = "music1.mid"
    composition.write('midi', fp=file_name)
    print(f"Music composition saved as '{file_name}'.")


# Execute the program
architecture_to_music()
