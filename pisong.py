#!/usr/bin/env python3

import time
import subprocess
from os import getenv
from glob import glob
from random import choice

from envirophat import motion, leds
import speakerphat

print("""Play random song when moved.

Press Ctrl+C to exit.

""")

class PiSong:
    def __init__(self):
        self.readings = []
        self.last_z = 0
        self.motion_threshold = float(getenv('MOTION_THRESHOLD', 0.1))
        print("threshold: {}".format(self.motion_threshold))
        self.motion_sleep = float(getenv('MOTION_SLEEP', 0.01))
        print("sleep: {}".format(self.motion_sleep))

    def play(self, song):
        self.call(['/usr/bin/mpg321', song])

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

    def read_z(self):
        self.readings.append(motion.accelerometer().z)
        self.readings = self.readings[-4:]
        return sum(self.readings) / len(self.readings)

    def sleep(self):
        time.sleep(self.motion_sleep)

    def detect_motion(self):
        z = self.read_z()
        z_delta = abs(z - self.last_z)
        if self.last_z > 0 and z_delta > self.motion_threshold:
            self.on_motion(z, z_delta)
            z = 0
        self.last_z = z
        self.sleep()

    def on_motion(self, z, z_delta):
        print("Motion detected: [last_z:{}] [z:{}] [z_delta:{}]".format(self.last_z, z, z_delta))
        leds.on()
        self.play(self.song())
        print("Done playing")
        leds.off()

    def run(self):
        self.sleep()
        while True:
            self.detect_motion()

if __name__ == "__main__":
    try:
        PiSong().run()
    except KeyboardInterrupt:
        leds.off()
        speakerphat.clear()
