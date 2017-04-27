#!/usr/bin/env python3

"""piscroller.py

Usage:
  scroller.py [--brightness=<b>] [--rotate] [--sleep=<s>] [--interval=<s>] [--loop] [--upper] <message>
  scroller.py (-h | --help)
  scroller.py --version

Options:
  -h --help         Show this screen.
  --version         Show version
  --rotate          Rotate 180 degrees
  --brightness=<b>  Brightness level 1-255 [default: 2]
  --interval=<s>    Seconds between each time scroll moves [default: 0.1]
  --sleep=<s>       Seconds to pause after scrolling message [default: 0]
  --loop            Loop message forever.
  --upper           Make text upper case

"""

# TODO: Should just add job to same queue as PiAPI
# TODO: Setup virtualenv
# TODO: Setup setuptools

import sys
import time
import signal

import scrollphat
from docopt import docopt

class ScrollJob:
    def __init__(self, options):
        self.options = options

    def init(self):
        scrollphat.set_brightness(self.options['brightness'])
        scrollphat.set_rotate(self.options['rotate'])

        message = self.options['message'] + '    '
        if self.options['upper'] == True:
            message = message.upper()
        scrollphat.write_string(message, 11)

    def run(self):
        self.init()
        length = scrollphat.buffer_len()
        if self.options['loop'] == True:
            counter = 0
            while True:
                self.scroll()
                counter += 1
                if counter % length == 0:
                    time.sleep(self.options['sleep'])
        else:
            for i in range(length):
                self.scroll()
            time.sleep(self.options['sleep'])

    def scroll(self):
        scrollphat.scroll()
        time.sleep(self.options['interval'])

    def cleanup(self):
        scrollphat.clear()

class JobCommand:
    def __init__(self, job, opts):
        self.job = job(self.parse_options(opts))
        self.setup_signal_handlers()

    def parse_options(self, opts):
        options = {
            'rotate': opts['--rotate'],
            'loop': opts['--loop'],
            'brightness': int(opts['--brightness']),
            'upper': opts['--upper'],
            'sleep': float(opts['--sleep']),
            'interval': float(opts['--interval']),
            'message': opts['<message>'],
        }

        return options

    def execute(self):
        self.job.run()
        sys.exit(0)

    def setup_signal_handlers(self):
        signal.signal(signal.SIGINT, self.cleanup)
        signal.signal(signal.SIGTERM, self.cleanup)

    def cleanup(self, signum, frame):
        self.job.cleanup()
        sys.exit(-1)

if __name__ == '__main__':
    opts = docopt(__doc__, version='Scroller v1.1')
    JobCommand(ScrollJob, opts).execute()

