#!/usr/bin/env python

import time
import subprocess

from envirophat import motion, leds
import speakerphat

print("""Play random song when moved.

Press Ctrl+C to exit.

""")

class PiSong:
    THRESHOLD = 0.05
    SLEEP = 0.001

    def __init__(self):
        self.readings = []
        self.last_z = 0

    def play(self):
        print("Motion Detected!!!")
        leds.on()

    def play(self):
        self.call(['/usr/bin/mpg321', self.song()])

    def song(self):
        return choice(self.songs())

    def songs(self):
        return glob("{}/*{}".format(self.path(), self.ext()))

    def path(self):
        return getenv('MUSIC_PATH', '/home/pi/music')

    def ext(self):
        return getenv('MUSIC_EXTENSION', '.mp3')

    def call(self, cmd):
        subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def detect_motion(self):
        self.readings.append(motion.accelerometer().z)
        self.readings = self.readings[-4:]
        z = sum(self.readings) / len(self.readings)
        z_delta = abs(z - self.last_z)
        if self.last_z > 0 and z_delta > self.THRESHOLD:
            print("Motion detected: [last_z:{}] [z:{}] [z_delta:{}]".format(self.last_z, z, z_delta))
            self.play()
            print("Done playing")
            leds.off()
        self.last_z = z
        time.sleep(self.SLEEP)

    def run(self):
        while True:
            self.detect_motion()

if __name__ == "__main__":
    try:
        PiSong().run()
    except KeyboardInterrupt:
        leds.off()
        speakerphat.clear()
