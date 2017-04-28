#!/usr/bin/env python3

"""piscroller.py

Usage:
  piscroller.py [--brightness=<b>] [--interval=<s>] [--sleep=<s>] [--loop] [--rotate] [--upper] <message>
  piscroller.py (-h | --help)
  piscroller.py --version

Options:
  -h --help         Show this screen.
  --version         Show version
  --brightness=<b>  Brightness level 1-255 [default: 2]
  --interval=<s>    Seconds between each time scroll moves [default: 0.1]
  --sleep=<s>       Seconds to pause after scrolling message [default: 0]
  --loop            Loop message forever.
  --rotate          Rotate 180 degrees
  --upper           Make text upper case

"""

# TODO: Should just add job to same queue as PiAPI
# TODO: Setup virtualenv
# TODO: Setup setuptools

import sys
import signal

from docopt import docopt
from pijobs.scrolljob import ScrollJob

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
    opts = docopt(__doc__, version='PiScroller v1.1')
    JobCommand(ScrollJob, opts).execute()

