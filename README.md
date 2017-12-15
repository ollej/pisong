PiSong
======

Play a random song when Pi is moved.

Requirements
------------

 * Speakerphat
 * Envirophat

Install
-------

Run the following command:

```
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configuration
-------------

Create a file called `.env` in the pisong directory with the following
content:

```
MUSIC_PATH=/home/pi/music   # Point to directory where your music is located.
MUSIC_EXTENSION=.mp3        # Set the extension of song files.
```
