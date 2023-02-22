import time
import random
import threading
from pydub import AudioSegment
from pydub.playback import play

bell_sound = AudioSegment.from_wav("./bell.wav")

def play_bell():
    global timer
    # Generate a interval of 90 minutes
    interval = (5400)
    # Schedule the next beep sound to play after the interval
    timer = threading.Timer(interval, play_bell)
    timer.start()
    # Play the beep sound
    play(bell_sound)

def main():
    # Start the first bell sound immediately
    play_bell()
    # Wait for the user to press enter to stop the program
    input("Press Enter to stop...")
    # Stop the timer for the next beep sound
    timer.cancel()

if __name__ == "__main__":
    main()