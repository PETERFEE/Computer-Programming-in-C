import pygame
import time
import mido
from pygame.locals import QUIT

# Initialize pygame
pygame.init()

# Set up screen dimensions and window
screen_width = 900  # Width of the window
screen_height = 100  # Height of the window for better text display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MIDI Note Display")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font for displaying note names
font = pygame.font.SysFont("Arial", 24)

# Initialize pygame mixer
pygame.mixer.init()

# Load the MIDI file
midi_file = 'music1.mid'  # Use the provided MIDI file name

# Load MIDI using mido
midi = mido.MidiFile(midi_file)

# Global variables
playing_notes = set()  # Set of currently playing notes

# Note-to-name mapping
MIDI_NOTE_NAMES = {
    21: 'A0', 22: 'A#0', 23: 'B0', 24: 'C1', 25: 'C#1', 26: 'D1', 27: 'D#1', 28: 'E1', 29: 'F1', 30: 'F#1',
    31: 'G1', 32: 'G#1', 33: 'A1', 34: 'A#1', 35: 'B1', 36: 'C2', 37: 'C#2', 38: 'D2', 39: 'D#2', 40: 'E2',
    41: 'F2', 42: 'F#2', 43: 'G2', 44: 'G#2', 45: 'A2', 46: 'A#2', 47: 'B2', 48: 'C3', 49: 'C#3', 50: 'D3',
    51: 'D#3', 52: 'E3', 53: 'F3', 54: 'F#3', 55: 'G3', 56: 'G#3', 57: 'A3', 58: 'A#3', 59: 'B3', 60: 'C4',
    61: 'C#4', 62: 'D4', 63: 'D#4', 64: 'E4', 65: 'F4', 66: 'F#4', 67: 'G4', 68: 'G#4', 69: 'A4', 70: 'A#4',
    71: 'B4', 72: 'C5', 73: 'C#5', 74: 'D5', 75: 'D#5', 76: 'E5', 77: 'F5', 78: 'F#5', 79: 'G5', 80: 'G#5',
    81: 'A5', 82: 'A#5', 83: 'B5', 84: 'C6', 85: 'C#6', 86: 'D6', 87: 'D#6', 88: 'E6', 89: 'F6', 90: 'F#6',
    91: 'G6', 92: 'G#6', 93: 'A6', 94: 'A#6', 95: 'B6', 96: 'C7', 97: 'C#7', 98: 'D7', 99: 'D#7', 100: 'E7',
    101: 'F7', 102: 'F#7', 103: 'G7', 104: 'G#7', 105: 'A7', 106: 'A#7', 107: 'B7', 108: 'C8'
}


def display_notes():
    """
    Display the notes being played on the screen as text in a horizontal line.
    The notes are shown as a space-separated list.
    """
    screen.fill(BLACK)

    # Create a list of the currently played notes (sorted) and join them as a string
    notes_list = [MIDI_NOTE_NAMES.get(note, 'Unknown') for note in sorted(playing_notes)]
    notes_text = ' '.join(notes_list)

    # Render the notes text and display it
    note_text_render = font.render(notes_text, True, WHITE)
    screen.blit(note_text_render, (20, screen_height // 2 - 12))  # Vertical centering

    pygame.display.flip()


def play_midi():
    """
    Plays the MIDI file and displays the currently played notes as a text list on the screen.
    """
    global playing_notes
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()

    # Event loop to monitor MIDI events and display notes
    for msg in midi.play():
        if msg.type == 'note_on' and msg.velocity > 0:  # When a note is pressed
            playing_notes.add(msg.note)
        elif msg.type == 'note_off':  # When a note is released
            playing_notes.discard(msg.note)

        # Monitor the pygame window and quit event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        # Display the notes as a space-separated list
        display_notes()

        # Wait for the next event to be processed
        time.sleep(0.05)


# Run the program
play_midi()
