PiSong
======

Play a random song when Pi is moved.

Requirements
------------

 * Speakerphat
 * Envirophat
 * mpg321

Install
-------

Run the following command:

```
apt-get install mpg321
pip install -r requirements.txt
```

Configuration
-------------

Create a file called `.env` in the pisong directory with the following
content:

```
MUSIC_PATH=/home/pi/music   # Point to directory where your music is located.
MUSIC_EXTENSION=.mp3        # Set the extension of song files.
MOTION_THRESHOLD=0.1        # How sensitive the motion detection should be.
MOTION_SLEEP=0.01           # Sleep time between detecting motion.
```
