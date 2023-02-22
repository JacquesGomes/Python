import time
import random
import threading
from pydub import AudioSegment
from pydub.playback import play

beep_sound = AudioSegment.from_wav("./beep.wav")

def play_beep():
    global timer
    # Generate a random interval between 300 and 600 seconds (5-10 minutes)
    interval = random.randint(600, 900)
    # Schedule the next beep sound to play after the interval
    timer = threading.Timer(interval, play_beep)
    timer.start()
    # Play the beep sound
    play(beep_sound)

def main():
    # Start the first beep sound immediately
    play_beep()
    # Wait for the user to press enter to stop the program
    input("Press Enter to stop...")
    # Stop the timer for the next beep sound
    timer.cancel()

if __name__ == "__main__":
    main()