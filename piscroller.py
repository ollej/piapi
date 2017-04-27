#!/usr/bin/env python3

"""piscroller.py

Usage:
  scroller.py [--brightness=<b>] [--rotate] [--sleep=<s>] [--loop] [--upper] <message>
  scroller.py (-h | --help)
  scroller.py --version

Options:
  -h --help         Show this screen.
  --version         Show version
  --rotate          Rotate 180 degrees
  --brightness=<b>  Brightness level 1-255 [default: 2]
  --sleep=<s>       Seconds between each time scroll moves [default: 0.1]
  --loop            Loop message forever.
  --upper           Make text upper case

"""

# TODO: Refactor into class for CLI handling and Job for scrolling.
# TODO: Reuse signal handler from pimon.py
# TODO: Should just add job to same queue as PiAPI
# TODO: Setup virtualenv
# TODO: Setup setuptools

import sys
import time

import scrollphat
from docopt import docopt


def scroll(opts):
    try:
        scrollphat.scroll()
        time.sleep(float(opts['--sleep']))
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)

if __name__ == '__main__':
    opts = docopt(__doc__, version='Scroller v1.0')

    scrollphat.set_brightness(int(opts['--brightness']))
    scrollphat.set_rotate(opts['--rotate'])

    message = opts['<message>'] + '    '
    if opts['--upper'] == True:
        message = message.upper()
    scrollphat.write_string(message, 11)

    if opts['--loop'] == True:
        while True:
            scroll(opts)
    else:
        length = scrollphat.buffer_len()
        for i in range(length):
            scroll(opts)
        scrollphat.clear()
        sys.exit(0)

