import time
import random
import threading
from pydub import AudioSegment
from pydub.playback import play

beep_sound = AudioSegment.from_wav("./beep.wav")
bell_sound = AudioSegment.from_wav("./bell.wav")

def play_beep():
    play(beep_sound)

def play_bell():
    play(bell_sound)

class Timer:
    def __init__(self, interval, function):
        self.interval = interval
        self.function = function
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.__run)
            self.thread.start()

    def stop(self):
        self.running = False

    def __run(self):
        while self.running:
            self.function()
            time.sleep(self.interval)

def main():
    # Play initial test sounds
    play_beep()
    time.sleep(1)
    play_bell()
    time.sleep(1)

    beep_timer = Timer(300, play_beep)  # 5 minutes
    beep_timer.start()

    bell_timer = Timer(5400, play_bell)  # 90 minutes
    bell_timer.start()

    input("Press Enter to stop...")
    beep_timer.stop()
    bell_timer.stop()

if __name__ == "__main__":
    main()